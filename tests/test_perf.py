import pytest

import pyhash


@pytest.mark.benchmark(group='hash32', disable_gc=True)
def test_fnv1_32_perf(benchmark, hash_bencher):
    hash_bencher(benchmark, pyhash.fnv1_32, 4117514240)


@pytest.mark.benchmark(group='hash32', disable_gc=True)
def test_fnv1a_32_perf(benchmark, hash_bencher):
    hash_bencher(benchmark, pyhash.fnv1a_32, 1500862464)


@pytest.mark.benchmark(group='hash64', disable_gc=True)
def test_fnv1_64_perf(benchmark, hash_bencher):
    hash_bencher(benchmark, pyhash.fnv1_64, 487086381785722880)


@pytest.mark.benchmark(group='hash64', disable_gc=True)
def test_fnv1a_64_perf(benchmark, hash_bencher):
    hash_bencher(benchmark, pyhash.fnv1a_64, 13917847256464560128)


@pytest.mark.benchmark(group='hash32', disable_gc=True)
def test_murmur_hash1_32_perf(benchmark, hash_bencher):
    hash_bencher(benchmark, pyhash.murmur1_32, 3043957486)


@pytest.mark.benchmark(group='hash32', disable_gc=True)
def test_murmur_hash1_aligned_32_perf(benchmark, hash_bencher):
    hash_bencher(benchmark, pyhash.murmur1_aligned_32, 3043957486)


@pytest.mark.benchmark(group='hash32', disable_gc=True)
def test_murmur_hash2_32_perf(benchmark, hash_bencher):
    hash_bencher(benchmark, pyhash.murmur2_32, 2373126550)


@pytest.mark.benchmark(group='hash32', disable_gc=True)
def test_murmur_hash2a_32_perf(benchmark, hash_bencher):
    hash_bencher(benchmark, pyhash.murmur2a_32, 178525084)


@pytest.mark.benchmark(group='hash32', disable_gc=True)
def test_murmur_hash2_aligned_32_perf(benchmark, hash_bencher):
    hash_bencher(benchmark, pyhash.murmur2_aligned_32, 2373126550)


@pytest.mark.benchmark(group='hash32', disable_gc=True)
def test_murmur_hash2_neutral_32_perf(benchmark, hash_bencher):
    hash_bencher(benchmark, pyhash.murmur2_neutral_32, 2373126550)


@pytest.mark.benchmark(group='hash64', disable_gc=True)
def test_murmur_hash2_x64_64a_perf(benchmark, hash_bencher):
    hash_bencher(benchmark, pyhash.murmur2_x64_64a, 12604435678857905857)


@pytest.mark.benchmark(group='hash64', disable_gc=True)
def test_murmur_hash2_x86_64b_perf(benchmark, hash_bencher):
    hash_bencher(benchmark, pyhash.murmur2_x86_64b, 3759496224018757553)


@pytest.mark.benchmark(group='hash32', disable_gc=True)
def test_murmur_hash3_32_perf(benchmark, hash_bencher):
    hash_bencher(benchmark, pyhash.murmur3_32, 3825864278)


@pytest.mark.benchmark(group='hash128', disable_gc=True)
def test_murmur_hash3_x86_128_perf(benchmark, hash_bencher):
    hash_bencher(benchmark, pyhash.murmur3_x86_128,
                 97431559281111809997269275467939498127)


@pytest.mark.benchmark(group='hash128', disable_gc=True)
def test_murmur_hash3_x64_128_perf(benchmark, hash_bencher):
    hash_bencher(benchmark, pyhash.murmur3_x64_128,
                 149984839147466660491291446859193586361)


@pytest.mark.benchmark(group='hash32', disable_gc=True)
def test_lookup3_perf(benchmark, hash_bencher):
    hash_bencher(benchmark, pyhash.lookup3, 3792570419)


@pytest.mark.benchmark(group='hash32', disable_gc=True)
def test_super_fast_hash_perf(benchmark, hash_bencher):
    hash_bencher(benchmark, pyhash.super_fast_hash, 2804200527)


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


@pytest.mark.benchmark(group='hash32', disable_gc=True)
def test_spooky_hash32_perf(benchmark, hash_bencher):
    hash_bencher(benchmark, pyhash.spooky_32, 2489700128)


@pytest.mark.benchmark(group='hash64', disable_gc=True)
def test_spooky_hash64_perf(benchmark, hash_bencher):
    hash_bencher(benchmark, pyhash.spooky_64, 8714752859576848160)


@pytest.mark.benchmark(group='hash128', disable_gc=True)
def test_spooky_hash128_perf(benchmark, hash_bencher):
    hash_bencher(benchmark, pyhash.spooky_128,
                 69975394272542483818884528997491134240)


@pytest.mark.benchmark(group='hash32', disable_gc=True)
def test_farm_hash32_perf(benchmark, hash_bencher):
    hash_bencher(benchmark, pyhash.farm_32, 3977123615)


@pytest.mark.benchmark(group='hash64', disable_gc=True)
def test_farm_hash64_perf(benchmark, hash_bencher):
    hash_bencher(benchmark, pyhash.farm_64, 5291657088564336415)


@pytest.mark.benchmark(group='hash128', disable_gc=True)
def test_farm_hash128_perf(benchmark, hash_bencher):
    hash_bencher(benchmark, pyhash.farm_128,
                 2614362402971166945389138950146702896)


@pytest.mark.benchmark(group='hash64', disable_gc=True)
def test_metro_hash64_1_perf(benchmark, hash_bencher):
    hash_bencher(benchmark, pyhash.metro_64_1, 6897098198286496634)


@pytest.mark.benchmark(group='hash128', disable_gc=True)
def test_metro_hash128_1_perf(benchmark, hash_bencher):
    hash_bencher(benchmark, pyhash.metro_128_1,
                 284089860902754045805586152203438670446)


@pytest.mark.benchmark(group='hash64', disable_gc=True)
def test_metro_hash64_2_perf(benchmark, hash_bencher):
    hash_bencher(benchmark, pyhash.metro_64_2, 9928248983045338067)


@pytest.mark.benchmark(group='hash128', disable_gc=True)
def test_metro_hash128_2_perf(benchmark, hash_bencher):
    hash_bencher(benchmark, pyhash.metro_128_2,
                 298961466275459716490100873977629041349)


@pytest.mark.benchmark(group='hash64', disable_gc=True)
def test_metro_hash_crc64_1_perf(benchmark, hash_bencher):
    hash_bencher(benchmark, pyhash.metro_crc_64_1, 15625740387403976237)


@pytest.mark.benchmark(group='hash128', disable_gc=True)
def test_metro_hash_crc128_1_perf(benchmark, hash_bencher):
    hash_bencher(benchmark, pyhash.metro_crc_128_1,
                 221795002586229010982769362009963170208)


@pytest.mark.benchmark(group='hash64', disable_gc=True)
def test_metro_hash_crc64_2_perf(benchmark, hash_bencher):
    hash_bencher(benchmark, pyhash.metro_crc_64_2, 9313388757605283934)


@pytest.mark.benchmark(group='hash128', disable_gc=True)
def test_metro_hash_crc128_2_perf(benchmark, hash_bencher):
    hash_bencher(benchmark, pyhash.metro_crc_128_2,
                 319940271611864595969873671463832146628)


@pytest.mark.benchmark(group='hash64', disable_gc=True)
def test_mum_hash3_perf(benchmark, hash_bencher):
    hash_bencher(benchmark, pyhash.mum_64, 5704960907050105809)


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
    hash_bencher(benchmark, pyhash.t1ha0, 6970451072221114646)


@pytest.mark.benchmark(group='hash32', disable_gc=True)
def test_xx_hash32_perf(benchmark, hash_bencher):
    hash_bencher(benchmark, pyhash.xx_32, 1497633363)


@pytest.mark.benchmark(group='hash64', disable_gc=True)
def test_xx_hash64_perf(benchmark, hash_bencher):
    hash_bencher(benchmark, pyhash.xx_64, 2282408585429094475)
