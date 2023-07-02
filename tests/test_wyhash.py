import pytest

import pyhash


def test_wy_32(hash_tester):
    hash_tester(
        hasher_type=pyhash.wy_32,
        bytes_hash=3257032231,
        seed_hash=4286430599,
        unicode_hash=213393459,
    )


def test_wy_64(hash_tester):
    hash_tester(
        hasher_type=pyhash.wy_64,
        bytes_hash=10062657028113479704,
        seed_hash=7566643489967525642,
        unicode_hash=9309557217718758546,
    )


@pytest.mark.benchmark(group="hash32", disable_gc=True)
def test_wy_hash32_perf(benchmark, hash_bencher):
    hash_bencher(benchmark, pyhash.wy_32, 2032615721)


@pytest.mark.benchmark(group="hash64", disable_gc=True)
def test_wy_hash64_perf(benchmark, hash_bencher):
    hash_bencher(benchmark, pyhash.wy_64, 5311500416313190714)
