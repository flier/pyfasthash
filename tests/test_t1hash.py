import pytest

import pyhash


def test_t1ha2_atonce(hash_tester):
    hash_tester(hasher_type=pyhash.t1ha2_atonce,
                bytes_hash=11576265462006865275,
                seed_hash=9383269742356701786,
                unicode_hash=10647421798084574537)


def test_t1ha2_atonce128(hash_tester):
    hash_tester(hasher_type=pyhash.t1ha2_atonce128,
                bytes_hash=111289500776795915835395169778666467727,
                seed_hash=86921791256626059574547663004160252269,
                unicode_hash=265347458704473149675948059533744938455)


def test_t1ha1_le(hash_tester):
    hash_tester(hasher_type=pyhash.t1ha1_le,
                bytes_hash=10616215634819799576,
                seed_hash=6056749954736269874,
                unicode_hash=18194209408316694427)


def test_t1ha1_be(hash_tester):
    hash_tester(hasher_type=pyhash.t1ha1_be,
                bytes_hash=7811195108528602730,
                seed_hash=16139937605191117723,
                unicode_hash=4258761466277697735)


def test_t1ha0(hash_tester):
    hash_tester(hasher_type=pyhash.t1ha0,
                bytes_hash=11576265462006865275,
                seed_hash=9383269742356701786,
                unicode_hash=10647421798084574537)


@pytest.mark.benchmark(group='hash64', disable_gc=True)
def test_t1ha2_perf(benchmark, hash_bencher):
    hash_bencher(benchmark, pyhash.t1ha2, 17171225769172857249)


@pytest.mark.benchmark(group='hash128', disable_gc=True)
def test_t1ha2_128_perf(benchmark, hash_bencher):
    hash_bencher(benchmark, pyhash.t1ha2_128,
                 263168739977411690410017013291704716368)


@pytest.mark.benchmark(group='hash64', disable_gc=True)
def test_t1ha1_perf(benchmark, hash_bencher):
    hash_bencher(benchmark, pyhash.t1ha1, 6501324028002495964)


@pytest.mark.benchmark(group='hash64', disable_gc=True)
def test_t1ha0_perf(benchmark, hash_bencher):
    hash_bencher(benchmark, pyhash.t1ha0, [6970451072221114646, 13811823941710697992])