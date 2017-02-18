#pragma once

#include "Hash.h"

#include "smhasher/mum.h"

template <typename T>
class mum_hash_t : public Hasher< mum_hash_t<T> >
{
public:
  mum_hash_t() {}

  typedef T hash_value_t;

  const hash_value_t operator()(void *buf, size_t len, hash_value_t seed) const;
};

typedef mum_hash_t<uint64_t> mum_hash_64_t;

template<>
const uint64_t mum_hash_t<uint64_t>::operator()(void *buf, size_t len, uint64_t seed) const
{
	return mum_hash(buf, len, seed);
}