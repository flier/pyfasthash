#pragma once

#include "Hash.h"

#include "smhasher/City.h"

/**

The CityHash family of hash functions

https://code.google.com/p/cityhash/

**/

template <typename T>
class city_hash_t : public Hasher< city_hash_t<T> >
{
public:
  city_hash_t() {}

  typedef T hash_value_t;

  const hash_value_t operator()(void *buf, size_t len, hash_value_t seed) const;
};

typedef city_hash_t<uint64_t> city_hash_64_t;
typedef city_hash_t<uint128_t> city_hash_128_t;

template<>
const uint64_t city_hash_t<uint64_t>::operator()(void *buf, size_t len, uint64_t seed) const
{
	if (seed) {
		return CityHash64WithSeed((const char *) buf, len, seed);
	} else {
		return CityHash64((const char *) buf, len);
	}
}

template<>
const uint128_t city_hash_t<uint128_t>::operator()(void *buf, size_t len, uint128_t seed) const
{
	if (seed) {
		const uint128& hash = CityHash128WithSeed((const char *) buf, len, std::make_pair(U128_LO(seed), U128_HI(seed)));

		return *(uint128_t *)&hash;
	} else {
		const uint128& hash = CityHash128((const char *) buf, len);

		return *(uint128_t *)&hash;
	}
}
