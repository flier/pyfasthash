import pytest

import pyhash


def test_farm_32(test_data):
    data, udata = test_data
    hasher = pyhash.farm_32()

    h1 = hasher(data)
    h2 = hasher(data, seed=123)
    h3 = hasher(udata)

    assert h1 != 0
    assert h2 != 0
    assert h3 != 0
    assert h1 != h2
    assert h1 != h3
    assert h2 != h3


def test_farm_64(hash_tester):
    hash_tester(
        hasher_type=pyhash.farm_64,
        bytes_hash=8581389452482819506,
        seed_hash=10025340881295800991,
        unicode_hash=7274603073818924232,
    )


def test_farm_128(hash_tester):
    hash_tester(
        hasher_type=pyhash.farm_128,
        bytes_hash=334882099032867325754781607143811124132,
        seed_hash=187628921277009896235568325208309914427,
        unicode_hash=251662992469041432568516527017706898625,
    )


def test_farm_fingerprint_32(fingerprint_tester):
    fingerprint_tester(
        fingerprinter_type=pyhash.farm_fingerprint_32,
        bytes_fingerprint=1633095781,
        unicode_fingerprint=3574089775,
    )


def test_farm_fingerprint_64(fingerprint_tester):
    fingerprint_tester(
        fingerprinter_type=pyhash.farm_fingerprint_64,
        bytes_fingerprint=8581389452482819506,
        unicode_fingerprint=7274603073818924232,
    )


def test_farm_fingerprint_128(fingerprint_tester):
    fingerprint_tester(
        fingerprinter_type=pyhash.farm_fingerprint_128,
        bytes_fingerprint=334882099032867325754781607143811124132,
        unicode_fingerprint=251662992469041432568516527017706898625,
    )


@pytest.mark.benchmark(group="hash32", disable_gc=True)
def test_farm_hash32_perf(benchmark, hash_bencher):
    hash_bencher(benchmark, pyhash.farm_32, [3712697123, 3977123615])


@pytest.mark.benchmark(group="hash64", disable_gc=True)
def test_farm_hash64_perf(benchmark, hash_bencher):
    hash_bencher(benchmark, pyhash.farm_64, 5291657088564336415)


@pytest.mark.benchmark(group="hash128", disable_gc=True)
def test_farm_hash128_perf(benchmark, hash_bencher):
    hash_bencher(benchmark, pyhash.farm_128, 2614362402971166945389138950146702896)
