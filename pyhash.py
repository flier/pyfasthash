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
murmur3_x86_128 = _pyhash.__dict__.get('murmur3_x86_128')
murmur3_x64_128 = _pyhash.__dict__.get('murmur3_x64_128')

lookup3 = _pyhash.lookup3_little if sys.byteorder == 'little' else _pyhash.lookup3_big
lookup3_little = _pyhash.lookup3_little
lookup3_big = _pyhash.lookup3_big

super_fast_hash = _pyhash.super_fast_hash

city_32 = _pyhash.city_32
city_64 = _pyhash.city_64
city_128 = _pyhash.__dict__.get('city_128')
city_crc_128 = _pyhash.__dict__.get('city_crc_128')

spooky_32 = _pyhash.spooky_32
spooky_64 = _pyhash.spooky_64
spooky_128 = _pyhash.__dict__.get('spooky_128')

farm_32 = _pyhash.__dict__.get('farm_32')
farm_64 = _pyhash.__dict__.get('farm_64')
farm_128 = _pyhash.__dict__.get('farm_128')

metro_64 = metro_64_1 = _pyhash.metro_64_1
metro_64_2 = _pyhash.metro_64_2
metro_128 = metro_128_1 = _pyhash.__dict__.get('metro_128_1')
metro_128_2 = _pyhash.__dict__.get('metro_128_2')
metro_crc_64 = metro_crc_64_1 = _pyhash.metro_64_crc_1
metro_crc_64_2 = _pyhash.metro_64_crc_2
metro_crc_128 = metro_crc_128_1 = _pyhash.__dict__.get('metro_128_crc_1')
metro_crc_128_2 = _pyhash.__dict__.get('metro_128_crc_2')

mum_64 = _pyhash.mum_64

t1_32 = _pyhash.t1_32
t1_32_be = _pyhash.t1_32_be
t1_64 = _pyhash.t1_64
t1_64_be = _pyhash.t1_64_be

xx_32 = _pyhash.xx_32
xx_64 = _pyhash.xx_64

import unittest
import logging


class TestHasher(unittest.TestCase):
    def setUp(self):
        self.data = b'test'
        self.udata = u'test'

    def doTest(self, hasher_type, bytes_hash, seed_hash, unicode_hash):
        if hasher_type:
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
    def testCityHash32(self):
        self.doTest(hasher_type=city_32,
                    bytes_hash=1633095781L,
                    seed_hash=3687200064L,
                    unicode_hash=3574089775L)

    def testCityHash64(self):
        self.doTest(hasher_type=city_64,
                    bytes_hash=17703940110308125106L,
                    seed_hash=8806864191580960558L,
                    unicode_hash=7557950076747784205L)

        self.assertFalse(hasattr(city_64, 'has_sse4_2'))

    def testCityHash128(self):
        self.doTest(hasher_type=city_128,
                    bytes_hash=195179989828428219998331619914059544201L,
                    seed_hash=206755929755292977387372217469167977636L,
                    unicode_hash=211596129097514838244042408160146499227L)

        if hasattr(city_128, 'has_sse4_2'):
            self.assertTrue(city_128.has_sse4_2, "support SSE 4.2")

    def testCityHashCrc128(self):
        self.doTest(hasher_type=city_crc_128,
                    bytes_hash=195179989828428219998331619914059544201L,
                    seed_hash=206755929755292977387372217469167977636L,
                    unicode_hash=211596129097514838244042408160146499227L)


class TestSpookyHash(TestHasher):
    def testSpookyHash32(self):
        self.doTest(hasher_type=spooky_32,
                    bytes_hash=1882037601L,
                    seed_hash=1324274298L,
                    unicode_hash=2977967976L)

    def testSpookyHash64(self):
        self.doTest(hasher_type=spooky_64,
                    bytes_hash=10130480990056717665L,
                    seed_hash=1598355329892273278L,
                    unicode_hash=4093159241144086376L)

    def testSpookyHash128(self):
        self.doTest(hasher_type=spooky_128,
                    bytes_hash=241061513486538422840128476001680072033L,
                    seed_hash=315901747311404831226315334184550174199L,
                    unicode_hash=207554373952009549684886824908954283880L)


class TestFarmHash(TestHasher):
    def testFarmHash32(self):
        hasher = farm_32()

        h1 = hasher(self.data)
        h2 = hasher(self.data, seed=123)
        h3 = hasher(self.udata)

        self.assertTrue(h1 != 0)
        self.assertTrue(h2 != 0)
        self.assertTrue(h3 != 0)
        self.assertNotEqual(h1, h2)
        self.assertNotEqual(h1, h3)
        self.assertNotEqual(h2, h3)

    def testFarmHash64(self):
        self.doTest(hasher_type=farm_64,
                    bytes_hash=8581389452482819506L,
                    seed_hash=10025340881295800991L,
                    unicode_hash=7274603073818924232L)

    def testFarmHash128(self):
        self.doTest(hasher_type=farm_128,
                    bytes_hash=334882099032867325754781607143811124132L,
                    seed_hash=49442029837562385903494085441886302499L,
                    unicode_hash=251662992469041432568516527017706898625L)


class TestMetroHash(TestHasher):
    def testMetroHash64_1(self):
        self.doTest(hasher_type=metro_64_1,
                    bytes_hash=7555593383206836236L,
                    seed_hash=9613011798576657330L,
                    unicode_hash=5634638029758084150L)

    def testMetroHash128_1(self):
        self.doTest(hasher_type=metro_128_1,
                    bytes_hash=310240039238111093048322555259813357218L,
                    seed_hash=330324289553816260191102680044286377986L,
                    unicode_hash=160639312567243412360084738183177128736L)

    def testMetroHash64_2(self):
        self.doTest(hasher_type=metro_64_2,
                    bytes_hash=13328239478646503906L,
                    seed_hash=16521803336796657060L,
                    unicode_hash=5992985172783395072L)

    def testMetroHash128_2(self):
        self.doTest(hasher_type=metro_128_2,
                    bytes_hash=308979041176504703647272401075625691044L,
                    seed_hash=156408679042779357342816971045969684594L,
                    unicode_hash=169904568621124891123383613748925830588L)

    def testMetroHashCrc64_1(self):
        self.doTest(hasher_type=metro_crc_64_1,
                    bytes_hash=6872506084457499713L,
                    seed_hash=14064239385324957326L,
                    unicode_hash=5634638029758084150L)

    def testMetroHashCrc128_1(self):
        self.doTest(hasher_type=metro_crc_128_1,
                    bytes_hash=44856800307026421677415827141042094245L,
                    seed_hash=199990471895323666720887863107514038076L,
                    unicode_hash=53052528140813423722778028047086277728L)

    def testMetroHashCrc64_2(self):
        self.doTest(hasher_type=metro_crc_64_2,
                    bytes_hash=9168163846307153532L,
                    seed_hash=11235719994915751828L,
                    unicode_hash=15697829093445668111L)

    def testMetroHashCrc128_2(self):
        self.doTest(hasher_type=metro_crc_128_2,
                    bytes_hash=29039398407115405218669555123781288008L,
                    seed_hash=26197404070933777589488526163359489061L,
                    unicode_hash=136212167639765185451107230087801381416L)


class TestMumHash(TestHasher):
    def testMumHash64(self):
        self.doTest(hasher_type=mum_64,
                    bytes_hash=8715813407503360407L,
                    seed_hash=1160173209250992409L,
                    unicode_hash=16548684777514844522L)


class TestT1Hash(TestHasher):
    def testT1Hash32(self):
        if _pyhash.build_with_sse42:
            self.doTest(hasher_type=t1_32,
                        bytes_hash=1818352152L,
                        seed_hash=2109716410L,
                        unicode_hash=1338597275L)
        else:
            self.doTest(hasher_type=t1_32,
                        bytes_hash=3522842737L,
                        seed_hash=1183993215L,
                        unicode_hash=4227842359L)

    def testT1Hash32Be(self):
        self.doTest(hasher_type=t1_32_be,
                    bytes_hash=3775388856L,
                    seed_hash=2897901480L,
                    unicode_hash=1664992048L)

    def testT1Hash64(self):
        self.doTest(hasher_type=t1_64,
                    bytes_hash=10616215634819799576L,
                    seed_hash=6056749954736269874L,
                    unicode_hash=18194209408316694427L)

    def testT1Hash64Be(self):
        self.doTest(hasher_type=t1_64_be,
                    bytes_hash=10616215634819799576L,
                    seed_hash=6056749954736269874L,
                    unicode_hash=18194209408316694427L)


class TestXXHash(TestHasher):
    def testXXHash32(self):
        self.doTest(hasher_type=xx_32,
                    bytes_hash=1042293711L,
                    seed_hash=1018767936L,
                    unicode_hash=2783988247L)

    def testXXHash64(self):
        self.doTest(hasher_type=xx_64,
                    bytes_hash=5754696928334414137L,
                    seed_hash=12934826212537126916L,
                    unicode_hash=16125048496228390453L)


class TestIssues(unittest.TestCase):
    # https://github.com/flier/pyfasthash/issues/3
    def testErrorReturnNone(self):
        h = fnv1_64()

        old_refcnt = sys.getrefcount(None)

        for i in range(10000):
            try:
                h(None)

                self.fail("fail to raise exception")
            except TypeError as ex:
                pass

        new_refcnt = sys.getrefcount(None)

        self.assertTrue(old_refcnt >= new_refcnt+1)


if __name__ == '__main__':
    if "-v" in sys.argv:
        level = logging.DEBUG
    else:
        level = logging.WARN

    logging.basicConfig(level=level,
                        format='%(asctime)s %(levelname)s %(message)s')

    unittest.main()
