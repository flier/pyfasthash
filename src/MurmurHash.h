#pragma once

#include "Hash.h"

/**
 * http://murmurhash.googlepages.com/
 */

typedef unsigned __int64 uint64_t;

// Note - This code makes a few assumptions about how your machine behaves -

// 1. We can read a 4-byte value from any address without crashing
// 2. sizeof(int) == 4

// And it has a few limitations -

// 1. It will not work incrementally.
// 2. It will not produce the same results on little-endian and big-endian
//    machines.
unsigned int MurmurHash2 ( const void * key, int len, unsigned int seed );

// This is a variant of MurmurHash2 modified to use the Merkle-Damgard
// construction. Bulk speed should be identical to Murmur2, small-key speed
// will be 10%-20% slower due to the added overhead at the end of the hash.

// This variant fixes a minor issue where null keys were more likely to
// collide with each other than expected, and also makes the algorithm
// more amenable to incremental implementations. All other caveats from
// MurmurHash2 still apply.
unsigned int MurmurHash2A ( const void * key, int len, unsigned int seed );

// Same algorithm as MurmurHash2, but only does aligned reads - should be safer
// on certain platforms. 

// Performance will be lower than MurmurHash2
unsigned int MurmurHashAligned2 ( const void * key, int len, unsigned int seed );

// Same as MurmurHash2, but endian- and alignment-neutral.
// Half the speed though, alas.
unsigned int MurmurHashNeutral2 ( const void * key, int len, unsigned int seed );

// The same caveats as 32-bit MurmurHash2 apply here - beware of alignment 
// and endian-ness issues if used across multiple platforms.
uint64_t MurmurHash64A ( const void * key, int len, unsigned int seed );

enum murmur_hash_type
{
  murmur_hash2,
  murmur_hash2a,
  murmur_hash2_aligned,
  murmur_hash2_neutral,
  murmur_hash2_64
};

template <typename T, murmur_hash_type TYPE>
class murmur_t : public Hasher< murmur_t<T, TYPE> >
{
public:
  murmur_t() {}

  typedef T hash_value_t;

  T operator()(void *buf, size_t len, unsigned int seed) const;
};

typedef murmur_t<unsigned int, murmur_hash2> murmur2_32_t;
typedef murmur_t<unsigned int, murmur_hash2a> murmur2a_32_t;
typedef murmur_t<unsigned int, murmur_hash2_aligned> murmur2_aligned_32_t;
typedef murmur_t<unsigned int, murmur_hash2_neutral> murmur2_neutral_32_t;
typedef murmur_t<uint64_t, murmur_hash2_64> murmur2_64_t;

template <>
inline unsigned int murmur_t<unsigned int, murmur_hash2>::operator()(void *buf, size_t len, unsigned int val) const
{
  return MurmurHash2(buf, len, val);
}

template <>
inline unsigned int murmur_t<unsigned int, murmur_hash2a>::operator()(void *buf, size_t len, unsigned int val) const
{
  return MurmurHash2A(buf, len, val);
}

template <>
inline unsigned int murmur_t<unsigned int, murmur_hash2_aligned>::operator()(void *buf, size_t len, unsigned int val) const
{
  return MurmurHashAligned2(buf, len, val);
}

template <>
inline unsigned int murmur_t<unsigned int, murmur_hash2_neutral>::operator()(void *buf, size_t len, unsigned int val) const
{
  return MurmurHashNeutral2(buf, len, val);
}

template <>
inline uint64_t murmur_t<uint64_t, murmur_hash2_64>::operator()(void *buf, size_t len, unsigned int val) const
{
  return MurmurHash64A(buf, len, val);
}