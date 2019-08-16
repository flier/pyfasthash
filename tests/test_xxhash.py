import pytest

import pyhash


def test_xx_32(hash_tester):
    hash_tester(hasher_type=pyhash.xx_32,
                bytes_hash=1042293711,
                seed_hash=1018767936,
                unicode_hash=2783988247)


def test_xx_64(hash_tester):
    hash_tester(hasher_type=pyhash.xx_64,
                bytes_hash=5754696928334414137,
                seed_hash=12934826212537126916,
                unicode_hash=16125048496228390453)


def test_xxh3_64(hash_tester):
    hash_tester(hasher_type=pyhash.xxh3_64,
                bytes_hash=10414627905623201439,
                seed_hash=16911555820549409221,
                unicode_hash=6799411566997318536)


@pytest.mark.skipif(not pyhash.build_with_int128, reason="requires int128 support")
def test_xxh3_128(hash_tester):
    hash_tester(hasher_type=pyhash.xxh3_128,
                bytes_hash=36091986456711630655561101449441744543,
                seed_hash=119421902396782338937329176477348497861,
                unicode_hash=217308309488429273506450508431355718536)


@pytest.mark.benchmark(group='hash32', disable_gc=True)
def test_xx_hash32_perf(benchmark, hash_bencher):
    hash_bencher(benchmark, pyhash.xx_32, 1497633363)


@pytest.mark.benchmark(group='hash64', disable_gc=True)
def test_xx_hash64_perf(benchmark, hash_bencher):
    hash_bencher(benchmark, pyhash.xx_64, 2282408585429094475)


@pytest.mark.benchmark(group='hash64', disable_gc=True)
def test_xxh3_hash64_perf(benchmark, hash_bencher):
    hash_bencher(benchmark, pyhash.xxh3_64, [
                 17963256408908765216, 4413354387267876313])


@pytest.mark.skipif(not pyhash.build_with_int128, reason="requires int128 support")
@pytest.mark.benchmark(group='hash128', disable_gc=True)
def test_xxh3_hash128_perf(benchmark, hash_bencher):
    hash_bencher(benchmark, pyhash.xxh3_128,
                 114325082382711370665287787442101032992)
