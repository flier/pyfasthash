#pragma once

#include "Hash.h"

#include "smhasher/farmhash-c.h"

/**

    FarmHash, a family of hash functions.

    https://github.com/google/farmhash

 **/

template <typename T>
class farm_hash_t : public Hasher<farm_hash_t<T>, T>
{
  public:
    typedef Hasher<farm_hash_t<T>, T> __hasher_t;
    typedef typename __hasher_t::hash_value_t hash_value_t;
    typedef typename __hasher_t::seed_value_t seed_value_t;

    farm_hash_t(seed_value_t seed = 0) : __hasher_t(seed) {}

    const hash_value_t operator()(void *buf, size_t len, seed_value_t seed) const;
};

typedef farm_hash_t<uint32_t> farm_hash_32_t;
typedef farm_hash_t<uint64_t> farm_hash_64_t;
#ifdef SUPPORT_INT128
typedef farm_hash_t<uint128_t> farm_hash_128_t;
#endif

template <>
const farm_hash_32_t::hash_value_t farm_hash_32_t::operator()(void *buf, size_t len, farm_hash_32_t::seed_value_t seed) const
{
    if (seed)
    {
        return farmhash32_with_seed((const char *)buf, len, seed);
    }
    else
    {
        return farmhash32((const char *)buf, len);
    }
}

template <>
const farm_hash_64_t::hash_value_t farm_hash_64_t::operator()(void *buf, size_t len, farm_hash_64_t::seed_value_t seed) const
{
    if (seed)
    {
        return farmhash64_with_seed((const char *)buf, len, seed);
    }
    else
    {
        return farmhash64((const char *)buf, len);
    }
}

#ifdef SUPPORT_INT128
template <>
const farm_hash_128_t::hash_value_t farm_hash_128_t::operator()(void *buf, size_t len, farm_hash_128_t::seed_value_t seed) const
{
    uint128_c_t hash;

    if (seed)
    {
        hash = farmhash128_with_seed((const char *)buf, len, make_uint128_c_t(U128_LO(seed), U128_HI(seed)));
    }
    else
    {
        hash = farmhash128((const char *)buf, len);
    }

    return U128_NEW(uint128_c_t_low64(hash), uint128_c_t_high64(hash));
}
#endif

template <typename T>
class farm_fingerprint_t : public Fingerprinter<farm_fingerprint_t<T>, T>
{
  public:
    typedef Fingerprinter<farm_fingerprint_t<T>, T> __fingerprinter_t;
    typedef typename __fingerprinter_t::fingerprint_t fingerprint_t;

    farm_fingerprint_t() = default;

    const fingerprint_t operator()(void *buf, size_t len) const;
};

typedef farm_fingerprint_t<uint32_t> farm_fingerprint_32_t;
typedef farm_fingerprint_t<uint64_t> farm_fingerprint_64_t;
#ifdef SUPPORT_INT128
typedef farm_fingerprint_t<uint128_t> farm_fingerprint_128_t;
#endif

template <>
const farm_fingerprint_32_t::fingerprint_t farm_fingerprint_32_t::operator()(void *buf, size_t len) const
{
    return farmhash_fingerprint32((const char *)buf, len);
}

template <>
const farm_fingerprint_64_t::fingerprint_t farm_fingerprint_64_t::operator()(void *buf, size_t len) const
{
    return farmhash_fingerprint64((const char *)buf, len);
}

#ifdef SUPPORT_INT128
template <>
const farm_fingerprint_128_t::fingerprint_t farm_fingerprint_128_t::operator()(void *buf, size_t len) const
{
    uint128_c_t fingerprint = farmhash_fingerprint128((const char *)buf, len);

    return U128_NEW(uint128_c_t_low64(fingerprint), uint128_c_t_high64(fingerprint));
}
#endif
