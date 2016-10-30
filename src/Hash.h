#pragma once

#include <boost/python.hpp>
#include <boost/python/raw_function.hpp>
namespace py = boost::python;

#if defined(_MSC_VER)
  typedef int int32_t;
  typedef unsigned int uint32_t;
  typedef __int64 int64_t;
  typedef unsigned __int64 uint64_t;

  typedef struct {
    uint64_t low, high;
  } uint128_t;

  #define U128_LO(v) (v.low)
  #define U128_HI(v) (v.high)

  #define U128_NEW(LO, HI) { .low = LO, .high = HI}
#else
  #include <stdint.h>     /* defines uint32_t etc */

  typedef boost::uint128_type uint128_t;

  #define U128_LO(v) (v >> 64)
  #define U128_HI(v) (v & 0xFFFFFFFFFFFFFFFF)

  #define U128_NEW(LO, HI) ((((uint128_t) HI) << 64) + LO)
#endif

namespace internal
{
  template <typename T>
  PyObject *convert(const T& value);

  template <>
  inline PyObject *convert(const int& value)
  {
    return ::PyLong_FromLong(value);
  }

  template <>
  inline PyObject *convert(const unsigned int& value)
  {
    return ::PyLong_FromSize_t(value);
  }

  template <>
  inline PyObject *convert(const long& value)
  {
    return ::PyLong_FromLong(value);
  }

  template <>
  inline PyObject *convert(const unsigned long& value)
  {
    return ::PyLong_FromUnsignedLong(value);
  }

  template <>
  inline PyObject *convert(const long long& value)
  {
    return ::PyLong_FromLongLong(value);
  }

  template <>
  inline PyObject *convert(const unsigned long long& value)
  {
    return ::PyLong_FromUnsignedLongLong(value);
  }

  template <>
  inline PyObject *convert(const uint128_t& value)
  {
    return ::_PyLong_FromByteArray((const unsigned char*) &value, sizeof(uint128_t), /*little_endian*/ 1, /*is_signed*/ 0);
  }
}

template <typename T>
class Hasher
{
protected:
  Hasher(void) {}
public:
  virtual ~Hasher(void) {}

  static py::object CallWithArgs(py::tuple args, py::dict kwds);

  static void Export(const char *name);
};

template <typename T>
inline void Hasher<T>::Export(const char *name)
{
  py::class_<T, boost::noncopyable>(name, py::init<>())
    .def("__call__", py::raw_function(&T::CallWithArgs))
    ;
}

template <typename T>
T extract_hash_value(PyObject *obj)
{
  T value = 0;

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
    ::PyErr_SetString(::PyExc_TypeError, "unknown `seed` type, expected `int` or `long`");
  }

  return value;
}

template <>
uint64_t extract_hash_value<uint64_t>(PyObject *obj)
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
    ::PyErr_SetString(::PyExc_TypeError, "unknown `seed` type, expected `int` or `long`");
  }

  return value;
}

template<>
uint128_t extract_hash_value<uint128_t>(PyObject *obj)
{
  uint128_t value = { 0 };

  if (PyLong_Check(obj))
  {
    _PyLong_AsByteArray((PyLongObject *)obj, (unsigned char *) &value, sizeof(uint128_t), /*little_endian*/ 1, /*is_signed*/ 0);
  }
  else
  {
    ::PyErr_SetString(::PyExc_TypeError, "unknown `seed` type, expected `long`");
  }

  return value;
}

template <typename T>
inline py::object Hasher<T>::CallWithArgs(py::tuple args, py::dict kwds)
{
  size_t argc = ::PyTuple_Size(args.ptr());

  if (argc == 0)
  {
    ::PyErr_SetString(::PyExc_TypeError, "missed self argument");
    return py::object(py::handle<>(Py_None));
  }

  py::object self = args[0];
  py::extract<T&> extractor(self);

  if (!extractor.check())
  {
    ::PyErr_SetString(::PyExc_TypeError, "wrong type of self argument");
    return py::object(py::handle<>(Py_None));
  }

  T& hasher = extractor();
  py::list argv(args.slice(1, py::_));

  typename T::hash_value_t value = {0};

  if (kwds.has_key("seed")) value = extract_hash_value<typename T::hash_value_t>(kwds.get("seed").ptr());

  for (Py_ssize_t i=0; i<PyList_Size(argv.ptr()); i++)
  {
    py::object arg = argv[i];

  #if PY_MAJOR_VERSION < 3
    if (PyString_CheckExact(arg.ptr()))
    {
      char *buf = NULL;
      Py_ssize_t len = 0;

      if (0 == PyString_AsStringAndSize(arg.ptr(), &buf, &len))
      {
        value = hasher(buf, len, value);
      }
    }
  #else
    if (PyBytes_Check(arg.ptr()))
    {
      char *buf = NULL;
      Py_ssize_t len = 0;

      if (0 == PyBytes_AsStringAndSize(arg.ptr(), &buf, &len))
      {
        value = hasher((void *) buf, len, value);
      }
    }
  #endif
    else if (PyUnicode_CheckExact(arg.ptr()))
    {
    #if PY_MAJOR_VERSION > 2
    # ifdef Py_UNICODE_WIDE
      py::object utf16 = py::object(py::handle<>(PyUnicode_AsUTF16String(arg.ptr())));

      char *buf = NULL;
      Py_ssize_t len = 0;

      if (0 == PyBytes_AsStringAndSize(utf16.ptr(), &buf, &len))
      {
        buf += 2;
        len -= 2;
      }
    # else
      Py_UCS2 *buf = PyUnicode_2BYTE_DATA(arg.ptr());
      Py_ssize_t len = PyUnicode_GET_LENGTH(arg.ptr()) * 2;
    # endif
    #else
    # ifdef Py_UNICODE_WIDE
      py::object utf16 = py::object(py::handle<>(PyUnicode_AsUTF16String(arg.ptr())));

      const char *buf = PyString_AS_STRING(utf16.ptr()) + 2; // skip the BOM
      Py_ssize_t len = PyString_GET_SIZE(utf16.ptr()) - 2;
    # else
      const char *buf = PyUnicode_AS_DATA(arg.ptr());
      Py_ssize_t len = PyUnicode_GET_DATA_SIZE(arg.ptr());
    # endif
    #endif

      value = hasher((void *) buf, len, value);
    }
  #if PY_MAJOR_VERSION < 3
    else if (PyBuffer_Check(arg.ptr()))
    {
      const void *buf = NULL;
      Py_ssize_t len = 0;

      if (0 == PyObject_AsReadBuffer(arg.ptr(), &buf, &len))
      {
        value = hasher((void *) buf, len, value);
      }
    }
  #endif
    else
    {
      ::PyErr_SetString(::PyExc_TypeError, "wrong type of argument");

      py::throw_error_already_set();

      return py::object();
    }
  }

  return py::object(py::handle<>(internal::convert(value)));
}
