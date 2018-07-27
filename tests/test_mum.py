import pytest

import pyhash


def test_mum64(hash_tester):
    hash_tester(hasher_type=pyhash.mum_64,
                bytes_hash=8715813407503360407,
                seed_hash=1160173209250992409,
                unicode_hash=16548684777514844522)


@pytest.mark.benchmark(group='hash64', disable_gc=True)
def test_mum_hash3_perf(benchmark, hash_bencher):
    hash_bencher(benchmark, pyhash.mum_64, 5704960907050105809)
