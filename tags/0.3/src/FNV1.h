#pragma once

#include "Hash.h"

#include "fnv/fnv.h"

/**
 * FNV hashes are designed to be fast while maintaining a low collision rate. 
 * The FNV speed allows one to quickly hash lots of data while maintaining 
 * a reasonable collision rate. The high dispersion of the FNV hashes 
 * makes them well suited for hashing nearly identical strings such as URLs, 
 * hostnames, filenames, text, IP addresses, etc.
 *
 * http://isthe.com/chongo/tech/comp/fnv/
 *
 */
template <typename T, bool ORDER>
class fnv_t : public Hasher< fnv_t<T, ORDER> >
{
public:
  fnv_t() {}

  typedef T hash_value_t;

  T operator()(void *buf, size_t len, T val) const;
};

typedef fnv_t<Fnv32_t, true> fnv1_32_t;
typedef fnv_t<Fnv32_t, false> fnv1a_32_t;
typedef fnv_t<Fnv64_t, true> fnv1_64_t;
typedef fnv_t<Fnv64_t, false> fnv1a_64_t;

template <>
inline Fnv32_t fnv_t<Fnv32_t, true>::operator()(void *buf, size_t len, Fnv32_t val) const
{
  return fnv_32_buf(buf, len, val);
}

template <>
inline Fnv32_t fnv_t<Fnv32_t, false>::operator()(void *buf, size_t len, Fnv32_t val) const
{
  return fnv_32a_buf(buf, len, val);
}

template <>
inline Fnv64_t fnv_t<Fnv64_t, true>::operator()(void *buf, size_t len, Fnv64_t val) const
{
  return fnv_64_buf(buf, len, val);
}

template <>
inline Fnv64_t fnv_t<Fnv64_t, false>::operator()(void *buf, size_t len, Fnv64_t val) const
{
  return fnv_64a_buf(buf, len, val);
}