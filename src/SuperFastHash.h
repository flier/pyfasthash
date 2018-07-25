#pragma once

#include "Hash.h"

/**
 * http://www.azillionmonkeys.com/qed/hash.html
 */

extern "C" uint32_t SuperFastHash(const char *data, int len, uint32_t hash);

class super_fast_hash_t : public Hasher<super_fast_hash_t, uint32_t>
{
public:
  typedef Hasher<super_fast_hash_t, uint32_t> __hasher_t;
  typedef typename __hasher_t::hash_value_t hash_value_t;
  typedef typename __hasher_t::seed_value_t seed_value_t;

  super_fast_hash_t(seed_value_t seed = 0) : __hasher_t(seed) {}

  const hash_value_t operator()(void *buf, size_t len, seed_value_t seed) const
  {
    return SuperFastHash((const char *)buf, (int)len, seed);
  }
};
