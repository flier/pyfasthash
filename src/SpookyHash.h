#pragma once

#include "Hash.h"

#include "smhasher/Spooky.h"

/**

	SpookyHash: a 128-bit noncryptographic hash

	http://burtleburtle.net/bob/hash/spooky.html

 **/

template <typename T>
class spooky_hash_t : public Hasher< spooky_hash_t<T> >
{
public:
  spooky_hash_t() {}

  typedef T hash_value_t;

  const hash_value_t operator()(void *buf, size_t len, hash_value_t seed) const;
};

typedef spooky_hash_t<uint32_t> spooky_hash_32_t;
typedef spooky_hash_t<uint64_t> spooky_hash_64_t;

template<>
const uint32_t spooky_hash_t<uint32_t>::operator()(void *buf, size_t len, uint32_t seed) const
{
	return SpookyHash::Hash32(buf, len, seed);
}

template<>
const uint64_t spooky_hash_t<uint64_t>::operator()(void *buf, size_t len, uint64_t seed) const
{
	return SpookyHash::Hash64(buf, len, seed);
}

#ifdef BOOST_HAS_INT128

typedef spooky_hash_t<uint128_t> spooky_hash_128_t;

template<>
const uint128_t spooky_hash_t<uint128_t>::operator()(void *buf, size_t len, uint128_t seed) const
{
	uint64_t lo = U128_LO(seed), hi = U128_HI(seed);

	SpookyHash::Hash128(buf, len, &lo, &hi);

	U128_NEW(value, lo, hi);

	return value;
}

#endif