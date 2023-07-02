#pragma once

#include "Hash.h"

#define XXH_STATIC_LINKING_ONLY

#include "xxHash/xxhash.h"

template <typename T>
class xx_hash_t : public Hasher<xx_hash_t<T>, T>
{
public:
  typedef Hasher<xx_hash_t<T>, T> __hasher_t;
  typedef typename __hasher_t::hash_value_t hash_value_t;
  typedef typename __hasher_t::seed_value_t seed_value_t;

  xx_hash_t(seed_value_t seed = 0) : __hasher_t(seed) {}

  const hash_value_t operator()(void *buf, size_t len, seed_value_t seed) const;
};

typedef xx_hash_t<uint32_t> xx_hash_32_t;
typedef xx_hash_t<uint64_t> xx_hash_64_t;

template <>
const xx_hash_32_t::hash_value_t xx_hash_32_t::operator()(void *buf, size_t len, xx_hash_32_t::seed_value_t seed) const
{
  return XXH32(buf, len, seed);
}
template <>
const xx_hash_64_t::hash_value_t xx_hash_64_t::operator()(void *buf, size_t len, xx_hash_64_t::seed_value_t seed) const
{
  return XXH64(buf, len, seed);
}

template <typename T>
class xxh3_hash_t : public Hasher<xxh3_hash_t<T>, uint64_t, T>
{
public:
  typedef Hasher<xxh3_hash_t<T>, uint64_t, T> __hasher_t;
  typedef typename __hasher_t::hash_value_t hash_value_t;
  typedef typename __hasher_t::seed_value_t seed_value_t;

  xxh3_hash_t(seed_value_t seed = 0) : __hasher_t(seed) {}

  const hash_value_t operator()(void *buf, size_t len, seed_value_t seed) const;
};

typedef xxh3_hash_t<uint64_t> xxh3_hash_64_t;
typedef xxh3_hash_t<uint128_t> xxh3_hash_128_t;

template <>
const xxh3_hash_64_t::hash_value_t xxh3_hash_64_t::operator()(void *buf, size_t len, xxh3_hash_64_t::seed_value_t seed) const
{
  return XXH3_64bits_withSeed(buf, len, seed);
}

template <>
const xxh3_hash_128_t::hash_value_t xxh3_hash_128_t::operator()(void *buf, size_t len, xxh3_hash_128_t::seed_value_t seed) const
{
  XXH128_hash_t hash = XXH3_128bits_withSeed(buf, len, seed);

  return U128_NEW(hash.low64, hash.high64);
}
