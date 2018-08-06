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
#include "T1ha.h"
#include "xxHash.h"

PYBIND11_MODULE(_pyhash, m)
{
  m.doc() = "Python Non-cryptographic Hash Library";

#if defined(__SSE4_2__) && defined(__x86_64__)
  m.attr("build_with_sse42") = true;
#else
  m.attr("build_with_sse42") = false;
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
#ifdef SUPPORT_INT128
  murmur3_x86_128_t::Export(m, "murmur3_x86_128");
  murmur3_x64_128_t::Export(m, "murmur3_x64_128");
#endif

  lookup3_little_t::Export(m, "lookup3_little");
  lookup3_big_t::Export(m, "lookup3_big");

  super_fast_hash_t::Export(m, "super_fast_hash");

  city_hash_32_t::Export(m, "city_32");
  city_hash_64_t::Export(m, "city_64");
#ifdef SUPPORT_INT128
  city_hash_128_t::Export(m, "city_128");
  city_hash_crc_128_t::Export(m, "city_crc_128");
  city_fingerprint_256_t::Export(m, "city_fingerprint_256");
#endif

  spooky_hash_32_t::Export(m, "spooky_32");
  spooky_hash_64_t::Export(m, "spooky_64");
#ifdef SUPPORT_INT128
  spooky_hash_128_t::Export(m, "spooky_128");
#endif

#ifndef _MSC_VER
  farm_hash_32_t::Export(m, "farm_32");
  farm_hash_64_t::Export(m, "farm_64");
#ifdef SUPPORT_INT128
  farm_hash_128_t::Export(m, "farm_128");
#endif
#endif

#ifndef _MSC_VER
  farm_fingerprint_32_t::Export(m, "farm_fingerprint_32");
  farm_fingerprint_64_t::Export(m, "farm_fingerprint_64");
#ifdef SUPPORT_INT128
  farm_fingerprint_128_t::Export(m, "farm_fingerprint_128");
#endif
#endif

  metro_hash_64_1_t::Export(m, "metro_64_1");
  metro_hash_64_2_t::Export(m, "metro_64_2");
#ifdef SUPPORT_INT128
  metro_hash_128_1_t::Export(m, "metro_128_1");
  metro_hash_128_2_t::Export(m, "metro_128_2");
#endif

  metro_hash_64_crc_1_t::Export(m, "metro_64_crc_1");
  metro_hash_64_crc_2_t::Export(m, "metro_64_crc_2");
#ifdef SUPPORT_INT128
  metro_hash_128_crc_1_t::Export(m, "metro_128_crc_1");
  metro_hash_128_crc_2_t::Export(m, "metro_128_crc_2");
#endif

  mum_hash_64_t::Export(m, "mum_64");

  t1ha2_atonce_t::Export(m, "t1ha2_atonce");
  t1ha2_atonce128_t::Export(m, "t1ha2_atonce128");
  t1ha1_le_t::Export(m, "t1ha1_le");
  t1ha1_be_t::Export(m, "t1ha1_be");
  t1ha0_t::Export(m, "t1ha0");

  xx_hash_32_t::Export(m, "xx_32");
  xx_hash_64_t::Export(m, "xx_64");
}

#include "t1ha/src/t1ha_bits.h"

#if T1HA0_RUNTIME_SELECT

#if T1HA0_AESNI_AVAILABLE && defined(__ia32__)
static uint64_t x86_cpu_features(void)
{
  uint32_t features = 0;
  uint32_t extended = 0;
#ifdef __GNUC__
  uint32_t eax, ebx, ecx, edx;
  const unsigned cpuid_max = __get_cpuid_max(0, NULL);
  if (cpuid_max >= 1)
  {
    __cpuid_count(1, 0, eax, ebx, features, edx);
    if (cpuid_max >= 7)
      __cpuid_count(7, 0, eax, extended, ecx, edx);
  }
#elif defined(_MSC_VER)
  int info[4];
  __cpuid(info, 0);
  const unsigned cpuid_max = info[0];
  if (cpuid_max >= 1)
  {
    __cpuidex(info, 1, 0);
    features = info[2];
    if (cpuid_max >= 7)
    {
      __cpuidex(info, 7, 0);
      extended = info[1];
    }
  }
#endif
  return features | (uint64_t)extended << 32;
}
#endif /* T1HA0_AESNI_AVAILABLE && __ia32__ */

#if __GNUC_PREREQ(4, 0) || __has_attribute(used)
__attribute__((used))
#endif
uint64_t (*t1ha0_resolve(void))(const void *, size_t, uint64_t)
{

#if T1HA0_AESNI_AVAILABLE && defined(__ia32__)
  uint64_t features = x86_cpu_features();
  if (features & UINT32_C(0x02000000) /* check for AES-NI */)
  {
    if ((features & UINT32_C(0x1A000000)) ==
        UINT32_C(0x1A000000) /* check for any AVX */)
      /* check for 'Advanced Vector Extensions 2' */
      return ((features >> 32) & 32) ? t1ha0_ia32aes_avx2 : t1ha0_ia32aes_avx;
    return t1ha0_ia32aes_noavx;
  }
#endif /* T1HA0_AESNI_AVAILABLE && __ia32__ */

#if __BYTE_ORDER__ == __ORDER_BIG_ENDIAN__
#if (UINTPTR_MAX > 0xffffFFFFul || ULONG_MAX > 0xffffFFFFul) && \
    (!defined(T1HA1_DISABLED) || !defined(T1HA2_DISABLED))
#ifndef T1HA1_DISABLED
  return t1ha1_be;
#else
  return t1ha2_atonce;
#endif /* T1HA1_DISABLED */
#else
  return t1ha0_32be;
#endif
#else /* __BYTE_ORDER__ != __ORDER_BIG_ENDIAN__ */
#if (UINTPTR_MAX > 0xffffFFFFul || ULONG_MAX > 0xffffFFFFul) && \
    (!defined(T1HA1_DISABLED) || !defined(T1HA2_DISABLED))
#ifndef T1HA1_DISABLED
  return t1ha1_le;
#else
  return t1ha2_atonce;
#endif /* T1HA1_DISABLED */
#else
  return t1ha0_32le;
#endif
#endif /* __BYTE_ORDER__ */
}
#endif /* T1HA0_RUNTIME_SELECT */
