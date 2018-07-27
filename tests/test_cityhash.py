import pytest

import pyhash


def test_city_32(hash_tester):
    hash_tester(hasher_type=pyhash.city_32,
                bytes_hash=1633095781,
                seed_hash=3687200064,
                unicode_hash=3574089775)


def test_city_64(hash_tester):
    hash_tester(hasher_type=pyhash.city_64,
                bytes_hash=17703940110308125106,
                seed_hash=8806864191580960558,
                unicode_hash=7557950076747784205)


def test_city_128(hash_tester):
    hash_tester(hasher_type=pyhash.city_128,
                bytes_hash=195179989828428219998331619914059544201,
                seed_hash=206755929755292977387372217469167977636,
                unicode_hash=211596129097514838244042408160146499227)


def test_city_crc128(hash_tester):
    hash_tester(hasher_type=pyhash.city_crc_128,
                bytes_hash=195179989828428219998331619914059544201,
                seed_hash=206755929755292977387372217469167977636,
                unicode_hash=211596129097514838244042408160146499227)


def test_city_crc256(fingerprint_tester):
    fingerprint_tester(fingerprinter_type=pyhash.city_fingerprint_256,
                       bytes_fingerprint=43374127706338803100025155483422426900760284308948611519881759972455588549698,
                       unicode_fingerprint=106103693879923228777324437129892107726572355760220840777228701216663718411687)


@pytest.mark.benchmark(group='hash32', disable_gc=True)
def test_city_hash32_perf(benchmark, hash_bencher):
    hash_bencher(benchmark, pyhash.city_32, 2824210825)


@pytest.mark.benchmark(group='hash64', disable_gc=True)
def test_city_hash64_perf(benchmark, hash_bencher):
    hash_bencher(benchmark, pyhash.city_64, 894299094737143437)


@pytest.mark.benchmark(group='hash128', disable_gc=True)
def test_city_hash128_perf(benchmark, hash_bencher):
    hash_bencher(benchmark, pyhash.city_128,
                 254849646208103091500548480943427727100)


@pytest.mark.benchmark(group='hash128', disable_gc=True)
def test_city_hash_crc128_perf(benchmark, hash_bencher):
    hash_bencher(benchmark, pyhash.city_crc_128,
                 254849646208103091500548480943427727100)
