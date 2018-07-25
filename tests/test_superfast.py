import pytest

import pyhash


def test_lookup3(hash_tester):
    hash_tester(hasher_type=pyhash.super_fast_hash,
                bytes_hash=942683319,
                seed_hash=777359542,
                unicode_hash=1430748046)
