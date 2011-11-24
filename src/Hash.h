#pragma once

#if defined(_MSC_VER)
  typedef unsigned char uint8_t;
  typedef unsigned short uint16_t;
  typedef unsigned long uint32_t;
  typedef unsigned __int64 uint64_t;  
#else
  #include <stdint.h>     /* defines uint32_t etc */
#endif

#include <boost/python.hpp>
#include <boost/python/raw_function.hpp>
namespace py = boost::python;

namespace internal
{
  template <typename T>
  PyObject *convert(const T& value);

  template <>
  inline PyObject *convert(const int& value)
  {
    return ::PyInt_FromLong(value);
  }

  template <>
  inline PyObject *convert(const unsigned int& value)
  {
    return ::PyInt_FromSize_t(value);
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

  typename T::hash_value_t value = 0;

  for (Py_ssize_t i=0; i<PyList_Size(argv.ptr()); i++)
  {
    py::object arg = argv[i];

    if (PyString_CheckExact(arg.ptr()))
    {
      char *buf = NULL;
      Py_ssize_t len = 0;

      if (0 == PyString_AsStringAndSize(arg.ptr(), &buf, &len))
      {
        value = hasher(buf, len, value);
      }
    }
    else if (PyUnicode_CheckExact(arg.ptr()))
    {
    #ifdef Py_UNICODE_WIDE
      py::object utf16 = py::object(py::handle<>(PyUnicode_AsUTF16String(arg.ptr()));

      const char *buf = PyUnicode_AS_DATA(utf16.ptr());
      Py_ssize_t len = PyUnicode_GET_DATA_SIZE(utf16.ptr());
    #else
      const char *buf = PyUnicode_AS_DATA(arg.ptr());
      Py_ssize_t len = PyUnicode_GET_DATA_SIZE(arg.ptr());
    #endif

      value = hasher((void *) buf, len, value);
    }
    else if (PyBuffer_Check(arg.ptr()))
    {
      const void *buf = NULL;
      Py_ssize_t len = 0;

      if (0 == PyObject_AsReadBuffer(arg.ptr(), &buf, &len))
      {
        value = hasher((void *) buf, len, value);
      }
    }
    else
    {
      ::PyErr_SetString(::PyExc_TypeError, "wrong type of argument");
      return py::object(py::handle<>(Py_None));
    }
  }

  return py::object(py::handle<>(internal::convert(value)));
}