#pragma once

#include "Hash.h"

#include "smhasher/xxhash.h"

template <typename T>
class xx_hash_t : public Hasher< xx_hash_t<T> >
{
public:
  xx_hash_t() {}

  typedef T hash_value_t;

  const hash_value_t operator()(void *buf, size_t len, hash_value_t seed) const;
};

typedef xx_hash_t<uint32_t> xx_hash_32_t;
typedef xx_hash_t<uint64_t> xx_hash_64_t;

template<>
const uint32_t xx_hash_t<uint32_t>::operator()(void *buf, size_t len, uint32_t seed) const
{
	return XXH32(buf, len, seed);
}
template<>
const uint64_t xx_hash_t<uint64_t>::operator()(void *buf, size_t len, uint64_t seed) const
{
	return XXH64(buf, len, seed);
}