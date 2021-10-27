import os

import pytest

import pyhash


def test_mum64(hash_tester, is_msvc):
    hash_tester(hasher_type=pyhash.mum_64,
                bytes_hash=12122843130624056202 if is_msvc else 8715813407503360407,
                seed_hash=14905784849636620642 if is_msvc else 1160173209250992409,
                unicode_hash=366515711009433586 if is_msvc else 16548684777514844522)


@pytest.mark.benchmark(group='hash64', disable_gc=True)
def test_mum_hash3_perf(benchmark, hash_bencher, is_msvc):
    hash_bencher(benchmark, pyhash.mum_64,
                 16713191835145177100 if is_msvc else 5704960907050105809)
