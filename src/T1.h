#pragma once

#include "Hash.h"

#include "smhasher/t1ha.h"

enum t1_hash_a
{
    t1ha2_atonce_a,
    t1ha2_atonce128_a,
    t1ha1_le_a,
    t1ha1_be_a,
    t1ha0_a,
    t1ha0_32le_a,
    t1ha0_32be_a,
    t1ha0_ia32aes_noavx_a,
    t1ha0_ia32aes_avx_a,
    t1ha0_ia32aes_avx2_a,
};

template <typename T, t1_hash_a A>
class t1_hash_t : public Hasher<t1_hash_t<T, A>, T>
{
  public:
    typedef Hasher<t1_hash_t<T, A>, T> __hasher_t;
    typedef typename __hasher_t::hash_value_t hash_value_t;
    typedef typename __hasher_t::seed_value_t seed_value_t;

    t1_hash_t(seed_value_t seed = 0) : __hasher_t(seed) {}

    const hash_value_t operator()(void *buf, size_t len, seed_value_t seed) const override;
};

typedef t1_hash_t<uint64_t, t1ha2_atonce_a> t1ha2_atonce_t;
#if defined(SUPPORT_INT128)
typedef t1_hash_t<uint128_t, t1ha2_atonce128_a> t1ha2_atonce128_t;
#endif
typedef t1_hash_t<uint64_t, t1ha1_le_a> t1ha1_le_t;
typedef t1_hash_t<uint64_t, t1ha1_be_a> t1ha1_be_t;
typedef t1_hash_t<uint64_t, t1ha0_a> t1ha0_t;
typedef t1_hash_t<uint64_t, t1ha0_32le_a> t1ha0_32le_t;
typedef t1_hash_t<uint64_t, t1ha0_32be_a> t1ha0_32be_t;
typedef t1_hash_t<uint64_t, t1ha0_ia32aes_noavx_a> t1ha0_ia32aes_noavx_t;
typedef t1_hash_t<uint64_t, t1ha0_ia32aes_avx_a> t1ha0_ia32aes_avx_t;
typedef t1_hash_t<uint64_t, t1ha0_ia32aes_avx2_a> t1ha0_ia32aes_avx2_t;

template <>
inline const t1ha2_atonce_t::hash_value_t t1ha2_atonce_t::operator()(void *buf, size_t len, t1ha2_atonce_t::seed_value_t seed) const
{
    return t1ha2_atonce(buf, len, seed);
}

#if defined(SUPPORT_INT128)
template <>
inline const t1ha2_atonce128_t::hash_value_t t1ha2_atonce128_t::operator()(void *buf, size_t len, t1ha2_atonce128_t::seed_value_t seed) const
{
    uint64_t hi = 0;
    uint64_t lo = t1ha2_atonce128(&hi, buf, len, seed);

    return U128_NEW(lo, hi);
}
#endif

template <>
inline const t1ha1_le_t::hash_value_t t1ha1_le_t::operator()(void *buf, size_t len, t1ha1_le_t::seed_value_t seed) const
{
    return t1ha1_le(buf, len, seed);
}

template <>
inline const t1ha1_be_t::hash_value_t t1ha1_be_t::operator()(void *buf, size_t len, t1ha1_be_t::seed_value_t seed) const
{
    return t1ha1_be(buf, len, seed);
}

template <>
inline const t1ha0_t::hash_value_t t1ha0_t::operator()(void *buf, size_t len, t1ha0_t::seed_value_t seed) const
{
    return t1ha0(buf, len, seed);
}

template <>
inline const t1ha0_32le_t::hash_value_t t1ha0_32le_t::operator()(void *buf, size_t len, t1ha0_32le_t::seed_value_t seed) const
{
    return t1ha0_32le(buf, len, seed);
}

template <>
inline const t1ha0_32be_t::hash_value_t t1ha0_32be_t::operator()(void *buf, size_t len, t1ha0_32be_t::seed_value_t seed) const
{
    return t1ha0_32be(buf, len, seed);
}

template <>
inline const t1ha0_ia32aes_noavx_t::hash_value_t t1ha0_ia32aes_noavx_t::operator()(void *buf, size_t len, t1ha0_ia32aes_noavx_t::seed_value_t seed) const
{
    return t1ha0_ia32aes_noavx(buf, len, seed);
}

template <>
inline const t1ha0_ia32aes_avx_t::hash_value_t t1ha0_ia32aes_avx_t::operator()(void *buf, size_t len, t1ha0_ia32aes_avx_t::seed_value_t seed) const
{
    return t1ha0_ia32aes_avx(buf, len, seed);
}

template <>
inline const t1ha0_ia32aes_avx2_t::hash_value_t t1ha0_ia32aes_avx2_t::operator()(void *buf, size_t len, t1ha0_ia32aes_avx2_t::seed_value_t seed) const
{
    return t1ha0_ia32aes_avx2(buf, len, seed);
}
