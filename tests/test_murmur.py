import pytest

import pyhash


def test_murmur1_32(hash_tester):
    hash_tester(
        hasher_type=pyhash.murmur1_32,
        bytes_hash=1706635965,
        seed_hash=1637637239,
        unicode_hash=2296970802,
    )


def test_murmur1_aligned_32(hash_tester):
    hash_tester(
        hasher_type=pyhash.murmur1_aligned_32,
        bytes_hash=1706635965,
        seed_hash=1637637239,
        unicode_hash=2296970802,
    )


def test_murmur2_32(hash_tester):
    hash_tester(
        hasher_type=pyhash.murmur2_32,
        bytes_hash=403862830,
        seed_hash=1257009171,
        unicode_hash=2308212514,
    )


def test_murmur2a_32(hash_tester):
    hash_tester(
        hasher_type=pyhash.murmur2a_32,
        bytes_hash=1026673864,
        seed_hash=3640713775,
        unicode_hash=3710634486,
    )


def test_murmur2_aligned32(hash_tester):
    hash_tester(
        hasher_type=pyhash.murmur2_aligned_32,
        bytes_hash=403862830,
        seed_hash=1257009171,
        unicode_hash=2308212514,
    )


def test_murmur2_neutral32(hash_tester):
    hash_tester(
        hasher_type=pyhash.murmur2_neutral_32,
        bytes_hash=403862830,
        seed_hash=1257009171,
        unicode_hash=2308212514,
    )


def test_murmur2_x64_64a(hash_tester):
    hash_tester(
        hasher_type=pyhash.murmur2_x64_64a,
        bytes_hash=3407684658384555107,
        seed_hash=14278059344916754999,
        unicode_hash=9820020607534352415,
    )


def test_murmur2_x86_64b(hash_tester):
    hash_tester(
        hasher_type=pyhash.murmur2_x86_64b,
        bytes_hash=1560774255606158893,
        seed_hash=11567531768634065834,
        unicode_hash=7104676830630207180,
    )


def test_murmur3_32(hash_tester):
    hash_tester(
        hasher_type=pyhash.murmur3_32,
        bytes_hash=3127628307,
        seed_hash=1973649836,
        unicode_hash=1351191292,
    )


def test_murmur3_x86_128(hash_tester):
    hash_tester(
        hasher_type=pyhash.murmur3_x86_128,
        bytes_hash=113049230771270950235709929058346397488,
        seed_hash=201730919445129814667855021331871906456,
        unicode_hash=34467989874860051826961972957664456325,
    )


def test_murmur3_x64_128(hash_tester):
    hash_tester(
        hasher_type=pyhash.murmur3_x64_128,
        bytes_hash=204797213367049729698754624420042367389,
        seed_hash=25000065729391260169145522623652811022,
        unicode_hash=301054382688326301269845371608405900524,
    )


@pytest.mark.benchmark(group="hash32", disable_gc=True)
def test_murmur_hash1_32_perf(benchmark, hash_bencher):
    hash_bencher(benchmark, pyhash.murmur1_32, 3043957486)


@pytest.mark.benchmark(group="hash32", disable_gc=True)
def test_murmur_hash1_aligned_32_perf(benchmark, hash_bencher):
    hash_bencher(benchmark, pyhash.murmur1_aligned_32, 3043957486)


@pytest.mark.benchmark(group="hash32", disable_gc=True)
def test_murmur_hash2_32_perf(benchmark, hash_bencher):
    hash_bencher(benchmark, pyhash.murmur2_32, 2373126550)


@pytest.mark.benchmark(group="hash32", disable_gc=True)
def test_murmur_hash2a_32_perf(benchmark, hash_bencher):
    hash_bencher(benchmark, pyhash.murmur2a_32, 178525084)


@pytest.mark.benchmark(group="hash32", disable_gc=True)
def test_murmur_hash2_aligned_32_perf(benchmark, hash_bencher):
    hash_bencher(benchmark, pyhash.murmur2_aligned_32, 2373126550)


@pytest.mark.benchmark(group="hash32", disable_gc=True)
def test_murmur_hash2_neutral_32_perf(benchmark, hash_bencher):
    hash_bencher(benchmark, pyhash.murmur2_neutral_32, 2373126550)


@pytest.mark.benchmark(group="hash64", disable_gc=True)
def test_murmur_hash2_x64_64a_perf(benchmark, hash_bencher):
    hash_bencher(benchmark, pyhash.murmur2_x64_64a, 12604435678857905857)


@pytest.mark.benchmark(group="hash64", disable_gc=True)
def test_murmur_hash2_x86_64b_perf(benchmark, hash_bencher):
    hash_bencher(benchmark, pyhash.murmur2_x86_64b, 3759496224018757553)


@pytest.mark.benchmark(group="hash32", disable_gc=True)
def test_murmur_hash3_32_perf(benchmark, hash_bencher):
    hash_bencher(benchmark, pyhash.murmur3_32, 3825864278)


@pytest.mark.benchmark(group="hash128", disable_gc=True)
def test_murmur_hash3_x86_128_perf(benchmark, hash_bencher):
    hash_bencher(
        benchmark, pyhash.murmur3_x86_128, 97431559281111809997269275467939498127
    )


@pytest.mark.benchmark(group="hash128", disable_gc=True)
def test_murmur_hash3_x64_128_perf(benchmark, hash_bencher):
    hash_bencher(
        benchmark, pyhash.murmur3_x64_128, 149984839147466660491291446859193586361
    )
