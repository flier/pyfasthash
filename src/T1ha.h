#pragma once

#include "Hash.h"

#include "t1ha/t1ha.h"

enum t1_hash_a
{
    t1ha2_atonce_a,
    t1ha2_atonce128_a,
    t1ha1_le_a,
    t1ha1_be_a,
    t1ha0_a,
};

template <typename T, t1_hash_a A>
class t1_hash_t : public Hasher<t1_hash_t<T, A>, uint64_t, T>
{
  public:
    typedef Hasher<t1_hash_t<T, A>, uint64_t, T> __hasher_t;
    typedef typename __hasher_t::hash_value_t hash_value_t;
    typedef typename __hasher_t::seed_value_t seed_value_t;

    t1_hash_t(seed_value_t seed = 0) : __hasher_t(seed) {}

    const hash_value_t operator()(void *buf, size_t len, seed_value_t seed) const;
};

typedef t1_hash_t<uint64_t, t1ha2_atonce_a> t1ha2_atonce_t;
#if defined(SUPPORT_INT128)
typedef t1_hash_t<uint128_t, t1ha2_atonce128_a> t1ha2_atonce128_t;
#endif
typedef t1_hash_t<uint64_t, t1ha1_le_a> t1ha1_le_t;
typedef t1_hash_t<uint64_t, t1ha1_be_a> t1ha1_be_t;
typedef t1_hash_t<uint64_t, t1ha0_a> t1ha0_t;

template <>
const t1ha2_atonce_t::hash_value_t t1ha2_atonce_t::operator()(void *buf, size_t len, t1ha2_atonce_t::seed_value_t seed) const
{
    return t1ha2_atonce(buf, len, seed);
}

#if defined(SUPPORT_INT128)
template <>
const t1ha2_atonce128_t::hash_value_t t1ha2_atonce128_t::operator()(void *buf, size_t len, t1ha2_atonce128_t::seed_value_t seed) const
{
    uint64_t hi = 0;
    uint64_t lo = t1ha2_atonce128(&hi, buf, len, seed);

    return U128_NEW(lo, hi);
}
#endif

template <>
const t1ha1_le_t::hash_value_t t1ha1_le_t::operator()(void *buf, size_t len, t1ha1_le_t::seed_value_t seed) const
{
    return t1ha1_le(buf, len, seed);
}

template <>
const t1ha1_be_t::hash_value_t t1ha1_be_t::operator()(void *buf, size_t len, t1ha1_be_t::seed_value_t seed) const
{
    return t1ha1_be(buf, len, seed);
}

template <>
const t1ha0_t::hash_value_t t1ha0_t::operator()(void *buf, size_t len, t1ha0_t::seed_value_t seed) const
{
    static auto t1ha0_funcptr = t1ha0_resolve();

    return t1ha0_funcptr(buf, len, seed);
}
