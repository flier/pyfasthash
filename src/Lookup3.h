#pragma once

#include "Hash.h"

/**
 * http://burtleburtle.net/bob/hash/doobs.html
 */
extern "C"
{

  uint32_t hashword(const uint32_t *k, /* the key, an array of uint32_t values */
                    size_t length,     /* the length of the key, in uint32_ts */
                    uint32_t initval);

  void hashword2(const uint32_t *k, /* the key, an array of uint32_t values */
                 size_t length,     /* the length of the key, in uint32_ts */
                 uint32_t *pc,      /* IN: seed OUT: primary hash value */
                 uint32_t *pb);     /* IN: more seed OUT: secondary hash value */

  uint32_t hashlittle(const void *key, size_t length, uint32_t initval);

  void hashlittle2(const void *key, /* the key to hash */
                   size_t length,   /* length of the key */
                   uint32_t *pc,    /* IN: primary initval, OUT: primary hash */
                   uint32_t *pb);   /* IN: secondary initval, OUT: secondary hash */

  uint32_t hashbig(const void *key, size_t length, uint32_t initval);
}

template <bool ORDER>
class lookup3_t : public Hasher<lookup3_t<ORDER>, uint32_t>
{
public:
  typedef Hasher<lookup3_t<ORDER>, uint32_t> __hasher_t;
  typedef typename __hasher_t::hash_value_t hash_value_t;
  typedef typename __hasher_t::seed_value_t seed_value_t;

  lookup3_t(seed_value_t seed = 0) : __hasher_t(seed) {}

  const hash_value_t operator()(void *buf, size_t len, seed_value_t seed) const;
};

typedef lookup3_t<true> lookup3_little_t;
typedef lookup3_t<false> lookup3_big_t;

template <>
const lookup3_little_t::hash_value_t lookup3_little_t::operator()(void *buf, size_t len, lookup3_little_t::seed_value_t seed) const
{
  return hashlittle(buf, len, seed);
}

template <>
const lookup3_big_t::hash_value_t lookup3_big_t::operator()(void *buf, size_t len, lookup3_big_t::seed_value_t seed) const
{
  return hashbig(buf, len, seed);
}
