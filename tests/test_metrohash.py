import pytest

import pyhash


def test_metro_64_1(hash_tester):
    hash_tester(
        hasher_type=pyhash.metro_64_1,
        bytes_hash=7555593383206836236,
        seed_hash=9613011798576657330,
        unicode_hash=5634638029758084150,
    )


def test_metro_128_1(hash_tester):
    hash_tester(
        hasher_type=pyhash.metro_128_1,
        bytes_hash=310240039238111093048322555259813357218,
        seed_hash=330324289553816260191102680044286377986,
        unicode_hash=160639312567243412360084738183177128736,
    )


def test_metro_64_2(hash_tester):
    hash_tester(
        hasher_type=pyhash.metro_64_2,
        bytes_hash=13328239478646503906,
        seed_hash=16521803336796657060,
        unicode_hash=5992985172783395072,
    )


def test_metro_128_2(hash_tester):
    hash_tester(
        hasher_type=pyhash.metro_128_2,
        bytes_hash=308979041176504703647272401075625691044,
        seed_hash=156408679042779357342816971045969684594,
        unicode_hash=169904568621124891123383613748925830588,
    )


def test_metro_Crc64_1(hash_tester):
    hash_tester(
        hasher_type=pyhash.metro_crc_64_1,
        bytes_hash=6872506084457499713,
        seed_hash=14064239385324957326,
        unicode_hash=5634638029758084150,
    )


def test_metro_Crc128_1(hash_tester):
    hash_tester(
        hasher_type=pyhash.metro_crc_128_1,
        bytes_hash=44856800307026421677415827141042094245,
        seed_hash=199990471895323666720887863107514038076,
        unicode_hash=53052528140813423722778028047086277728,
    )


def test_metro_Crc64_2(hash_tester):
    hash_tester(
        hasher_type=pyhash.metro_crc_64_2,
        bytes_hash=9168163846307153532,
        seed_hash=11235719994915751828,
        unicode_hash=15697829093445668111,
    )


def test_metro_Crc128_2(hash_tester):
    hash_tester(
        hasher_type=pyhash.metro_crc_128_2,
        bytes_hash=29039398407115405218669555123781288008,
        seed_hash=26197404070933777589488526163359489061,
        unicode_hash=136212167639765185451107230087801381416,
    )


@pytest.mark.benchmark(group="hash64", disable_gc=True)
def test_metro_hash64_1_perf(benchmark, hash_bencher):
    hash_bencher(benchmark, pyhash.metro_64_1, 6897098198286496634)


@pytest.mark.benchmark(group="hash128", disable_gc=True)
def test_metro_hash128_1_perf(benchmark, hash_bencher):
    hash_bencher(benchmark, pyhash.metro_128_1, 284089860902754045805586152203438670446)


@pytest.mark.benchmark(group="hash64", disable_gc=True)
def test_metro_hash64_2_perf(benchmark, hash_bencher):
    hash_bencher(benchmark, pyhash.metro_64_2, 9928248983045338067)


@pytest.mark.benchmark(group="hash128", disable_gc=True)
def test_metro_hash128_2_perf(benchmark, hash_bencher):
    hash_bencher(benchmark, pyhash.metro_128_2, 298961466275459716490100873977629041349)


@pytest.mark.benchmark(group="hash64", disable_gc=True)
def test_metro_hash_crc64_1_perf(benchmark, hash_bencher):
    hash_bencher(benchmark, pyhash.metro_crc_64_1, 15625740387403976237)


@pytest.mark.benchmark(group="hash128", disable_gc=True)
def test_metro_hash_crc128_1_perf(benchmark, hash_bencher):
    hash_bencher(
        benchmark, pyhash.metro_crc_128_1, 221795002586229010982769362009963170208
    )


@pytest.mark.benchmark(group="hash64", disable_gc=True)
def test_metro_hash_crc64_2_perf(benchmark, hash_bencher):
    hash_bencher(benchmark, pyhash.metro_crc_64_2, 9313388757605283934)


@pytest.mark.benchmark(group="hash128", disable_gc=True)
def test_metro_hash_crc128_2_perf(benchmark, hash_bencher):
    hash_bencher(
        benchmark, pyhash.metro_crc_128_2, 319940271611864595969873671463832146628
    )
