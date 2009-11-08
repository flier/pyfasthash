#include "Hash.h"

#include "FNV1.h"
#include "MurmurHash.h"

BOOST_PYTHON_MODULE(_pyhash)
{
  fnv1_32_t::Export("fnv1_32");
  fnv1a_32_t::Export("fnv1a_32");
  fnv1_64_t::Export("fnv1_64");
  fnv1a_64_t::Export("fnv1a_64");

  murmur2_32_t::Export("murmur2_32");
  murmur2a_32_t::Export("murmur2a_32");
  murmur2_aligned_32_t::Export("murmur2_aligned_32");
  murmur2_neutral_32_t::Export("murmur2_neutral_32");
  murmur2_64_t::Export("murmur2_64");
}