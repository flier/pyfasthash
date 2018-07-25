import pytest

import pyhash


def test_murmur1_32(hash_tester):
    hash_tester(hasher_type=pyhash.murmur1_32,
                bytes_hash=1706635965,
                seed_hash=1637637239,
                unicode_hash=2296970802)


def test_murmur1_aligned_32(hash_tester):
    hash_tester(hasher_type=pyhash.murmur1_aligned_32,
                bytes_hash=1706635965,
                seed_hash=1637637239,
                unicode_hash=2296970802)


def test_murmur2_32(hash_tester):
    hash_tester(hasher_type=pyhash.murmur2_32,
                bytes_hash=403862830,
                seed_hash=1257009171,
                unicode_hash=2308212514)


def test_murmur2a_32(hash_tester):
    hash_tester(hasher_type=pyhash.murmur2a_32,
                bytes_hash=1026673864,
                seed_hash=3640713775,
                unicode_hash=3710634486)


def test_murmur2_aligned32(hash_tester):
    hash_tester(hasher_type=pyhash.murmur2_aligned_32,
                bytes_hash=403862830,
                seed_hash=1257009171,
                unicode_hash=2308212514)


def test_murmur2_neutral32(hash_tester):
    hash_tester(hasher_type=pyhash.murmur2_neutral_32,
                bytes_hash=403862830,
                seed_hash=1257009171,
                unicode_hash=2308212514)


def test_murmur2_x64_64a(hash_tester):
    hash_tester(hasher_type=pyhash.murmur2_x64_64a,
                bytes_hash=3407684658384555107,
                seed_hash=14278059344916754999,
                unicode_hash=9820020607534352415)


def test_murmur2_x86_64b(hash_tester):
    hash_tester(hasher_type=pyhash.murmur2_x86_64b,
                bytes_hash=1560774255606158893,
                seed_hash=11567531768634065834,
                unicode_hash=7104676830630207180)


def test_murmur3_32(hash_tester):
    hash_tester(hasher_type=pyhash.murmur3_32,
                bytes_hash=3127628307,
                seed_hash=1973649836,
                unicode_hash=1351191292)


def test_murmur3_x86_128(hash_tester):
    hash_tester(hasher_type=pyhash.murmur3_x86_128,
                bytes_hash=113049230771270950235709929058346397488,
                seed_hash=201730919445129814667855021331871906456,
                unicode_hash=34467989874860051826961972957664456325)


def test_murmur3_x64_128(hash_tester):
    hash_tester(hasher_type=pyhash.murmur3_x64_128,
                bytes_hash=204797213367049729698754624420042367389,
                seed_hash=25000065729391260169145522623652811022,
                unicode_hash=301054382688326301269845371608405900524)
