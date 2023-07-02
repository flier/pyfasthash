#include "Hash.h"

#include "FNV1.h"
#include "MurmurHash.h"
#include "Lookup3.h"
#include "SuperFastHash.h"
#include "CityHash.h"
#include "SpookyHash.h"
#include "FarmHash.h"
#include "MetroHash.h"
#include "Mum.h"
#include "T1ha.h"
#include "xxHash.h"
#include "Highway.h"
#include "wyHash.h"
#include "Halftime.h"

PYBIND11_MODULE(_pyhash, m)
{
  m.doc() = "Python Non-cryptographic Hash Library";

#if defined(__SSE4_2__) && defined(__x86_64__)
  m.attr("build_with_sse42") = true;
#else
  m.attr("build_with_sse42") = false;
#endif

#ifdef _MSC_VER
  m.attr("_MSC_VER") = _MSC_VER;
#endif

#ifdef __GNUC__
  m.attr("_GCC_VER") = __GNUC__ * 10000 + __GNUC_MINOR__ * 100 + __GNUC_PATCHLEVEL__;
#endif

#ifdef __clang__
  m.attr("_CLANG_VER") = __clang__ * 10000 + __clang_major__ * 100 + __clang_patchlevel__;
#endif

#ifdef __VERSION__
  m.attr("__VERSION__") = __VERSION__;
#endif

  fnv1_32_t::Export(m, "fnv1_32");
  fnv1a_32_t::Export(m, "fnv1a_32");
  fnv1_64_t::Export(m, "fnv1_64");
  fnv1a_64_t::Export(m, "fnv1a_64");

  murmur1_32_t::Export(m, "murmur1_32");
  murmur1_aligned_32_t::Export(m, "murmur1_aligned_32");
  murmur2_32_t::Export(m, "murmur2_32");
  murmur2a_32_t::Export(m, "murmur2a_32");
  murmur2_aligned_32_t::Export(m, "murmur2_aligned_32");
  murmur2_neutral_32_t::Export(m, "murmur2_neutral_32");
  murmur2_x64_64a_t::Export(m, "murmur2_x64_64a");
  murmur2_x86_64b_t::Export(m, "murmur2_x86_64b");
  murmur3_32_t::Export(m, "murmur3_32");
  murmur3_x86_128_t::Export(m, "murmur3_x86_128");
  murmur3_x64_128_t::Export(m, "murmur3_x64_128");

  lookup3_little_t::Export(m, "lookup3_little");
  lookup3_big_t::Export(m, "lookup3_big");

  super_fast_hash_t::Export(m, "super_fast_hash");

  city_hash_32_t::Export(m, "city_32");
  city_hash_64_t::Export(m, "city_64");
  city_hash_128_t::Export(m, "city_128");
#if defined(__SSE4_2__) && defined(__x86_64__)
  city_hash_crc_128_t::Export(m, "city_crc_128");
  city_fingerprint_256_t::Export(m, "city_fingerprint_256");
#endif

  spooky_hash_v1_32_t::Export(m, "spooky_v1_32");
  spooky_hash_v1_64_t::Export(m, "spooky_v1_64");
  spooky_hash_v1_128_t::Export(m, "spooky_v1_128");

  spooky_hash_v2_32_t::Export(m, "spooky_v2_32");
  spooky_hash_v2_64_t::Export(m, "spooky_v2_64");
  spooky_hash_v2_128_t::Export(m, "spooky_v2_128");

  farm_hash_32_t::Export(m, "farm_32");
  farm_hash_64_t::Export(m, "farm_64");
  farm_hash_128_t::Export(m, "farm_128");

  farm_fingerprint_32_t::Export(m, "farm_fingerprint_32");
  farm_fingerprint_64_t::Export(m, "farm_fingerprint_64");
  farm_fingerprint_128_t::Export(m, "farm_fingerprint_128");

  metro_hash_64_1_t::Export(m, "metro_64_1");
  metro_hash_64_2_t::Export(m, "metro_64_2");
  metro_hash_128_1_t::Export(m, "metro_128_1");
  metro_hash_128_2_t::Export(m, "metro_128_2");

  metro_hash_64_crc_1_t::Export(m, "metro_64_crc_1");
  metro_hash_64_crc_2_t::Export(m, "metro_64_crc_2");
  metro_hash_128_crc_1_t::Export(m, "metro_128_crc_1");
  metro_hash_128_crc_2_t::Export(m, "metro_128_crc_2");

  mum_hash_64_t::Export(m, "mum_64");

  t1ha2_atonce_t::Export(m, "t1ha2_atonce");
  t1ha2_atonce128_t::Export(m, "t1ha2_atonce128");
  t1ha1_le_t::Export(m, "t1ha1_le");
  t1ha1_be_t::Export(m, "t1ha1_be");
  t1ha0_t::Export(m, "t1ha0");

  xx_hash_32_t::Export(m, "xx_32");
  xx_hash_64_t::Export(m, "xx_64");

  xxh3_hash_64_t::Export(m, "xxh3_64");
  xxh3_hash_128_t::Export(m, "xxh3_128");

  highway_hash_64_t::Export(m, "highway_64");
  highway_hash_128_t::Export(m, "highway_128");
  highway_hash_256_t::Export(m, "highway_256");

  wy_hash_32_t::Export(m, "wy_32");
  wy_hash_64_t::Export(m, "wy_64");

  halftime_hash_64_t::Export(m, "halftime_64");

  halftime_hash_128_t::Export(m, "halftime_128");
  halftime_hash_256_t::Export(m, "halftime_256");
  halftime_hash_512_t::Export(m, "halftime_512");
}
