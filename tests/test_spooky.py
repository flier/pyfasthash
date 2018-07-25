import pytest

import pyhash


def test_spooky_32(hash_tester):
    hash_tester(hasher_type=pyhash.spooky_32,
                bytes_hash=1882037601,
                seed_hash=1324274298,
                unicode_hash=2977967976)


def test_spooky_64(hash_tester):
    hash_tester(hasher_type=pyhash.spooky_64,
                bytes_hash=10130480990056717665,
                seed_hash=1598355329892273278,
                unicode_hash=4093159241144086376)


def test_spooky_128(hash_tester):
    hash_tester(hasher_type=pyhash.spooky_128,
                bytes_hash=241061513486538422840128476001680072033,
                seed_hash=315901747311404831226315334184550174199,
                unicode_hash=207554373952009549684886824908954283880)
