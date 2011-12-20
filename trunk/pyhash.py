#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys, os

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

lookup3 = _pyhash.lookup3_little if sys.byteorder == 'little' else _pyhash.lookup3_big
lookup3_little = _pyhash.lookup3_little
lookup3_big = _pyhash.lookup3_big

super_fast_hash = _pyhash.super_fast_hash

import unittest
import logging

class TestHasher(unittest.TestCase):
    def setUp(self):
        self.data = 'test'
        self.udata = u'test'

    def testSeed(self):
        hasher = fnv1_32()

        self.assertEqual(3698262380L, hasher(self.data))
        self.assertEqual(660137056, hasher(self.data, seed=3698262380L))

class TestFNV1(TestHasher):        
    def testFNV1_32(self):
        hasher = fnv1_32()
        
        self.assertEqual(3698262380L, hasher(self.data))
        self.assertEqual(660137056, hasher(self.data, self.data))
        
        self.assertEqual(3910690890L, hasher(self.udata))
        
    def testFNV1a_32(self):
        hasher = fnv1a_32()
        
        self.assertEqual(1858026756, hasher(self.data))
        self.assertEqual(1357873952, hasher(self.data, self.data))
        
        self.assertEqual(996945022, hasher(self.udata))
        
    def testFNV1_64(self):
        hasher = fnv1_64()
        
        self.assertEqual(17151984479173897804L, hasher(self.data))
        self.assertEqual(6349570372626520864L, hasher(self.data, self.data))
        
        self.assertEqual(14017453969697934794L, hasher(self.udata))
        
    def testFNV1a_64(self):
        hasher = fnv1a_64()
        
        self.assertEqual(11830222609977404196L, hasher(self.data))
        self.assertEqual(8858165303110309728L, hasher(self.data, self.data))
        
        self.assertEqual(14494269412771327550L, hasher(self.udata))
            
class TestMurMurHash2(TestHasher):
    def testMurMurHash1_32(self):
        hasher = murmur1_32()

        self.assertEqual(1706635965, hasher(self.data))
        self.assertEqual(1637637239, hasher(self.data, self.data))

        self.assertEqual(2296970802L, hasher(self.udata))

    def testMurMurHash1Aligned_32(self):
        hasher = murmur1_aligned_32()

        self.assertEqual(1706635965, hasher(self.data))
        self.assertEqual(1637637239, hasher(self.data, self.data))

        self.assertEqual(2296970802L, hasher(self.udata))

    def testMurMurHash2_32(self):
        hasher = murmur2_32()

        self.assertEqual(403862830, hasher(self.data))
        self.assertEqual(1257009171, hasher(self.data, self.data))
        
        self.assertEqual(2308212514L, hasher(self.udata))

    def testMurMurHash2a_32(self):
        hasher = murmur2a_32()

        self.assertEqual(1026673864, hasher(self.data))
        self.assertEqual(3640713775L, hasher(self.data, self.data))
        
        self.assertEqual(3710634486L, hasher(self.udata))

    def testMurMurHash2Aligned32(self):
        hasher = murmur2_aligned_32()

        self.assertEqual(403862830, hasher(self.data))
        self.assertEqual(1257009171, hasher(self.data, self.data))
        
        self.assertEqual(2308212514L, hasher(self.udata))

    def testMurMurHash2Neutral32(self):
        hasher = murmur2_neutral_32()

        self.assertEqual(403862830, hasher(self.data))
        self.assertEqual(1257009171, hasher(self.data, self.data))
        
        self.assertEqual(2308212514L, hasher(self.udata))

    def testMurMurHash2_x64_64a(self):
        hasher = murmur2_x64_64a()

        self.assertEqual(3407684658384555107L, hasher(self.data))
        self.assertEqual(14278059344916754999L, hasher(self.data, self.data))

        self.assertEqual(9820020607534352415L, hasher(self.udata))

    def testMurMurHash2_x86_64b(self):
        hasher = murmur2_x86_64b()

        self.assertEqual(1560774255606158893L, hasher(self.data))
        self.assertEqual(11567531768634065834L, hasher(self.data, self.data))

        self.assertEqual(7104676830630207180L, hasher(self.udata))

    def testMurMurHash3_32(self):
        hasher = murmur3_32()

        self.assertEqual(3127628307, hasher(self.data))
        self.assertEqual(1973649836, hasher(self.data, self.data))

        self.assertEqual(1351191292, hasher(self.udata))

class TestLookup3(TestHasher):
    def testLookup3(self):
        hasher = lookup3()

        self.assertEqual(3188463954L, hasher(self.data))
        self.assertEqual(478901866, hasher(self.data, self.data))
        
        self.assertEqual(1380664715, hasher(self.udata))
            
class TestSuperFastHash(TestHasher):
    def testSuperFastHash(self):
        hasher = super_fast_hash()

        self.assertEqual(942683319, hasher(self.data))
        self.assertEqual(777359542, hasher(self.data, self.data))
        
        self.assertEqual(1430748046, hasher(self.udata))
            
if __name__ == '__main__':
    if "-v" in sys.argv:
        level = logging.DEBUG
    else:
        level = logging.WARN
    
    logging.basicConfig(level=level, format='%(asctime)s %(levelname)s %(message)s')
    
    unittest.main()