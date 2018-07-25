import pytest

import pyhash


def test_xx_32(hash_tester):
    hash_tester(hasher_type=pyhash.xx_32,
                bytes_hash=1042293711,
                seed_hash=1018767936,
                unicode_hash=2783988247)


def test_xx_64(hash_tester):
    hash_tester(hasher_type=pyhash.xx_64,
                bytes_hash=5754696928334414137,
                seed_hash=12934826212537126916,
                unicode_hash=16125048496228390453)
