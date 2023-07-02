#pragma once

#include "Hash.h"

#include "smhasher/Spooky.h"

/**

	SpookyHash: a 128-bit noncryptographic hash

	http://burtleburtle.net/bob/hash/spooky.html

 **/

template <typename T>
class spooky_hash_v1_t : public Hasher<spooky_hash_v1_t<T>, T>
{
public:
	typedef Hasher<spooky_hash_v1_t<T>, T> __hasher_t;
	typedef typename __hasher_t::hash_value_t hash_value_t;
	typedef typename __hasher_t::seed_value_t seed_value_t;

	spooky_hash_v1_t(seed_value_t seed = 0) : __hasher_t(seed) {}

	const hash_value_t operator()(void *buf, size_t len, seed_value_t seed) const;
};

typedef spooky_hash_v1_t<uint32_t> spooky_hash_v1_32_t;
typedef spooky_hash_v1_t<uint64_t> spooky_hash_v1_64_t;

template <>
const spooky_hash_v1_32_t::hash_value_t spooky_hash_v1_32_t::operator()(void *buf, size_t len, spooky_hash_v1_32_t::seed_value_t seed) const
{
	return SpookyHashV1::Hash32(buf, len, seed);
}

template <>
const spooky_hash_v1_64_t::hash_value_t spooky_hash_v1_64_t::operator()(void *buf, size_t len, spooky_hash_v1_64_t::seed_value_t seed) const
{
	return SpookyHashV1::Hash64(buf, len, seed);
}

typedef spooky_hash_v1_t<uint128_t> spooky_hash_v1_128_t;

template <>
const spooky_hash_v1_128_t::hash_value_t spooky_hash_v1_128_t::operator()(void *buf, size_t len, spooky_hash_v1_128_t::seed_value_t seed) const
{
	uint64_t lo = U128_LO(seed), hi = U128_HI(seed);

	SpookyHashV1::Hash128(buf, len, &lo, &hi);

	return U128_NEW(lo, hi);
}

template <typename T>
class spooky_hash_v2_t : public Hasher<spooky_hash_v2_t<T>, T>
{
public:
	typedef Hasher<spooky_hash_v2_t<T>, T> __hasher_t;
	typedef typename __hasher_t::hash_value_t hash_value_t;
	typedef typename __hasher_t::seed_value_t seed_value_t;

	spooky_hash_v2_t(seed_value_t seed = 0) : __hasher_t(seed) {}

	const hash_value_t operator()(void *buf, size_t len, seed_value_t seed) const;
};

typedef spooky_hash_v2_t<uint32_t> spooky_hash_v2_32_t;
typedef spooky_hash_v2_t<uint64_t> spooky_hash_v2_64_t;

template <>
const spooky_hash_v2_32_t::hash_value_t spooky_hash_v2_32_t::operator()(void *buf, size_t len, spooky_hash_v2_32_t::seed_value_t seed) const
{
	return SpookyHashV1::Hash32(buf, len, seed);
}

template <>
const spooky_hash_v2_64_t::hash_value_t spooky_hash_v2_64_t::operator()(void *buf, size_t len, spooky_hash_v2_64_t::seed_value_t seed) const
{
	return SpookyHashV1::Hash64(buf, len, seed);
}

typedef spooky_hash_v2_t<uint128_t> spooky_hash_v2_128_t;

template <>
const spooky_hash_v2_128_t::hash_value_t spooky_hash_v2_128_t::operator()(void *buf, size_t len, spooky_hash_v2_128_t::seed_value_t seed) const
{
	uint64_t lo = U128_LO(seed), hi = U128_HI(seed);

	SpookyHashV1::Hash128(buf, len, &lo, &hi);

	return U128_NEW(lo, hi);
}
