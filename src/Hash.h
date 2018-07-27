#pragma once

#include <algorithm>

#include <pybind11/pybind11.h>

namespace py = pybind11;

#ifdef _MSC_VER

typedef int int32_t;
typedef unsigned int uint32_t;
typedef __int64 int64_t;
typedef unsigned __int64 uint64_t;

#else // _MSC_VER

#include <stdint.h>

#ifdef SUPPORT_INT128

typedef unsigned __int128 uint128_t;
typedef std::array<uint64_t, 4> uint256_t;

#define U128_LO(v) (v >> 64)
#define U128_HI(v) (v & 0xFFFFFFFFFFFFFFFF)

#define U128_NEW(LO, HI) ((((uint128_t)HI) << 64) + LO)

namespace pybind11
{
namespace detail
{
template <>
struct type_caster<uint128_t>
{
public:
  PYBIND11_TYPE_CASTER(uint128_t, _("uint128_t"));

  bool load(handle src, bool)
  {
    PyObject *source = src.ptr();
    PyObject *tmp = PyNumber_Long(source);
    if (!tmp)
      return false;
    _PyLong_AsByteArray((PyLongObject *)tmp, (unsigned char *)&value, sizeof(uint128_t), /*little_endian*/ 1, /*is_signed*/ 0);
    Py_DECREF(tmp);

    return !PyErr_Occurred();
  }

  static handle cast(uint128_t src, return_value_policy /* policy */, handle /* parent */)
  {
    return ::_PyLong_FromByteArray((const unsigned char *)&src, sizeof(uint128_t), /*little_endian*/ 1, /*is_signed*/ 0);
  }
};

template <>
struct type_caster<uint256_t>
{
public:
  PYBIND11_TYPE_CASTER(uint256_t, _("uint256_t"));

  bool load(handle src, bool)
  {
    PyObject *source = src.ptr();
    PyObject *tmp = PyNumber_Long(source);
    if (!tmp)
      return false;
    _PyLong_AsByteArray((PyLongObject *)tmp, (unsigned char *)value.data(), sizeof(uint256_t), /*little_endian*/ 1, /*is_signed*/ 0);
    Py_DECREF(tmp);

    return !PyErr_Occurred();
  }

  static handle cast(uint256_t src, return_value_policy /* policy */, handle /* parent */)
  {
    return ::_PyLong_FromByteArray((const unsigned char *)src.data(), sizeof(uint256_t), /*little_endian*/ 1, /*is_signed*/ 0);
  }
};
} // namespace detail
} // namespace pybind11

#endif // SUPPORT_INT128

#endif // _MSC_VER

namespace internal
{
const size_t BOM_MARK_SIZE = 2;

template <typename T>
PyObject *wrap_value(const T &value);

template <>
PyObject *wrap_value(const int &value)
{
  return PyLong_FromLong(value);
}

template <>
PyObject *wrap_value(const unsigned int &value)
{
  return PyLong_FromSize_t(value);
}

template <>
PyObject *wrap_value(const long &value)
{
  return PyLong_FromLong(value);
}

template <>
PyObject *wrap_value(const unsigned long &value)
{
  return PyLong_FromUnsignedLong(value);
}

template <>
PyObject *wrap_value(const long long &value)
{
  return PyLong_FromLongLong(value);
}

template <>
PyObject *wrap_value(const unsigned long long &value)
{
  return PyLong_FromUnsignedLongLong(value);
}

#ifndef _MSC_VER
template <>
PyObject *wrap_value(const uint128_t &value)
{
  return ::_PyLong_FromByteArray((const unsigned char *)&value, sizeof(uint128_t), /*little_endian*/ 1, /*is_signed*/ 0);
}

template <>
PyObject *wrap_value(const uint256_t &value)
{
  return ::_PyLong_FromByteArray((const unsigned char *)value.data(), sizeof(uint256_t), /*little_endian*/ 1, /*is_signed*/ 0);
}
#endif

template <typename T>
T extract_value(PyObject *obj);

template <>
uint32_t extract_value(PyObject *obj)
{
  uint32_t value = 0;

  if (PyLong_Check(obj))
  {
    value = PyLong_AsUnsignedLong(obj);
  }
#if PY_MAJOR_VERSION < 3
  else if (PyInt_Check(obj))
  {
    value = PyInt_AsUnsignedLongMask(obj);
  }
#endif
  else
  {
    throw std::invalid_argument("unknown `seed` type, expected `int` or `long`");
  }

  return value;
}

template <>
uint64_t extract_value<uint64_t>(PyObject *obj)
{
  uint64_t value = 0;

  if (PyLong_Check(obj))
  {
    value = PyLong_AsUnsignedLongLong(obj);
  }
#if PY_MAJOR_VERSION < 3
  else if (PyInt_Check(obj))
  {
    value = PyInt_AsUnsignedLongLongMask(obj);
  }
#endif
  else
  {
    throw std::invalid_argument("unknown `seed` type, expected `int` or `long`");
  }

  return value;
}

#ifdef SUPPORT_INT128

template <>
uint128_t extract_value<uint128_t>(PyObject *obj)
{
  uint128_t value = {0};

  if (PyLong_Check(obj))
  {
    _PyLong_AsByteArray((PyLongObject *)obj, (unsigned char *)&value, sizeof(uint128_t), /*little_endian*/ 1, /*is_signed*/ 0);
  }
  else
  {
    throw std::invalid_argument("unknown `seed` type, expected `int` or `long`");
  }

  return value;
}

template <>
uint256_t extract_value<uint256_t>(PyObject *obj)
{
  uint256_t value = {};

  if (PyLong_Check(obj))
  {
    _PyLong_AsByteArray((PyLongObject *)obj, (unsigned char *)&value, sizeof(uint256_t), /*little_endian*/ 1, /*is_signed*/ 0);
  }
  else
  {
    throw std::invalid_argument("unknown `seed` type, expected `int` or `long`");
  }

  return value;
}
#endif

} // namespace internal

template <typename T, typename S, typename H = S>
class Hasher
{
public:
  typedef S seed_value_t;
  typedef H hash_value_t;

private:
  seed_value_t _seed;

protected:
  Hasher(seed_value_t seed = {}) : _seed(seed) {}

public:
  virtual ~Hasher(void) {}

  static py::object CallWithArgs(py::args args, py::kwargs kwargs);

  static void Export(const py::module &m, const char *name)
  {
    py::class_<T>(m, name)
        .def(py::init<seed_value_t>(), py::arg("seed") = 0)
        .def_readwrite("seed", &T::_seed)
        .def("__call__", &T::CallWithArgs);
  }
};

template <typename T, typename H>
class Fingerprinter
{
public:
  typedef H fingerprint_t;

  virtual ~Fingerprinter(void) {}

  static py::object CallWithArgs(py::args args, py::kwargs kwargs);

  static void Export(const py::module &m, const char *name)
  {
    py::class_<T>(m, name)
        .def(py::init<>())
        .def("__call__", &T::CallWithArgs);
  }
};

template <typename T, typename S, typename H>
py::object Hasher<T, S, H>::CallWithArgs(py::args args, py::kwargs kwargs)
{
  if (args.size() == 0)
  {
    throw std::invalid_argument("missed self argument");
  }

  py::object self = args[0];

  if (!self)
  {
    throw std::invalid_argument("wrong type of self argument");
  }

  const T &hasher = self.cast<T>();
  typename T::hash_value_t value = kwargs.contains("seed") ? internal::extract_value<typename T::hash_value_t>(kwargs["seed"].ptr()) : hasher._seed;

  std::for_each(std::next(args.begin()), args.end(), [&](const py::handle &arg) {
    const char *buf = nullptr;
    Py_ssize_t len = 0;

#if PY_MAJOR_VERSION < 3
    if (PyString_CheckExact(arg.ptr()))
    {
      if (-1 == PyString_AsStringAndSize(arg.ptr(), (char **)&buf, &len))
      {
        throw py::error_already_set();
      }
    }
#else
    if (PyBytes_CheckExact(arg.ptr()))
    {
      if (-1 == PyBytes_AsStringAndSize(arg.ptr(), (char **)&buf, &len))
      {
        throw py::error_already_set();
      }
    }
#endif
    else if (PyUnicode_CheckExact(arg.ptr()))
    {
#if PY_MAJOR_VERSION > 2
#ifndef Py_UNICODE_WIDE
      if (PyUnicode_2BYTE_KIND == PyUnicode_KIND(arg.ptr()) && PyUnicode_IS_READY(arg.ptr()))
      {
        buf = PyUnicode_2BYTE_DATA(arg.ptr());
        len = PyUnicode_GET_LENGTH(arg.ptr()) * Py_UNICODE_SIZE;
      }
      else
      {
#endif
        py::object utf16 = py::reinterpret_steal<py::object>(PyUnicode_AsUTF16String(arg.ptr()));

        if (!utf16)
        {
          throw py::error_already_set();
        }

        if (-1 == PyBytes_AsStringAndSize(utf16.ptr(), (char **)&buf, &len))
        {
          throw py::error_already_set();
        }

        buf += internal::BOM_MARK_SIZE;
        len -= internal::BOM_MARK_SIZE;

        if (buf && len)
        {
          value = hasher((void *)buf, len, value);
          return;
        }
#ifndef Py_UNICODE_WIDE
      }
#endif
#else
#ifdef Py_UNICODE_WIDE
      py::object utf16 = py::reinterpret_steal<py::object>(PyUnicode_AsUTF16String(arg.ptr()));

      if (!utf16) {
        throw py::error_already_set();
      }

      buf = PyString_AS_STRING(utf16.ptr()) + internal::BOM_MARK_SIZE;
      len = PyString_GET_SIZE(utf16.ptr()) - internal::BOM_MARK_SIZE;
#else
      buf = PyUnicode_AS_DATA(arg.ptr());
      len = PyUnicode_GET_DATA_SIZE(arg.ptr());
#endif
      if (buf && len)
      {
        value = hasher((void *)buf, len, value);
        return;
      }
#endif
    }
#if PY_MAJOR_VERSION < 3
    else if (PyObject_CheckReadBuffer(arg.ptr()))
    {
      if (-1 == PyObject_AsReadBuffer(arg.ptr(), (const void **)&buf, &len))
      {
        throw py::error_already_set();
      }
    }
#endif
    else
    {
      throw std::invalid_argument("wrong type of argument");
    }

    if (buf && len)
    {
      value = hasher((void *)buf, len, value);
    }
  });

  return py::reinterpret_steal<py::object>(internal::wrap_value(value));
}

template <typename T, typename H>
py::object Fingerprinter<T, H>::CallWithArgs(py::args args, py::kwargs kwargs)
{
  if (args.size() == 0)
  {
    throw std::invalid_argument("missed self argument");
  }

  py::object self = args[0];

  if (!self)
  {
    throw std::invalid_argument("wrong type of self argument");
  }

  const T &fingerprinter = self.cast<T>();
  std::vector<typename T::fingerprint_t> results;

  std::transform(std::next(args.begin()), args.end(), std::back_inserter(results), [&](const py::handle &arg) {
    const char *buf = nullptr;
    Py_ssize_t len = 0;

#if PY_MAJOR_VERSION < 3
    if (PyString_CheckExact(arg.ptr()))
    {
      if (-1 == PyString_AsStringAndSize(arg.ptr(), (char **)&buf, &len))
      {
        throw py::error_already_set();
      }
    }
#else
    if (PyBytes_CheckExact(arg.ptr()))
    {
      if (-1 == PyBytes_AsStringAndSize(arg.ptr(), (char **)&buf, &len))
      {
        throw py::error_already_set();
      }
    }
#endif
    else if (PyUnicode_CheckExact(arg.ptr()))
    {
#if PY_MAJOR_VERSION > 2
#ifndef Py_UNICODE_WIDE
      if (PyUnicode_2BYTE_KIND == PyUnicode_KIND(arg.ptr()) && PyUnicode_IS_READY(arg.ptr()))
      {
        buf = PyUnicode_2BYTE_DATA(arg.ptr());
        len = PyUnicode_GET_LENGTH(arg.ptr()) * Py_UNICODE_SIZE;
      }
      else
      {
#endif
        py::object utf16 = py::reinterpret_steal<py::object>(PyUnicode_AsUTF16String(arg.ptr()));

        if (!utf16)
        {
          throw py::error_already_set();
        }

        if (-1 == PyBytes_AsStringAndSize(utf16.ptr(), (char **)&buf, &len))
        {
          throw py::error_already_set();
        }

        buf += internal::BOM_MARK_SIZE;
        len -= internal::BOM_MARK_SIZE;

        return fingerprinter((void *)buf, len);
#ifndef Py_UNICODE_WIDE
      }
#endif
#else
#ifdef Py_UNICODE_WIDE
      py::object utf16 = py::reinterpret_steal<py::object>(PyUnicode_AsUTF16String(arg.ptr()));

      if (!utf16) {
        throw py::error_already_set();
      }

      buf = PyString_AS_STRING(utf16.ptr()) + internal::BOM_MARK_SIZE;
      len = PyString_GET_SIZE(utf16.ptr()) - internal::BOM_MARK_SIZE;
#else
      buf = PyUnicode_AS_DATA(arg.ptr());
      len = PyUnicode_GET_DATA_SIZE(arg.ptr());
#endif
        return fingerprinter((void *)buf, len);
#endif
    }
#if PY_MAJOR_VERSION < 3
    else if (PyObject_CheckReadBuffer(arg.ptr()))
    {
      if (-1 == PyObject_AsReadBuffer(arg.ptr(), (const void **)&buf, &len))
      {
        throw py::error_already_set();
      }
    }
#endif
    else
    {
      throw std::invalid_argument("wrong type of argument");
    }

    return fingerprinter((void *)buf, len);
  });

  if (results.size() == 1)
  {
    return py::reinterpret_steal<py::object>(internal::wrap_value(results.front()));
  }

  return py::make_iterator(results.begin(), results.end());
}
