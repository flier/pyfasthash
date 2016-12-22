#pragma once

#include "Hash.h"

#include "smhasher/farmhash-c.h"

/**

    FarmHash, a family of hash functions.

    https://github.com/google/farmhash

 **/

template <typename T>
class farm_hash_t : public Hasher< farm_hash_t<T> >
{
public:
  farm_hash_t() {}

  typedef T hash_value_t;

  const hash_value_t operator()(void *buf, size_t len, hash_value_t seed) const;
};

typedef farm_hash_t<uint32_t> farm_hash_32_t;
typedef farm_hash_t<uint64_t> farm_hash_64_t;
typedef farm_hash_t<uint128_t> farm_hash_128_t;

template<>
const uint32_t farm_hash_t<uint32_t>::operator()(void *buf, size_t len, uint32_t seed) const
{
    if (seed) {
        return farmhash32_with_seed((const char *) buf, len, seed);
    } else {
        return farmhash32((const char *) buf, len);
    }
}

template<>
const uint64_t farm_hash_t<uint64_t>::operator()(void *buf, size_t len, uint64_t seed) const
{
    if (seed) {
        return farmhash64_with_seed((const char *) buf, len, seed);
    } else {
        return farmhash64((const char *) buf, len);
    }
}

template<>
const uint128_t farm_hash_t<uint128_t>::operator()(void *buf, size_t len, uint128_t seed) const
{
    uint128_c_t hash;

    if (seed) {
        hash = farmhash128_with_seed((const char *) buf, len, make_uint128_c_t(U128_LO(seed), U128_HI(seed)));
    } else {
        hash = farmhash128((const char *) buf, len);
    }

    return U128_NEW(uint128_c_t_low64(hash), uint128_c_t_high64(hash));
}
