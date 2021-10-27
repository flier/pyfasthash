import pytest

import pyhash


def test_halftime_64(hash_tester):
    hash_tester(hasher_type=pyhash.halftime_64,
                bytes_hash=3604972081320839471,
                seed_hash=3471423249075386634,
                unicode_hash=7775058808590938809)


@pytest.mark.skipif(not pyhash.build_with_int128, reason="requires int128 support")
def test_halftime_128(hash_tester):
    hash_tester(hasher_type=pyhash.halftime_128,
                bytes_hash=1789925655390500234,
                seed_hash=1764839430745045589,
                unicode_hash=13450828806325116760)


@pytest.mark.skipif(not pyhash.build_with_int128, reason="requires int128 support")
def test_halftime_256(hash_tester):
    hash_tester(hasher_type=pyhash.halftime_256,
                bytes_hash=7217693443645459132,
                seed_hash=2352364554368405048,
                unicode_hash=3229181546426569946)


@pytest.mark.skipif(not pyhash.build_with_int128, reason="requires int128 support")
def test_halftime_512(hash_tester):
    hash_tester(hasher_type=pyhash.halftime_512,
                bytes_hash=11860383299129413215,
                seed_hash=14752946495531348805,
                unicode_hash=11130042267740264375)


@pytest.mark.benchmark(group='hash64', disable_gc=True)
def test_halftime_hash64_perf(benchmark, hash_bencher):
    hash_bencher(benchmark, pyhash.halftime_64, 16234903152174643107)


@pytest.mark.skipif(not pyhash.build_with_int128, reason="requires int128 support")
@pytest.mark.benchmark(group='hash128', disable_gc=True)
def test_halftime_hash128_perf(benchmark, hash_bencher):
    hash_bencher(benchmark, pyhash.halftime_128, 17751672293671634095)


@pytest.mark.skipif(not pyhash.build_with_int128, reason="requires int128 support")
@pytest.mark.benchmark(group='hash256', disable_gc=True)
def test_halftime_hash256_perf(benchmark, hash_bencher):
    hash_bencher(benchmark, pyhash.halftime_256, 17104156079727854476)


@pytest.mark.skipif(not pyhash.build_with_int128, reason="requires int128 support")
@pytest.mark.benchmark(group='hash512', disable_gc=True)
def test_halftime_hash512_perf(benchmark, hash_bencher):
    hash_bencher(benchmark, pyhash.halftime_512, 4920030102686204611)
