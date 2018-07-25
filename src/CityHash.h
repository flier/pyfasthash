#pragma once

#include "Hash.h"

#include "smhasher/City.h"

/**

The CityHash family of hash functions

https://code.google.com/p/cityhash/

**/

template <typename T>
struct city_hash_t : public Hasher<city_hash_t<T>, T>
{
#if defined(__SSE4_2__) && defined(__x86_64__)
	static bool has_sse4_2;
#endif

  public:
	typedef Hasher<city_hash_t<T>, T> __hasher_t;
	typedef typename __hasher_t::hash_value_t hash_value_t;
	typedef typename __hasher_t::seed_value_t seed_value_t;

	city_hash_t(seed_value_t seed = 0) : __hasher_t(seed) {}

	const hash_value_t operator()(void *buf, size_t len, seed_value_t seed) const override;
};

#if defined(__SSE4_2__) && defined(__x86_64__)

template <typename T>
bool city_hash_t<T>::has_sse4_2 = false;

#endif

typedef city_hash_t<uint32_t> city_hash_32_t;
typedef city_hash_t<uint64_t> city_hash_64_t;
#ifdef SUPPORT_INT128
typedef city_hash_t<uint128_t> city_hash_128_t;
#endif

template <>
const city_hash_32_t::hash_value_t city_hash_32_t::operator()(void *buf, size_t len, city_hash_32_t::seed_value_t seed) const
{
	return CityHash32WithSeed((const char *)buf, len, seed);
}

template <>
const city_hash_64_t::hash_value_t city_hash_64_t::operator()(void *buf, size_t len, city_hash_64_t::seed_value_t seed) const
{
	if (seed)
	{
		return CityHash64WithSeed((const char *)buf, len, seed);
	}
	else
	{
		return CityHash64((const char *)buf, len);
	}
}

#ifdef SUPPORT_INT128

template <>
inline const city_hash_128_t::hash_value_t city_hash_128_t::operator()(void *buf, size_t len, city_hash_128_t::seed_value_t seed) const
{
#if defined(__SSE4_2__) && defined(__x86_64__)
	if (has_sse4_2)
	{
		if (seed)
		{
			const uint128 &hash = CityHashCrc128WithSeed((const char *)buf, len, std::make_pair(U128_LO(seed), U128_HI(seed)));

			return *(uint128_t *)&hash;
		}
		else
		{
			const uint128 &hash = CityHashCrc128((const char *)buf, len);

			return *(uint128_t *)&hash;
		}
	}
#endif

	if (seed)
	{
		const uint128 &hash = CityHash128WithSeed((const char *)buf, len, std::make_pair(U128_LO(seed), U128_HI(seed)));

		return *(uint128_t *)&hash;
	}
	else
	{
		const uint128 &hash = CityHash128((const char *)buf, len);

		return *(uint128_t *)&hash;
	}
}

#endif

#if defined(__SSE4_2__) && defined(__x86_64__)

template <typename T>
struct city_hash_crc_t : public Hasher<city_hash_crc_t<T>, T>
{
  public:
	typedef Hasher<city_hash_crc_t<T>, T> __hasher_t;
	typedef typename __hasher_t::hash_value_t hash_value_t;
	typedef typename __hasher_t::seed_value_t seed_value_t;

	const hash_value_t operator()(void *buf, size_t len, seed_value_t seed) const override;
};

typedef city_hash_crc_t<uint128_t> city_hash_crc_128_t;

template <>
inline const city_hash_crc_128_t::hash_value_t city_hash_crc_128_t::operator()(void *buf, size_t len, city_hash_crc_128_t::seed_value_t seed) const
{
	if (seed)
	{
		const uint128 &hash = CityHashCrc128WithSeed((const char *)buf, len, std::make_pair(U128_LO(seed), U128_HI(seed)));

		return *(uint128_t *)&hash;
	}
	else
	{
		const uint128 &hash = CityHashCrc128((const char *)buf, len);

		return *(uint128_t *)&hash;
	}
}

bool support_sse4_2(void)
{
	unsigned cpuinfo[4] = {0};
	unsigned infotype = 1;

#ifdef _MSC_VER
	__cpuid(cpuinfo, infotype);
#else
// cpuid and PIC mode don't play nice. Push ebx before use!
// see http://www.technovelty.org/code/arch/pic-cas.html
#ifdef __x86_64__
	__asm__ __volatile__(
		"cpuid;"
		: "=a"(cpuinfo[0]), "=b"(cpuinfo[1]), "=c"(cpuinfo[2]), "=d"(cpuinfo[3])
		: "a"(infotype));
#else
	__asm__ __volatile__(
		"pushl %%ebx;"
		"cpuid;"
		"movl %%ebx,%1;"
		"pop %%ebx;"
		: "=a"(cpuinfo[0]), "=m"(cpuinfo[1]), "=c"(cpuinfo[2]), "=d"(cpuinfo[3])
		: "a"(infotype));
#endif
#endif

	return cpuinfo[2] & (1 << 20);
}

#ifdef SUPPORT_INT128

template <>
inline void city_hash_128_t::__hasher_t::Export(const py::module &m, const char *name)
{
	city_hash_128_t::has_sse4_2 = support_sse4_2();

	py::class_<city_hash_128_t>(m, name)
		.def(py::init<>())
		.def_property_readonly_static("has_sse4_2", [](py::object /* self */) { return city_hash_128_t::has_sse4_2; })
		.def("__call__", &city_hash_128_t::CallWithArgs);
}

template <>
inline void city_hash_crc_128_t::__hasher_t::Export(const py::module &m, const char *name)
{
	py::class_<city_hash_crc_128_t>(m, name)
		.def(py::init<>())
		.def("__call__", &city_hash_crc_128_t::CallWithArgs);
}

#endif

#endif
