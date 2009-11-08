#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys, os

import _pyhash

fnv1_32 = _pyhash.fnv1_32
fnv1a_32 = _pyhash.fnv1a_32
fnv1_64 = _pyhash.fnv1_64
fnv1a_64 = _pyhash.fnv1a_64

murmur2_32 = _pyhash.murmur2_32
murmur2a_32 = _pyhash.murmur2a_32
murmur2_aligned_32 = _pyhash.murmur2_aligned_32
murmur2_neutral_32 = _pyhash.murmur2_neutral_32
murmur2_64 = _pyhash.murmur2_64

import unittest
import logging

class TestHasher(unittest.TestCase):
    def setUp(self):
        self.data = 'test'
        self.udata = u'test'

class TestFNV1(TestHasher):        
    def testFNV1_32(self):
        hasher = fnv1_32()
        
        self.assertEqual(3698262380L, hasher(self.data))
        self.assertEqual(660137056, hasher(self.data, self.data))
        
        if os.name == "nt":
            self.assertEqual(3910690890L, hasher(self.udata))
        else:
            self.assertEqual(619499010, hasher(self.udata))
        
    def testFNV1a_32(self):
        hasher = fnv1a_32()
        
        self.assertEqual(1858026756, hasher(self.data))
        self.assertEqual(1357873952, hasher(self.data, self.data))
        
        if os.name == "nt":
            self.assertEqual(996945022, hasher(self.udata))
        else:
            self.assertEqual(583552294, hasher(self.udata))
        
    def testFNV1_64(self):
        hasher = fnv1_64()
        
        self.assertEqual(17151984479173897804L, hasher(self.data))
        self.assertEqual(6349570372626520864L, hasher(self.data, self.data))
        
        if os.name == "nt":
            self.assertEqual(14017453969697934794L, hasher(self.udata))
        else:
            self.assertEqual(12225005685850216898L, hasher(self.udata))
        
    def testFNV1a_64(self):
        hasher = fnv1a_64()
        
        self.assertEqual(11830222609977404196L, hasher(self.data))
        self.assertEqual(8858165303110309728L, hasher(self.data, self.data))
        
        if os.name == "nt":
            self.assertEqual(14494269412771327550L, hasher(self.udata))
        else:
            self.assertEqual(9509857141423752358L, hasher(self.udata))
            
class TestMurMurHash2(TestHasher):
    def testMurMurHash2_32(self):
        hasher = murmur2_32()

        self.assertEqual(403862830, hasher(self.data))
        self.assertEqual(1257009171, hasher(self.data, self.data))
        
        if os.name == "nt":
            self.assertEqual(2308212514L, hasher(self.udata))
        else:
            self.assertEqual(2325743913L, hasher(self.udata))

    def testMurMurHash2a_32(self):
        hasher = murmur2a_32()

        self.assertEqual(1026673864, hasher(self.data))
        self.assertEqual(3640713775L, hasher(self.data, self.data))
        
        if os.name == "nt":
            self.assertEqual(3710634486L, hasher(self.udata))
        else:
            self.assertEqual(787576890, hasher(self.udata))

    def testMurMurHash2Aligned32(self):
        hasher = murmur2_aligned_32()

        self.assertEqual(403862830, hasher(self.data))
        self.assertEqual(1257009171, hasher(self.data, self.data))
        
        if os.name == "nt":
            self.assertEqual(2308212514L, hasher(self.udata))
        else:
            self.assertEqual(2325743913L, hasher(self.udata))

    def testMurMurHash2Neutral32(self):
        hasher = murmur2_neutral_32()

        self.assertEqual(403862830, hasher(self.data))
        self.assertEqual(1257009171, hasher(self.data, self.data))
        
        if os.name == "nt":
            self.assertEqual(2308212514L, hasher(self.udata))
        else:
            self.assertEqual(2325743913L, hasher(self.udata))

    def testMurMurHash2_64(self):
        hasher = murmur2_64()

        self.assertEqual(3407684658384555107L, hasher(self.data))
        self.assertEqual(940757698219426231L, hasher(self.data, self.data))
        
        if os.name == "nt":
            self.assertEqual(9820020607534352415L, hasher(self.udata))
        else:
            self.assertEqual(5522330703187561353L, hasher(self.udata))

if __name__ == '__main__':
    if "-v" in sys.argv:
        level = logging.DEBUG
    else:
        level = logging.WARN
    
    logging.basicConfig(level=level, format='%(asctime)s %(levelname)s %(message)s')
    
    unittest.main()