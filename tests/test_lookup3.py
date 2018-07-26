import pytest

import pyhash


def test_lookup3(hash_tester):
    hash_tester(hasher_type=pyhash.lookup3,
                bytes_hash=3188463954,
                seed_hash=478901866,
                unicode_hash=1380664715)


def test_lookup3_big(hash_tester):
    hash_tester(hasher_type=pyhash.lookup3_big,
                bytes_hash=305759528,
                seed_hash=1889773852,
                unicode_hash=1487153094)
