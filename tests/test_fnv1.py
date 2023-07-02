import pytest

import pyhash


def test_fnv1_32(hash_tester):
    hash_tester(
        hasher_type=pyhash.fnv1_32,
        bytes_hash=3698262380,
        seed_hash=660137056,
        unicode_hash=3910690890,
    )


def test_fnv1a_32(hash_tester):
    hash_tester(
        hasher_type=pyhash.fnv1a_32,
        bytes_hash=1858026756,
        seed_hash=1357873952,
        unicode_hash=996945022,
    )


def test_fnv1_64(hash_tester):
    hash_tester(
        hasher_type=pyhash.fnv1_64,
        bytes_hash=17151984479173897804,
        seed_hash=6349570372626520864,
        unicode_hash=14017453969697934794,
    )


def test_fnv1a_64(hash_tester):
    hash_tester(
        hasher_type=pyhash.fnv1a_64,
        bytes_hash=11830222609977404196,
        seed_hash=8858165303110309728,
        unicode_hash=14494269412771327550,
    )


@pytest.mark.benchmark(group="hash32", disable_gc=True)
def test_fnv1_32_perf(benchmark, hash_bencher):
    hash_bencher(benchmark, pyhash.fnv1_32, 4117514240)


@pytest.mark.benchmark(group="hash32", disable_gc=True)
def test_fnv1a_32_perf(benchmark, hash_bencher):
    hash_bencher(benchmark, pyhash.fnv1a_32, 1500862464)


@pytest.mark.benchmark(group="hash64", disable_gc=True)
def test_fnv1_64_perf(benchmark, hash_bencher):
    hash_bencher(benchmark, pyhash.fnv1_64, 487086381785722880)


@pytest.mark.benchmark(group="hash64", disable_gc=True)
def test_fnv1a_64_perf(benchmark, hash_bencher):
    hash_bencher(benchmark, pyhash.fnv1a_64, 13917847256464560128)
