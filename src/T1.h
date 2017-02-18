#pragma once

#include "Hash.h"

#include "smhasher/t1ha.h"

template <typename T, bool LE>
class t1_hash_t : public Hasher< t1_hash_t<T, LE> >
{
public:
  t1_hash_t() {}

  typedef T hash_value_t;

  const hash_value_t operator()(void *buf, size_t len, hash_value_t seed) const;
};

typedef t1_hash_t<uint32_t, true> t1_hash_32_t;
typedef t1_hash_t<uint32_t, false> t1_hash_32_be_t;
typedef t1_hash_t<uint64_t, true> t1_hash_64_t;
typedef t1_hash_t<uint64_t, true> t1_hash_64_be_t;

template<>
const uint32_t t1_hash_t<uint32_t, true>::operator()(void *buf, size_t len, uint32_t seed) const
{
#if defined(__SSE4_2__) && defined(__x86_64__)
    return t1ha_ia32crc(buf, len, seed);
#else
    return t1ha_32le(buf, len, seed);
#endif
}

template<>
const uint32_t t1_hash_t<uint32_t, false>::operator()(void *buf, size_t len, uint32_t seed) const
{
    return t1ha_32be(buf, len, seed);
}

template<>
const uint64_t t1_hash_t<uint64_t, true>::operator()(void *buf, size_t len, uint64_t seed) const
{
    return t1ha_64le(buf, len, seed);
}

template<>
const uint64_t t1_hash_t<uint64_t, false>::operator()(void *buf, size_t len, uint64_t seed) const
{
    return t1ha_64be(buf, len, seed);
}