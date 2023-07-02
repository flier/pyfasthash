#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import sys
import inspect

import _pyhash

__is_little_endian__ = sys.byteorder == "little"

_MSC_VER = _pyhash.__dict__.get("_MSC_VER")
_GCC_VER = _pyhash.__dict__.get("_GCC_VER")
_CLANG_VER = _pyhash.__dict__.get("_CLANG_VER")
__VERSION__ = _pyhash.__dict__.get("__VERSION__")

fnv1_32 = _pyhash.fnv1_32
fnv1a_32 = _pyhash.fnv1a_32
fnv1_64 = _pyhash.fnv1_64
fnv1a_64 = _pyhash.fnv1a_64

murmur1_32 = _pyhash.murmur1_32
murmur1_aligned_32 = _pyhash.murmur1_aligned_32
murmur2_32 = _pyhash.murmur2_32
murmur2a_32 = _pyhash.murmur2a_32
murmur2_aligned_32 = _pyhash.murmur2_aligned_32
murmur2_neutral_32 = _pyhash.murmur2_neutral_32
murmur2_x64_64a = _pyhash.murmur2_x64_64a
murmur2_x86_64b = _pyhash.murmur2_x86_64b
murmur3_32 = _pyhash.murmur3_32
murmur3_x86_128 = _pyhash.murmur3_x86_128
murmur3_x64_128 = _pyhash.murmur3_x64_128

lookup3 = _pyhash.lookup3_little if __is_little_endian__ else _pyhash.lookup3_big
lookup3_little = _pyhash.lookup3_little
lookup3_big = _pyhash.lookup3_big

super_fast_hash = _pyhash.super_fast_hash

city_32 = _pyhash.city_32
city_64 = _pyhash.city_64
city_128 = _pyhash.__dict__.get("city_128")
city_crc_128 = _pyhash.__dict__.get("city_crc_128")
city_fingerprint_256 = _pyhash.__dict__.get("city_fingerprint_256")

spooky_v1_32 = _pyhash.spooky_v1_32
spooky_v1_64 = _pyhash.spooky_v1_64
spooky_v1_128 = _pyhash.spooky_v1_128

spooky_v2_32 = _pyhash.spooky_v2_32
spooky_v2_64 = _pyhash.spooky_v2_64
spooky_v2_128 = _pyhash.spooky_v2_128

spooky_32 = spooky_v2_32
spooky_64 = spooky_v2_64
spooky_128 = spooky_v2_128

farm_32 = _pyhash.farm_32
farm_64 = _pyhash.farm_64
farm_128 = _pyhash.farm_128

farm_fingerprint_32 = _pyhash.farm_fingerprint_32
farm_fingerprint_64 = _pyhash.farm_fingerprint_64
farm_fingerprint_128 = _pyhash.farm_fingerprint_128

metro_64 = metro_64_1 = _pyhash.metro_64_1
metro_64_2 = _pyhash.metro_64_2
metro_128 = metro_128_1 = _pyhash.metro_128_1
metro_128_2 = _pyhash.metro_128_2
metro_crc_64 = metro_crc_64_1 = _pyhash.__dict__.get("metro_64_crc_1")
metro_crc_64_2 = _pyhash.__dict__.get("metro_64_crc_2")
metro_crc_128 = metro_crc_128_1 = _pyhash.__dict__.get("metro_128_crc_1")
metro_crc_128_2 = _pyhash.__dict__.get("metro_128_crc_2")

mum_64 = _pyhash.mum_64

t1ha2 = t1ha2_64 = t1ha2_atonce = _pyhash.t1ha2_atonce
t1ha2_128 = t1ha2_atonce128 = _pyhash.t1ha2_atonce128
t1ha1_le = t1ha1_64le = _pyhash.t1ha1_le
t1ha1_be = t1ha1_64be = _pyhash.t1ha1_be
t1ha1 = t1ha1_64 = t1ha1_le if __is_little_endian__ else t1ha1_be
t1ha0 = t1ha0_64 = _pyhash.t1ha0

xx_32 = _pyhash.xx_32
xx_64 = _pyhash.xx_64
xxh3_64 = _pyhash.xxh3_64
xxh3_128 = _pyhash.xxh3_128

highway_64 = _pyhash.highway_64
highway_128 = _pyhash.highway_128
highway_256 = _pyhash.highway_256

wy_32 = _pyhash.wy_32
wy_64 = _pyhash.wy_64

halftime_64 = _pyhash.halftime_64
halftime_128 = _pyhash.halftime_128
halftime_256 = _pyhash.halftime_256
halftime_512 = _pyhash.halftime_512

__hasher__ = dict(inspect.getmembers(sys.modules[__name__], inspect.isclass))
