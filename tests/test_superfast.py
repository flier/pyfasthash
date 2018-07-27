import pytest

import pyhash


def test_lookup3(hash_tester):
    hash_tester(hasher_type=pyhash.super_fast_hash,
                bytes_hash=942683319,
                seed_hash=777359542,
                unicode_hash=1430748046)


@pytest.mark.benchmark(group='hash32', disable_gc=True)
def test_super_fast_hash_perf(benchmark, hash_bencher):
    hash_bencher(benchmark, pyhash.super_fast_hash, 2804200527)
