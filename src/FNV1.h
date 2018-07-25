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
class fnv_t : public Hasher<fnv_t<T, ORDER>, T>
{
public:
  typedef Hasher<fnv_t<T, ORDER>, T> __hasher_t;
  typedef typename __hasher_t::hash_value_t hash_value_t;
  typedef typename __hasher_t::seed_value_t seed_value_t;

  fnv_t(seed_value_t seed = 0) : __hasher_t(seed) {}

  const hash_value_t operator()(void *buf, size_t len, seed_value_t seed) const;
};

typedef fnv_t<Fnv32_t, true> fnv1_32_t;
typedef fnv_t<Fnv32_t, false> fnv1a_32_t;
typedef fnv_t<Fnv64_t, true> fnv1_64_t;
typedef fnv_t<Fnv64_t, false> fnv1a_64_t;

template <>
const fnv1_32_t::hash_value_t fnv1_32_t::operator()(void *buf, size_t len, fnv1_32_t::seed_value_t seed) const
{
  return fnv_32_buf(buf, len, seed);
}

template <>
const fnv1a_32_t::hash_value_t fnv1a_32_t::operator()(void *buf, size_t len, fnv1a_32_t::seed_value_t seed) const
{
  return fnv_32a_buf(buf, len, seed);
}

template <>
const fnv1_64_t::hash_value_t fnv1_64_t::operator()(void *buf, size_t len, fnv1_64_t::seed_value_t seed) const
{
  return fnv_64_buf(buf, len, seed);
}

template <>
const fnv1a_64_t::hash_value_t fnv1a_64_t::operator()(void *buf, size_t len, fnv1a_64_t::seed_value_t seed) const
{
  return fnv_64a_buf(buf, len, seed);
}
