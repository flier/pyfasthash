#pragma once

#include "Hash.h"

#include "smhasher/MurmurHash1.h"
#include "smhasher/MurmurHash2.h"
#include "smhasher/MurmurHash3.h"

/**
 * http://code.google.com/p/smhasher/
 */

enum murmur_hash_t
{
  murmur_hash1,
  murmur_hash1_aligned,
  murmur_hash2,
  murmur_hash2a,
  murmur_hash2_aligned,
  murmur_hash2_neutral,
  murmur_hash2_x64_64a,
  murmur_hash2_x86_64b,
  murmur_hash3_32,
  murmur_hash3_x86_128,
  murmur_hash3_x64_128
};

template <typename T, typename S, murmur_hash_t TYPE>
class murmur_t : public Hasher<murmur_t<T, S, TYPE>, S, T>
{
public:
  typedef Hasher<murmur_t<T, S, TYPE>, S, T> __hasher_t;
  typedef typename __hasher_t::hash_value_t hash_value_t;
  typedef typename __hasher_t::seed_value_t seed_value_t;

  murmur_t(seed_value_t seed = 0) : __hasher_t(seed) {}

  const hash_value_t operator()(void *buf, size_t len, seed_value_t seed) const;
};

typedef murmur_t<uint32_t, uint32_t, murmur_hash1> murmur1_32_t;
typedef murmur_t<uint32_t, uint32_t, murmur_hash1_aligned> murmur1_aligned_32_t;
typedef murmur_t<uint32_t, uint32_t, murmur_hash2> murmur2_32_t;
typedef murmur_t<uint32_t, uint32_t, murmur_hash2a> murmur2a_32_t;
typedef murmur_t<uint32_t, uint32_t, murmur_hash2_aligned> murmur2_aligned_32_t;
typedef murmur_t<uint32_t, uint32_t, murmur_hash2_neutral> murmur2_neutral_32_t;
typedef murmur_t<uint64_t, uint64_t, murmur_hash2_x64_64a> murmur2_x64_64a_t;
typedef murmur_t<uint64_t, uint64_t, murmur_hash2_x86_64b> murmur2_x86_64b_t;
typedef murmur_t<uint32_t, uint32_t, murmur_hash3_32> murmur3_32_t;

#ifdef SUPPORT_INT128
typedef murmur_t<uint128_t, uint32_t, murmur_hash3_x86_128> murmur3_x86_128_t;
typedef murmur_t<uint128_t, uint32_t, murmur_hash3_x64_128> murmur3_x64_128_t;
#endif

template <>
const murmur1_32_t::hash_value_t murmur1_32_t::operator()(void *buf, size_t len, murmur1_32_t::seed_value_t seed) const
{
  return MurmurHash1(buf, (int)len, seed);
}

template <>
const murmur1_aligned_32_t::hash_value_t murmur1_aligned_32_t::operator()(void *buf, size_t len, murmur1_aligned_32_t::seed_value_t seed) const
{
  return MurmurHash1Aligned(buf, (int)len, seed);
}

template <>
const murmur2_32_t::hash_value_t murmur2_32_t::operator()(void *buf, size_t len, murmur2_32_t::seed_value_t seed) const
{
  return MurmurHash2(buf, (int)len, seed);
}

template <>
const murmur2a_32_t::hash_value_t murmur2a_32_t::operator()(void *buf, size_t len, murmur2a_32_t::seed_value_t seed) const
{
  return MurmurHash2A(buf, (int)len, seed);
}

template <>
const murmur2_aligned_32_t::hash_value_t murmur2_aligned_32_t::operator()(void *buf, size_t len, murmur2_aligned_32_t::seed_value_t seed) const
{
  return MurmurHashAligned2(buf, (int)len, seed);
}

template <>
const murmur2_neutral_32_t::hash_value_t murmur2_neutral_32_t::operator()(void *buf, size_t len, murmur2_neutral_32_t::seed_value_t seed) const
{
  return MurmurHashNeutral2(buf, (int)len, seed);
}

template <>
const murmur2_x64_64a_t::hash_value_t murmur2_x64_64a_t::operator()(void *buf, size_t len, murmur2_x64_64a_t::seed_value_t seed) const
{
  return MurmurHash64A(buf, (int)len, seed);
}

template <>
const murmur2_x86_64b_t::hash_value_t murmur2_x86_64b_t::operator()(void *buf, size_t len, murmur2_x86_64b_t::seed_value_t seed) const
{
  return MurmurHash64B(buf, (int)len, seed);
}

template <>
const murmur3_32_t::hash_value_t murmur3_32_t::operator()(void *buf, size_t len, murmur3_32_t::seed_value_t seed) const
{
  unsigned int hash = 0;

  MurmurHash3_x86_32(buf, (int)len, seed, &hash);

  return hash;
}

#ifdef SUPPORT_INT128

template <>
const murmur3_x86_128_t::hash_value_t murmur3_x86_128_t::operator()(void *buf, size_t len, murmur3_x86_128_t::seed_value_t seed) const
{
  uint128_t hash = 0;

  MurmurHash3_x86_128(buf, (int)len, seed, &hash);

  return hash;
}

template <>
const murmur3_x64_128_t::hash_value_t murmur3_x64_128_t::operator()(void *buf, size_t len, murmur3_x64_128_t::seed_value_t seed) const
{
  uint128_t hash = 0;

  MurmurHash3_x64_128(buf, (int)len, seed, &hash);

  return hash;
}

#endif
