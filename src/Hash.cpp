#include "Hash.h"

#include "FNV1.h"
#include "MurmurHash.h"
#include "Lookup3.h"
#include "SuperFastHash.h"

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

  lookup3_little_t::Export("lookup3_little");
  lookup3_big_t::Export("lookup3_big");

  super_fast_hash_t::Export("super_fast_hash");
}