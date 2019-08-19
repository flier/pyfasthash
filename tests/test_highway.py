import pytest

import pyhash


def test_highway_64(hash_tester):
    hash_tester(hasher_type=pyhash.highway_64,
                bytes_hash=10478741295963822880,
                seed_hash=10160071405899912585,
                unicode_hash=12146505054120333431)


@pytest.mark.skipif(not pyhash.build_with_int128, reason="requires int128 support")
def test_highway_128(hash_tester):
    hash_tester(hasher_type=pyhash.highway_128,
                bytes_hash=205029416337089142837388334492957817459,
                seed_hash=[131606380489010322043134332560055467821,
                           49445702356125343135034790375575615434],
                unicode_hash=106097529843409528118081989705354610918)


@pytest.mark.skipif(not pyhash.build_with_int128, reason="requires int128 support")
def test_highway_256(hash_tester):
    hash_tester(hasher_type=pyhash.highway_256,
                bytes_hash=81695253358482264846640254134214061745359108833184802399504321540179680608337,
                seed_hash=38580172915253542762608044587659714789132854339955812293479199758918380945040,
                unicode_hash=82825971135523989855392223965598679755378386501396024912896994597279835575349)


@pytest.mark.benchmark(group='hash64', disable_gc=True)
def bench_highway_64(benchmark, hash_bencher):
    hash_bencher(benchmark, pyhash.highway_64, 17171225769172857249)


@pytest.mark.skipif(not pyhash.build_with_int128, reason="requires int128 support")
@pytest.mark.benchmark(group='hash128', disable_gc=True)
def bench_highway_128(benchmark, hash_bencher):
    hash_bencher(benchmark, pyhash.highway_128,
                 263168739977411690410017013291704716368)


@pytest.mark.skipif(not pyhash.build_with_int128, reason="requires int128 support")
@pytest.mark.benchmark(group='hash128', disable_gc=True)
def bench_highway_256(benchmark, hash_bencher):
    hash_bencher(benchmark, pyhash.highway_256,
                 263168739977411690410017013291704716368)
