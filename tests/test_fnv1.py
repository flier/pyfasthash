import pytest

import pyhash


def test_fnv1_32(hash_tester):
    hash_tester(hasher_type=pyhash.fnv1_32,
                bytes_hash=3698262380,
                seed_hash=660137056,
                unicode_hash=3910690890)


def test_fnv1a_32(hash_tester):
    hash_tester(hasher_type=pyhash.fnv1a_32,
                bytes_hash=1858026756,
                seed_hash=1357873952,
                unicode_hash=996945022)


def test_fnv1_64(hash_tester):
    hash_tester(hasher_type=pyhash.fnv1_64,
                bytes_hash=17151984479173897804,
                seed_hash=6349570372626520864,
                unicode_hash=14017453969697934794)


def test_fnv1a_64(hash_tester):
    hash_tester(hasher_type=pyhash.fnv1a_64,
                bytes_hash=11830222609977404196,
                seed_hash=8858165303110309728,
                unicode_hash=14494269412771327550)
