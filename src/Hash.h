#pragma once

#include <algorithm>
#include <functional>

#include <pybind11/pybind11.h>

namespace py = pybind11;

const size_t BOM_MARK_SIZE = 2;

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

#if __BYTE_ORDER__ == __ORDER_LITTLE_ENDIAN__
const int IS_LITTLE_ENDIAN = 1;
#else
const int IS_LITTLE_ENDIAN = 0;
#endif
const int PyLong_Unsigned = 0;

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
    py::object n = py::reinterpret_steal<py::object>(PyNumber_Long(src.ptr()));

    if (!n)
    {
      return false;
    }

    _PyLong_AsByteArray((PyLongObject *)n.ptr(), (unsigned char *)&value, sizeof(uint128_t), IS_LITTLE_ENDIAN, PyLong_Unsigned);

    return !PyErr_Occurred();
  }

  static handle cast(uint128_t src, return_value_policy /* policy */, handle /* parent */)
  {
    return _PyLong_FromByteArray((const unsigned char *)&src, sizeof(uint128_t), IS_LITTLE_ENDIAN, PyLong_Unsigned);
  }
};

template <>
struct type_caster<uint256_t>
{
public:
  PYBIND11_TYPE_CASTER(uint256_t, _("uint256_t"));

  bool load(handle src, bool)
  {
    py::object n = py::reinterpret_steal<py::object>(PyNumber_Long(src.ptr()));

    if (!n)
    {
      return false;
    }

    _PyLong_AsByteArray((PyLongObject *)n.ptr(), (unsigned char *)&value, sizeof(uint256_t), IS_LITTLE_ENDIAN, PyLong_Unsigned);

    return !PyErr_Occurred();
  }

  static handle cast(uint256_t src, return_value_policy /* policy */, handle /* parent */)
  {
    return _PyLong_FromByteArray((const unsigned char *)src.data(), sizeof(uint256_t), IS_LITTLE_ENDIAN, PyLong_Unsigned);
  }
};
} // namespace detail
} // namespace pybind11

#endif // SUPPORT_INT128

#endif // _MSC_VER

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

void handle_data(PyObject *obj, std::function<void(const char *buf, Py_ssize_t len)> callback);

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
    PyErr_SetString(PyExc_TypeError, "wrong type of self argument");

    throw py::error_already_set();
  }

  const T &hasher = self.cast<T>();
  typename T::hash_value_t value = kwargs.contains("seed") ? kwargs["seed"].cast<typename T::hash_value_t>() : hasher._seed;

  std::for_each(std::next(args.begin()), args.end(), [&](const py::handle &arg) {
    handle_data(arg.ptr(), [&](const char *buf, Py_ssize_t len) {
      value = hasher((void *)buf, len, value);
    });
  });

  return py::cast(value);
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
    PyErr_SetString(PyExc_TypeError, "wrong type of self argument");

    throw py::error_already_set();
  }

  const T &fingerprinter = self.cast<T>();
  std::vector<typename T::fingerprint_t> results;

  std::for_each(std::next(args.begin()), args.end(), [&](const py::handle &arg) {
    handle_data(arg.ptr(), [&](const char *buf, Py_ssize_t len) {
      results.push_back(fingerprinter((void *)buf, len));
    });
  });

  if (results.size() == 1)
  {
    return py::cast(results.front());
  }

  py::list fingerprintes;

  for (auto result : results)
  {
    fingerprintes.append(py::cast(result));
  }

  return fingerprintes;
}

void handle_data(PyObject *obj, std::function<void(const char *buf, Py_ssize_t len)> callback)
{
  const char *buf = nullptr;
  Py_ssize_t len = 0;

#if PY_MAJOR_VERSION < 3
  if (PyString_CheckExact(obj))
  {
    if (-1 == PyString_AsStringAndSize(obj, (char **)&buf, &len))
    {
      throw py::error_already_set();
    }
  }
#else
  if (PyBytes_CheckExact(obj))
  {
    if (-1 == PyBytes_AsStringAndSize(obj, (char **)&buf, &len))
    {
      throw py::error_already_set();
    }
  }
#endif
  else if (PyUnicode_CheckExact(obj))
  {
#if PY_MAJOR_VERSION > 2
#ifndef Py_UNICODE_WIDE
    if (PyUnicode_2BYTE_KIND == PyUnicode_KIND(obj) && PyUnicode_IS_READY(obj))
    {
      buf = PyUnicode_2BYTE_DATA(obj);
      len = PyUnicode_GET_LENGTH(obj) * Py_UNICODE_SIZE;
    }
    else
    {
#endif
      py::object utf16 = py::reinterpret_steal<py::object>(PyUnicode_AsUTF16String(obj));

      if (!utf16)
      {
        throw py::error_already_set();
      }

      if (-1 == PyBytes_AsStringAndSize(utf16.ptr(), (char **)&buf, &len))
      {
        throw py::error_already_set();
      }

      buf += BOM_MARK_SIZE;
      len -= BOM_MARK_SIZE;

      callback(buf, len);
      return;
#ifndef Py_UNICODE_WIDE
    }
#endif
#else
#ifdef Py_UNICODE_WIDE
    py::object utf16 = py::reinterpret_steal<py::object>(PyUnicode_AsUTF16String(obj));

    if (!utf16)
    {
      throw py::error_already_set();
    }

    buf = PyString_AS_STRING(utf16.ptr()) + BOM_MARK_SIZE;
    len = PyString_GET_SIZE(utf16.ptr()) - BOM_MARK_SIZE;
#else
    buf = PyUnicode_AS_DATA(obj);
    len = PyUnicode_GET_DATA_SIZE(obj);
#endif

    callback(buf, len);
    return;
#endif
  }
#if PY_MAJOR_VERSION < 3
  else if (PyObject_CheckReadBuffer(obj))
  {
    if (-1 == PyObject_AsReadBuffer(obj, (const void **)&buf, &len))
    {
      throw py::error_already_set();
    }
  }
#endif
  else if (PyObject_CheckBuffer(obj))
  {
    Py_buffer view;

    if (-1 == PyObject_GetBuffer(obj, &view, PyBUF_SIMPLE) || !PyBuffer_IsContiguous(&view, 'C'))
    {
      throw std::invalid_argument("only support contiguous buffer");
    }

    callback((const char *)view.buf, view.len);
    return;
  }
  else if (PyMemoryView_Check(obj))
  {
    Py_buffer *view = PyMemoryView_GET_BUFFER(obj);

    if (!view || !PyBuffer_IsContiguous(view, 'C'))
    {
      throw std::invalid_argument("only support contiguous memoryview");
    }

    buf = (const char *)view->buf;
    len = view->len;
  }
  else
  {
    PyErr_SetString(PyExc_TypeError, "unsupported argument type");

    throw py::error_already_set();
  }

  callback(buf, len);
}
