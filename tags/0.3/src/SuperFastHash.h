#pragma once

#include "Hash.h"

/**
 * http://www.azillionmonkeys.com/qed/hash.html
 */

extern "C" uint32_t SuperFastHash (const char * data, int len, uint32_t hash);

class super_fast_hash_t : public Hasher< super_fast_hash_t >
{
public:
  super_fast_hash_t() {}

  typedef uint32_t hash_value_t;

  inline hash_value_t operator()(void *buf, size_t len, hash_value_t val) const
  {
    return SuperFastHash((const char *) buf, len, val);
  }
};
