#pragma once

#include "Hash.h"

#include "smhasher/metrohash.h"

/**

    MetroHash: Faster, Better Hash Functions

    https://github.com/jandrewrogers/MetroHash

 **/

template <typename T, int S>
class metro_hash_t : public Hasher<metro_hash_t<T, S>, uint32_t, T>
{
  public:
    typedef Hasher<metro_hash_t<T, S>, uint32_t, T> __hasher_t;
    typedef typename __hasher_t::hash_value_t hash_value_t;
    typedef typename __hasher_t::seed_value_t seed_value_t;

    metro_hash_t(seed_value_t seed = 0) : __hasher_t(seed) {}

    const hash_value_t operator()(void *buf, size_t len, seed_value_t seed) const;
};

typedef metro_hash_t<uint64_t, 1> metro_hash_64_1_t;
typedef metro_hash_t<uint64_t, 2> metro_hash_64_2_t;
#ifdef SUPPORT_INT128
typedef metro_hash_t<uint128_t, 1> metro_hash_128_1_t;
typedef metro_hash_t<uint128_t, 2> metro_hash_128_2_t;
#endif

template <>
const metro_hash_64_1_t::hash_value_t metro_hash_64_1_t::operator()(void *buf, size_t len, metro_hash_64_1_t::seed_value_t seed) const
{
    uint64_t hash;

    metrohash64_1((const uint8_t *)buf, len, seed, (uint8_t *)&hash);

    return hash;
}

template <>
const metro_hash_64_2_t::hash_value_t metro_hash_64_2_t::operator()(void *buf, size_t len, metro_hash_64_2_t::seed_value_t seed) const
{
    uint64_t hash;

    metrohash64_2((const uint8_t *)buf, len, seed, (uint8_t *)&hash);

    return hash;
}

#ifdef SUPPORT_INT128

template <>
const metro_hash_128_1_t::hash_value_t metro_hash_128_1_t::operator()(void *buf, size_t len, metro_hash_128_1_t::seed_value_t seed) const
{
    uint128_t hash;

    metrohash128_1((const uint8_t *)buf, len, seed, (uint8_t *)&hash);

    return hash;
}

template <>
const metro_hash_128_2_t::hash_value_t metro_hash_128_2_t::operator()(void *buf, size_t len, metro_hash_128_2_t::seed_value_t seed) const
{
    uint128_t hash;

    metrohash128_2((const uint8_t *)buf, len, seed, (uint8_t *)&hash);

    return hash;
}
#endif

template <typename T, int S>
class metro_hash_crc_t : public Hasher<metro_hash_crc_t<T, S>, uint32_t, T>
{
  public:
    typedef Hasher<metro_hash_crc_t<T, S>, uint32_t, T> __hasher_t;
    typedef typename __hasher_t::hash_value_t hash_value_t;
    typedef typename __hasher_t::seed_value_t seed_value_t;

    metro_hash_crc_t(seed_value_t seed = 0) : __hasher_t(seed) {}

    const hash_value_t operator()(void *buf, size_t len, seed_value_t seed) const;
};

typedef metro_hash_crc_t<uint64_t, 1> metro_hash_64_crc_1_t;
typedef metro_hash_crc_t<uint64_t, 2> metro_hash_64_crc_2_t;
#ifdef SUPPORT_INT128
typedef metro_hash_crc_t<uint128_t, 1> metro_hash_128_crc_1_t;
typedef metro_hash_crc_t<uint128_t, 2> metro_hash_128_crc_2_t;
#endif

template <>
const metro_hash_64_crc_1_t::hash_value_t metro_hash_64_crc_1_t::operator()(void *buf, size_t len, metro_hash_64_crc_1_t::seed_value_t seed) const
{
    uint64_t hash;

    metrohash64crc_1((const uint8_t *)buf, len, (uint32_t)seed, (uint8_t *)&hash);

    return hash;
}

template <>
const metro_hash_64_crc_2_t::hash_value_t metro_hash_64_crc_2_t::operator()(void *buf, size_t len, metro_hash_64_crc_2_t::seed_value_t seed) const
{
    uint64_t hash;

    metrohash64crc_2((const uint8_t *)buf, len, (uint32_t)seed, (uint8_t *)&hash);

    return hash;
}

#ifdef SUPPORT_INT128

template <>
const metro_hash_128_crc_1_t::hash_value_t metro_hash_128_crc_1_t::operator()(void *buf, size_t len, metro_hash_128_crc_1_t::seed_value_t seed) const
{
    uint128_t hash;

    metrohash128crc_1((const uint8_t *)buf, len, seed, (uint8_t *)&hash);

    return hash;
}

template <>
const metro_hash_128_crc_2_t::hash_value_t metro_hash_128_crc_2_t::operator()(void *buf, size_t len, metro_hash_128_crc_2_t::seed_value_t seed) const
{
    uint128_t hash;

    metrohash128crc_2((const uint8_t *)buf, len, seed, (uint8_t *)&hash);

    return hash;
}

#endif
