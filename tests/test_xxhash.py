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


def test_xxh3_64(hash_tester):
    hash_tester(hasher_type=pyhash.xxh3_64,
                bytes_hash=9511462701433476418,
                seed_hash=18431907721717861993,
                unicode_hash=9339502706477692137)


@pytest.mark.skipif(not pyhash.build_with_int128, reason="requires int128 support")
def test_xxh3_128(hash_tester):
    hash_tester(hasher_type=pyhash.xxh3_128,
                bytes_hash=61773019920352653487352012421565896002,
                seed_hash=75077604214798731190000330999719120489,
                unicode_hash=253138563925068684169935446223964533993)


@pytest.mark.benchmark(group='hash32', disable_gc=True)
def test_xx_hash32_perf(benchmark, hash_bencher):
    hash_bencher(benchmark, pyhash.xx_32, 1497633363)


@pytest.mark.benchmark(group='hash64', disable_gc=True)
def test_xx_hash64_perf(benchmark, hash_bencher):
    hash_bencher(benchmark, pyhash.xx_64, 2282408585429094475)


@pytest.mark.benchmark(group='hash64', disable_gc=True)
def test_xxh3_hash64_perf(benchmark, hash_bencher):
    hash_bencher(benchmark, pyhash.xxh3_64, 5383753519105369680)


@pytest.mark.skipif(not pyhash.build_with_int128, reason="requires int128 support")
@pytest.mark.benchmark(group='hash128', disable_gc=True)
def test_xxh3_hash128_perf(benchmark, hash_bencher):
    hash_bencher(benchmark, pyhash.xxh3_128,
                 38410093203896075778304082117375728449)
