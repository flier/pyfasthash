#include "Hash.h"

#include "FNV1.h"
#include "MurmurHash.h"
#include "Lookup3.h"
#include "SuperFastHash.h"
#include "CityHash.h"
#include "SpookyHash.h"
#ifndef _MSC_VER
#include "FarmHash.h"
#endif
#include "MetroHash.h"
#include "Mum.h"
#include "T1.h"
#include "xxHash.h"

BOOST_PYTHON_MODULE(_pyhash)
{
  fnv1_32_t::Export("fnv1_32");
  fnv1a_32_t::Export("fnv1a_32");
  fnv1_64_t::Export("fnv1_64");
  fnv1a_64_t::Export("fnv1a_64");

  murmur1_32_t::Export("murmur1_32");
  murmur1_aligned_32_t::Export("murmur1_aligned_32");
  murmur2_32_t::Export("murmur2_32");
  murmur2a_32_t::Export("murmur2a_32");
  murmur2_aligned_32_t::Export("murmur2_aligned_32");
  murmur2_neutral_32_t::Export("murmur2_neutral_32");
  murmur2_x64_64a_t::Export("murmur2_x64_64a");
  murmur2_x86_64b_t::Export("murmur2_x86_64b");
  murmur3_32_t::Export("murmur3_32");
#ifdef SUPPORT_INT128
  murmur3_x86_128_t::Export("murmur3_x86_128");
  murmur3_x64_128_t::Export("murmur3_x64_128");
#endif

  lookup3_little_t::Export("lookup3_little");
  lookup3_big_t::Export("lookup3_big");

  super_fast_hash_t::Export("super_fast_hash");

  city_hash_32_t::Export("city_32");
  city_hash_64_t::Export("city_64");
#ifdef SUPPORT_INT128
  city_hash_128_t::Export("city_128");
  city_hash_crc_128_t::Export("city_crc_128");
#endif

  spooky_hash_32_t::Export("spooky_32");
  spooky_hash_64_t::Export("spooky_64");
#ifdef SUPPORT_INT128
  spooky_hash_128_t::Export("spooky_128");
#endif

#ifndef _MSC_VER
  farm_hash_32_t::Export("farm_32");
  farm_hash_64_t::Export("farm_64");
#ifdef SUPPORT_INT128
  farm_hash_128_t::Export("farm_128");
#endif
#endif

  metro_hash_64_1_t::Export("metro_64_1");
  metro_hash_64_2_t::Export("metro_64_2");
#ifdef SUPPORT_INT128
  metro_hash_128_1_t::Export("metro_128_1");
  metro_hash_128_2_t::Export("metro_128_2");
#endif

  metro_hash_64_crc_1_t::Export("metro_64_crc_1");
  metro_hash_64_crc_2_t::Export("metro_64_crc_2");
#ifdef SUPPORT_INT128
  metro_hash_128_crc_1_t::Export("metro_128_crc_1");
  metro_hash_128_crc_2_t::Export("metro_128_crc_2");
#endif

  mum_hash_64_t::Export("mum_64");

  t1_hash_32_t::Export("t1_32");
  t1_hash_32_be_t::Export("t1_32_be");
  t1_hash_64_t::Export("t1_64");
  t1_hash_64_be_t::Export("t1_64_be");

  xx_hash_32_t::Export("xx_32");
  xx_hash_64_t::Export("xx_64");
};
