import pytest

import pyhash


def test_spooky_v1_32(hash_tester):
    hash_tester(
        hasher_type=pyhash.spooky_v1_32,
        bytes_hash=1882037601,
        seed_hash=1324274298,
        unicode_hash=2977967976,
    )


def test_spooky_v1_64(hash_tester):
    hash_tester(
        hasher_type=pyhash.spooky_v1_64,
        bytes_hash=10130480990056717665,
        seed_hash=1598355329892273278,
        unicode_hash=4093159241144086376,
    )


def test_spooky_v1_128(hash_tester):
    hash_tester(
        hasher_type=pyhash.spooky_v1_128,
        bytes_hash=241061513486538422840128476001680072033,
        seed_hash=197773926455441667640915872760094474199,
        unicode_hash=207554373952009549684886824908954283880,
    )


def test_spooky_v2_32(hash_tester):
    hash_tester(
        hasher_type=pyhash.spooky_v2_32,
        bytes_hash=1882037601,
        seed_hash=1324274298,
        unicode_hash=2977967976,
    )


def test_spooky_v2_64(hash_tester):
    hash_tester(
        hasher_type=pyhash.spooky_v2_64,
        bytes_hash=10130480990056717665,
        seed_hash=1598355329892273278,
        unicode_hash=4093159241144086376,
    )


def test_spooky_v2_128(hash_tester):
    hash_tester(
        hasher_type=pyhash.spooky_v2_128,
        bytes_hash=241061513486538422840128476001680072033,
        seed_hash=197773926455441667640915872760094474199,
        unicode_hash=207554373952009549684886824908954283880,
    )


@pytest.mark.benchmark(group="hash32", disable_gc=True)
def test_spooky_v1_hash32_perf(benchmark, hash_bencher):
    hash_bencher(benchmark, pyhash.spooky_v1_32, 2489700128)


@pytest.mark.benchmark(group="hash64", disable_gc=True)
def test_spooky_v1_hash64_perf(benchmark, hash_bencher):
    hash_bencher(benchmark, pyhash.spooky_v1_64, 8714752859576848160)


@pytest.mark.benchmark(group="hash128", disable_gc=True)
def test_spooky_v1_hash128_perf(benchmark, hash_bencher):
    hash_bencher(
        benchmark, pyhash.spooky_v1_128, 69975394272542483818884528997491134240
    )


@pytest.mark.benchmark(group="hash32", disable_gc=True)
def test_spooky_v2_hash32_perf(benchmark, hash_bencher):
    hash_bencher(benchmark, pyhash.spooky_v2_32, 2489700128)


@pytest.mark.benchmark(group="hash64", disable_gc=True)
def test_spooky_v2_hash64_perf(benchmark, hash_bencher):
    hash_bencher(benchmark, pyhash.spooky_v2_64, 8714752859576848160)


@pytest.mark.benchmark(group="hash128", disable_gc=True)
def test_spooky_v2_hash128_perf(benchmark, hash_bencher):
    hash_bencher(
        benchmark, pyhash.spooky_v2_128, 69975394272542483818884528997491134240
    )
