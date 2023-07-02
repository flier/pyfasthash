import pytest

import pyhash


def test_xx_32(hash_tester):
    hash_tester(
        hasher_type=pyhash.xx_32,
        bytes_hash=1042293711,
        seed_hash=1018767936,
        unicode_hash=2783988247,
    )


def test_xx_64(hash_tester):
    hash_tester(
        hasher_type=pyhash.xx_64,
        bytes_hash=5754696928334414137,
        seed_hash=12934826212537126916,
        unicode_hash=16125048496228390453,
    )


def test_xxh3_64(hash_tester):
    hash_tester(
        hasher_type=pyhash.xxh3_64,
        bytes_hash=11441948532827618368,
        seed_hash=2089348107868048054,
        unicode_hash=16570491819903731716,
    )


def test_xxh3_128(hash_tester):
    hash_tester(
        hasher_type=pyhash.xxh3_128,
        bytes_hash=144184260470930790206475339950959648696,
        seed_hash=245340701302628892366188236529209798014,
        unicode_hash=178697977782819640141202674788096098003,
    )


@pytest.mark.benchmark(group="hash32", disable_gc=True)
def test_xx_hash32_perf(benchmark, hash_bencher):
    hash_bencher(benchmark, pyhash.xx_32, 1497633363)


@pytest.mark.benchmark(group="hash64", disable_gc=True)
def test_xx_hash64_perf(benchmark, hash_bencher):
    hash_bencher(benchmark, pyhash.xx_64, 2282408585429094475)


@pytest.mark.benchmark(group="hash64", disable_gc=True)
def test_xxh3_hash64_perf(benchmark, hash_bencher):
    hash_bencher(benchmark, pyhash.xxh3_64, 10666956326096416113)


@pytest.mark.benchmark(group="hash128", disable_gc=True)
def test_xxh3_hash128_perf(benchmark, hash_bencher):
    hash_bencher(benchmark, pyhash.xxh3_128, 321635069348597727998765129269811424625)
