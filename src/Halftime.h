#pragma once

#include <algorithm>
#include <array>
#include <random>

#include "Hash.h"

#include "halftime/halftime-hash.hpp"

typedef std::array<uint64_t, halftime_hash::kEntropyBytesNeeded / sizeof(uint64_t)> halftime_seed_t;

template <>
halftime_seed_t as_seed_value(uint64_t hash)
{
    halftime_seed_t seed;
    std::generate(seed.begin(), seed.end(), std::mt19937_64(hash));
    return seed;
}

template <>
uint64_t as_hash_value(halftime_seed_t seed)
{
    return seed[0];
}

template <>
halftime_seed_t as_seed_value(uint128_t hash)
{
    std::seed_seq seeds{U128_LO(hash), U128_HI(hash)};
    std::mt19937_64 gen(seeds);

    halftime_seed_t seed;
    std::generate(seed.begin(), seed.end(), gen);
    return seed;
}

template <>
halftime_seed_t as_seed_value(uint256_t hash)
{
    std::seed_seq seeds(hash.begin(), hash.end());
    std::mt19937_64 gen(seeds);

    halftime_seed_t seed;
    std::generate(seed.begin(), seed.end(), gen);
    return seed;
}

template <>
halftime_seed_t as_seed_value(uint512_t hash)
{
    std::seed_seq seeds(hash.begin(), hash.end());
    std::mt19937_64 gen(seeds);

    halftime_seed_t seed;
    std::generate(seed.begin(), seed.end(), gen);
    return seed;
}

template <>
uint128_t as_hash_value(halftime_seed_t seed)
{
    return U128_NEW(seed[0], seed[1]);
}

template <>
uint256_t as_hash_value(halftime_seed_t seed)
{
    return {seed[0], seed[1], seed[2], seed[3]};
}

template <>
uint512_t as_hash_value(halftime_seed_t seed)
{
    return {seed[0], seed[1], seed[2], seed[3], seed[4], seed[5], seed[6], seed[7]};
}

template <typename T>
class halftime_hash_t : public Hasher<halftime_hash_t<T>, halftime_seed_t, uint64_t>
{
public:
    typedef Hasher<halftime_hash_t<T>, halftime_seed_t, uint64_t> __hasher_t;
    typedef typename __hasher_t::hash_value_t hash_value_t;
    typedef typename __hasher_t::seed_value_t seed_value_t;

    halftime_hash_t(uint64_t seed = {}) : __hasher_t(as_seed_value<halftime_seed_t>(seed))
    {
    }

    const hash_value_t operator()(void *buf, size_t len, seed_value_t seed) const;

    static py::class_<halftime_hash_t<T> > Export(const py::module &m, const char *name)
    {
        return py::class_<halftime_hash_t<T> >(m, name)
            .def(py::init<uint64_t>(), py::arg("seed") = 0)
            .def_readwrite("seed", &halftime_hash_t::_seed)
            .def("__call__", &halftime_hash_t::CallWithArgs);
    }
};

typedef halftime_hash_t<uint64_t> halftime_hash_64_t;
typedef halftime_hash_t<uint128_t> halftime_hash_128_t;
typedef halftime_hash_t<uint256_t> halftime_hash_256_t;
typedef halftime_hash_t<uint512_t> halftime_hash_512_t;

template <>
const halftime_hash_64_t::hash_value_t halftime_hash_64_t::operator()(void *buf, size_t len, halftime_hash_64_t::seed_value_t seed) const
{
    return halftime_hash::HalftimeHashStyle64(seed.data(), (const char *)buf, len);
}

template <>
const halftime_hash_128_t::hash_value_t halftime_hash_128_t::operator()(void *buf, size_t len, halftime_hash_128_t::seed_value_t seed) const
{
    return halftime_hash::HalftimeHashStyle128(seed.data(), (const char *)buf, len);
}

template <>
const halftime_hash_256_t::hash_value_t halftime_hash_256_t::operator()(void *buf, size_t len, halftime_hash_256_t::seed_value_t seed) const
{
    return halftime_hash::HalftimeHashStyle256(seed.data(), (const char *)buf, len);
}

template <>
const halftime_hash_512_t::hash_value_t halftime_hash_512_t::operator()(void *buf, size_t len, halftime_hash_512_t::seed_value_t seed) const
{
    return halftime_hash::HalftimeHashStyle512(seed.data(), (const char *)buf, len);
}
