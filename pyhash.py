#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import sys

import _pyhash

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

lookup3 = _pyhash.lookup3_little if sys.byteorder == 'little' else _pyhash.lookup3_big
lookup3_little = _pyhash.lookup3_little
lookup3_big = _pyhash.lookup3_big

super_fast_hash = _pyhash.super_fast_hash

city_64 = _pyhash.city_64
city_128 = _pyhash.city_128

import unittest
import logging

class TestHasher(unittest.TestCase):
    def setUp(self):
        self.data = b'test'
        self.udata = u'test'

    def doTest(self, hasher_type, bytes_hash, seed_hash, unicode_hash):
        hasher = hasher_type()

        self.assertEqual(bytes_hash, hasher(self.data))

        self.assertEqual(seed_hash, hasher(self.data, seed=bytes_hash))

        self.assertEqual(seed_hash, hasher(self.data, self.data))

        self.assertEqual(unicode_hash, hasher(self.udata))

class TestFNV1(TestHasher):
    def testFNV1_32(self):
        self.doTest(hasher_type=fnv1_32,
                    bytes_hash=3698262380L,
                    seed_hash=660137056,
                    unicode_hash=3910690890L)

    def testFNV1a_32(self):
        self.doTest(hasher_type=fnv1a_32,
                    bytes_hash=1858026756,
                    seed_hash=1357873952,
                    unicode_hash=996945022)

    def testFNV1_64(self):
        self.doTest(hasher_type=fnv1_64,
                    bytes_hash=17151984479173897804L,
                    seed_hash=6349570372626520864L,
                    unicode_hash=14017453969697934794L)

    def testFNV1a_64(self):
        self.doTest(hasher_type=fnv1a_64,
                    bytes_hash=11830222609977404196L,
                    seed_hash=8858165303110309728L,
                    unicode_hash=14494269412771327550L)


class TestMurMurHash(TestHasher):
    def testMurMurHash1_32(self):
        self.doTest(hasher_type=murmur1_32,
                    bytes_hash=1706635965,
                    seed_hash=1637637239,
                    unicode_hash=2296970802L)

    def testMurMurHash1Aligned_32(self):
        self.doTest(hasher_type=murmur1_aligned_32,
                    bytes_hash=1706635965,
                    seed_hash=1637637239,
                    unicode_hash=2296970802L)

    def testMurMurHash2_32(self):
        self.doTest(hasher_type=murmur2_32,
                    bytes_hash=403862830,
                    seed_hash=1257009171,
                    unicode_hash=2308212514L)

    def testMurMurHash2a_32(self):
        self.doTest(hasher_type=murmur2a_32,
                    bytes_hash=1026673864,
                    seed_hash=3640713775L,
                    unicode_hash=3710634486L)

    def testMurMurHash2Aligned32(self):
        self.doTest(hasher_type=murmur2_aligned_32,
                    bytes_hash=403862830,
                    seed_hash=1257009171,
                    unicode_hash=2308212514L)

    def testMurMurHash2Neutral32(self):
        self.doTest(hasher_type=murmur2_neutral_32,
                    bytes_hash=403862830,
                    seed_hash=1257009171,
                    unicode_hash=2308212514L)

    def testMurMurHash2_x64_64a(self):
        self.doTest(hasher_type=murmur2_x64_64a,
                    bytes_hash=3407684658384555107L,
                    seed_hash=14278059344916754999L,
                    unicode_hash=9820020607534352415L)

    def testMurMurHash2_x86_64b(self):
        self.doTest(hasher_type=murmur2_x86_64b,
                    bytes_hash=1560774255606158893L,
                    seed_hash=11567531768634065834L,
                    unicode_hash=7104676830630207180L)

    def testMurMurHash3_32(self):
        self.doTest(hasher_type=murmur3_32,
                    bytes_hash=3127628307,
                    seed_hash=1973649836,
                    unicode_hash=1351191292)

    def testMurMurHash3_x86_128(self):
        self.doTest(hasher_type=murmur3_x86_128,
                    bytes_hash=113049230771270950235709929058346397488L,
                    seed_hash=201730919445129814667855021331871906456L,
                    unicode_hash=34467989874860051826961972957664456325L)

    def testMurMurHash3_x64_128(self):
        self.doTest(hasher_type=murmur3_x64_128,
                    bytes_hash=204797213367049729698754624420042367389L,
                    seed_hash=25000065729391260169145522623652811022L,
                    unicode_hash=301054382688326301269845371608405900524L)

class TestLookup3(TestHasher):
    def testLookup3(self):
        self.doTest(hasher_type=lookup3,
                    bytes_hash=3188463954L,
                    seed_hash=478901866,
                    unicode_hash=1380664715)


class TestSuperFastHash(TestHasher):
    def testSuperFastHash(self):
        self.doTest(hasher_type=super_fast_hash,
                    bytes_hash=942683319,
                    seed_hash=777359542,
                    unicode_hash=1430748046)


class TestCityHash(TestHasher):
    def testCityHash64(self):
        self.doTest(hasher_type=city_64,
                    bytes_hash=17703940110308125106L,
                    seed_hash=8806864191580960558L,
                    unicode_hash=7557950076747784205L)

    def testCityHash128(self):
        self.doTest(hasher_type=city_128,
                    bytes_hash=195179989828428219998331619914059544201L,
                    seed_hash=206755929755292977387372217469167977636L,
                    unicode_hash=211596129097514838244042408160146499227L)

if __name__ == '__main__':
    if "-v" in sys.argv:
        level = logging.DEBUG
    else:
        level = logging.WARN

    logging.basicConfig(level=level, format='%(asctime)s %(levelname)s %(message)s')

    unittest.main()
