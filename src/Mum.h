#pragma once

#include "Hash.h"

#include "smhasher/mum.h"

template <typename T>
class mum_hash_t : public Hasher<mum_hash_t<T>, T>
{
public:
  typedef Hasher<mum_hash_t<T>, T> __hasher_t;
  typedef typename __hasher_t::hash_value_t hash_value_t;
  typedef typename __hasher_t::seed_value_t seed_value_t;

  mum_hash_t(seed_value_t seed = 0) : __hasher_t(seed) {}

  const hash_value_t operator()(void *buf, size_t len, seed_value_t seed) const;
};

typedef mum_hash_t<uint64_t> mum_hash_64_t;

template <>
const mum_hash_64_t::hash_value_t mum_hash_64_t::operator()(void *buf, size_t len, mum_hash_64_t::seed_value_t seed) const
{
  return mum_hash(buf, len, seed);
}
