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


@pytest.mark.benchmark(group='hash32', disable_gc=True)
def test_spooky_hash32_perf(benchmark, hash_bencher):
    hash_bencher(benchmark, pyhash.spooky_32, 2489700128)


@pytest.mark.benchmark(group='hash64', disable_gc=True)
def test_spooky_hash64_perf(benchmark, hash_bencher):
    hash_bencher(benchmark, pyhash.spooky_64, 8714752859576848160)


@pytest.mark.benchmark(group='hash128', disable_gc=True)
def test_spooky_hash128_perf(benchmark, hash_bencher):
    hash_bencher(benchmark, pyhash.spooky_128,
                 69975394272542483818884528997491134240)
