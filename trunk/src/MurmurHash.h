#pragma once

#include "Hash.h"

#include "MurmurHash/MurmurHash1.h"
#include "MurmurHash/MurmurHash2.h"
#include "MurmurHash/MurmurHash3.h"

/**
 * http://code.google.com/p/smhasher/
 */

enum murmur_hash_type
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

template <typename T, typename S, murmur_hash_type TYPE>
class murmur_t : public Hasher< murmur_t<T, S, TYPE> >
{
public:
  murmur_t() {}

  typedef T hash_value_t;
  typedef S hash_seed_t;

  const hash_value_t operator()(void *buf, size_t len, hash_seed_t seed) const;
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
typedef murmur_t<uint128_t, uint32_t, murmur_hash3_x86_128> murmur3_x86_128_t;
typedef murmur_t<uint128_t, uint32_t, murmur_hash3_x64_128> murmur3_x64_128_t;

template <>
inline const uint32_t murmur_t<uint32_t, uint32_t, murmur_hash1>::operator()(void *buf, size_t len, unsigned int val) const
{
  return MurmurHash1(buf, len, val);
}

template <>
inline const uint32_t murmur_t<uint32_t, uint32_t, murmur_hash1_aligned>::operator()(void *buf, size_t len, unsigned int val) const
{
  return MurmurHash1Aligned(buf, len, val);
}

template <>
inline const uint32_t murmur_t<uint32_t, uint32_t, murmur_hash2>::operator()(void *buf, size_t len, unsigned int val) const
{
  return MurmurHash2(buf, len, val);
}

template <>
inline const uint32_t murmur_t<uint32_t, uint32_t, murmur_hash2a>::operator()(void *buf, size_t len, unsigned int val) const
{
  return MurmurHash2A(buf, len, val);
}

template <>
inline const uint32_t murmur_t<uint32_t, uint32_t, murmur_hash2_aligned>::operator()(void *buf, size_t len, unsigned int val) const
{
  return MurmurHashAligned2(buf, len, val);
}

template <>
inline const uint32_t murmur_t<uint32_t, uint32_t, murmur_hash2_neutral>::operator()(void *buf, size_t len, unsigned int val) const
{
  return MurmurHashNeutral2(buf, len, val);
}

template <>
inline const uint64_t murmur_t<uint64_t, uint64_t, murmur_hash2_x64_64a>::operator()(void *buf, size_t len, uint64_t val) const
{
  return MurmurHash64A(buf, len, val);
}

template <>
inline const uint64_t murmur_t<uint64_t, uint64_t, murmur_hash2_x86_64b>::operator()(void *buf, size_t len, uint64_t val) const
{
  return MurmurHash64B(buf, len, val);
}

template <>
inline const uint32_t murmur_t<uint32_t, uint32_t, murmur_hash3_32>::operator()(void *buf, size_t len, unsigned int val) const
{
  unsigned int hash;

  MurmurHash3_x86_32(buf, len, val, &hash);

  return hash;
}

template <>
inline const uint128_t murmur_t<uint128_t, uint32_t, murmur_hash3_x86_128>::operator()(void *buf, size_t len, unsigned int val) const
{
  uint128_t hash;

  MurmurHash3_x86_128(buf, len, val, &hash);

  return hash;
}

template <>
inline const uint128_t murmur_t<uint128_t, uint32_t, murmur_hash3_x64_128>::operator()(void *buf, size_t len, unsigned int val) const
{
  uint128_t hash;

  MurmurHash3_x64_128(buf, len, val, &hash);

  return hash;
}
