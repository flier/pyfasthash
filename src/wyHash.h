#pragma once

#include "Hash.h"

#include "wyhash/wyhash.h"
#include "wyhash/wyhash32.h"

template <typename T>
class wy_hash_t : public Hasher<wy_hash_t<T>, T>
{
public:
  typedef Hasher<wy_hash_t<T>, T> __hasher_t;
  typedef typename __hasher_t::hash_value_t hash_value_t;
  typedef typename __hasher_t::seed_value_t seed_value_t;

  wy_hash_t(seed_value_t seed = 0) : __hasher_t(seed) {}

  const hash_value_t operator()(void *buf, size_t len, seed_value_t seed) const;
};

typedef wy_hash_t<uint32_t> wy_hash_32_t;
typedef wy_hash_t<uint64_t> wy_hash_64_t;

template <>
const wy_hash_32_t::hash_value_t wy_hash_32_t::operator()(void *buf, size_t len, wy_hash_32_t::seed_value_t seed) const
{
  return wyhash32(buf, len, seed);
}
template <>
const wy_hash_64_t::hash_value_t wy_hash_64_t::operator()(void *buf, size_t len, wy_hash_64_t::seed_value_t seed) const
{
  return wyhash(buf, len, seed, _wyp);
}
