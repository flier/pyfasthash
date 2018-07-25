import pytest

import pyhash


def test_lookup3(hash_tester):
    hash_tester(hasher_type=pyhash.lookup3,
                bytes_hash=3188463954,
                seed_hash=478901866,
                unicode_hash=1380664715)
