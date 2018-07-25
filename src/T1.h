#pragma once

#include "Hash.h"

#include "smhasher/t1ha.h"

template <typename T, bool LE>
class t1_hash_t : public Hasher<t1_hash_t<T, LE>, T>
{
  public:
    typedef Hasher<t1_hash_t<T, LE>, T> __hasher_t;
    typedef typename __hasher_t::hash_value_t hash_value_t;
    typedef typename __hasher_t::seed_value_t seed_value_t;

    t1_hash_t(seed_value_t seed = 0) : __hasher_t(seed) {}

    const hash_value_t operator()(void *buf, size_t len, seed_value_t seed) const override;
};

typedef t1_hash_t<uint32_t, true> t1_hash_32_t;
typedef t1_hash_t<uint32_t, false> t1_hash_32_be_t;
typedef t1_hash_t<uint64_t, true> t1_hash_64_t;
typedef t1_hash_t<uint64_t, false> t1_hash_64_be_t;

template <>
inline const t1_hash_32_t::hash_value_t t1_hash_32_t::operator()(void *buf, size_t len, t1_hash_32_t::seed_value_t seed) const
{
#if defined(__SSE4_2__) && defined(__x86_64__)
    return t1ha_ia32crc(buf, len, seed);
#else
    return t1ha_32le(buf, len, seed);
#endif
}

template <>
inline const t1_hash_32_be_t::hash_value_t t1_hash_32_be_t::operator()(void *buf, size_t len, t1_hash_32_be_t::seed_value_t seed) const
{
    return t1ha_32be(buf, len, seed);
}

template <>
inline const t1_hash_64_t::hash_value_t t1_hash_64_t::operator()(void *buf, size_t len, t1_hash_64_t::seed_value_t seed) const
{
    return t1ha_64le(buf, len, seed);
}

template <>
inline const t1_hash_64_be_t::hash_value_t t1_hash_64_be_t::operator()(void *buf, size_t len, t1_hash_64_be_t::seed_value_t seed) const
{
    return t1ha_64be(buf, len, seed);
}
