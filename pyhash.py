#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

import _pyhash

fnv1_32 = _pyhash.fnv1_32
fnv1a_32 = _pyhash.fnv1a_32
fnv1_64 = _pyhash.fnv1_64
fnv1a_64 = _pyhash.fnv1a_64

import unittest
import logging

class TestFNV(unittest.TestCase):
    def setUp(self):
        self.data = 'test'
        self.udata = u'test'
        
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

if __name__ == '__main__':
    if "-v" in sys.argv:
        level = logging.DEBUG
    else:
        level = logging.WARN
    
    logging.basicConfig(level=level, format='%(asctime)s %(levelname)s %(message)s')
    
    unittest.main()