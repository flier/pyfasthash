import pytest

import pyhash


def test_wy_32(hash_tester):
    hash_tester(hasher_type=pyhash.wy_32,
                bytes_hash=3257032231,
                seed_hash=4286430599,
                unicode_hash=213393459)


def test_wy_64(hash_tester):
    hash_tester(hasher_type=pyhash.wy_64,
                bytes_hash=13282522921993940974,
                seed_hash=10112467932320148695,
                unicode_hash=2990017137888294531)


@pytest.mark.benchmark(group='hash32', disable_gc=True)
def test_wy_hash32_perf(benchmark, hash_bencher):
    hash_bencher(benchmark, pyhash.wy_32, 2032615721)


@pytest.mark.benchmark(group='hash64', disable_gc=True)
def test_wy_hash64_perf(benchmark, hash_bencher):
    hash_bencher(benchmark, pyhash.wy_64, 16560810041235762008)
