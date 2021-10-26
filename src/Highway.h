#pragma once

#include "Hash.h"

#include "highwayhash/highwayhash/highwayhash_target.h"
#include "highwayhash/highwayhash/instruction_sets.h"

#ifdef SUPPORT_INT128

template <typename T>
class hightway_hash_t : public Hasher<hightway_hash_t<T>, uint256_t, T>
{
public:
    typedef Hasher<hightway_hash_t<T>, uint256_t, T> __hasher_t;
    typedef typename __hasher_t::hash_value_t hash_value_t;
    typedef typename __hasher_t::seed_value_t seed_value_t;

    hightway_hash_t(seed_value_t seed = 0) : __hasher_t(seed) {}

    const hash_value_t operator()(void *buf, size_t len, seed_value_t seed) const;
};

typedef hightway_hash_t<uint64_t> highway_hash_64_t;

template <>
const highway_hash_64_t::hash_value_t highway_hash_64_t::operator()(void *buf, size_t len, highway_hash_64_t::seed_value_t seed) const
{
    highwayhash::HHResult64 result;
    highwayhash::InstructionSets::Run<highwayhash::HighwayHash>(
        *reinterpret_cast<const highwayhash::HHKey *>(&seed),
        reinterpret_cast<const char *>(buf), len, &result);
    return result;
}

typedef hightway_hash_t<uint128_t> highway_hash_128_t;

template <>
const highway_hash_128_t::hash_value_t highway_hash_128_t::operator()(void *buf, size_t len, highway_hash_128_t::seed_value_t seed) const
{
    highwayhash::HHResult128 result;
    highwayhash::InstructionSets::Run<highwayhash::HighwayHash>(
        *reinterpret_cast<const highwayhash::HHKey *>(&seed),
        reinterpret_cast<const char *>(buf), len, &result);
    return U128_NEW(result[0], result[1]);
}

typedef hightway_hash_t<uint256_t> highway_hash_256_t;

template <>
const highway_hash_256_t::hash_value_t highway_hash_256_t::operator()(void *buf, size_t len, highway_hash_256_t::seed_value_t seed) const
{
    highwayhash::HHResult256 result;
    highwayhash::InstructionSets::Run<highwayhash::HighwayHash>(
        *reinterpret_cast<const highwayhash::HHKey *>(&seed),
        reinterpret_cast<const char *>(buf), len, &result);

    uint256_t hash;
    std::move(std::begin(result), std::end(result), hash.begin());
    return hash;
}

#endif
