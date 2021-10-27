from collections import namedtuple
import os
import platform
import sys
import logging

import pytest

import pyhash


@pytest.fixture
def is_x86():
    return platform.machine().lower() in ['i386', 'i686', 'x86_64', 'amd64']


@pytest.fixture
def is_64bit():
    return sys.maxsize > 2**32


@pytest.fixture
def is_winnt():
    return os.name == "nt"


@pytest.fixture
def is_msvc():
    return getattr(pyhash, "_MSC_VER", None) is not None


CpuFeatures = namedtuple("CpuFeatures",
                         ['name', 'vendor', 'arch', 'sse41', 'sse42', 'aes', 'avx', 'avx2'])


@pytest.fixture
def cpu(is_x86, is_64bit):
    cpu = CpuFeatures(name=platform.processor(), vendor=platform.platform(), arch=platform.machine(),
                      sse41=False, sse42=False, aes=False, avx=False, avx2=False)

    if is_x86:
        from cpuid import _is_set, cpu_vendor, cpu_name, cpu_microarchitecture

        cpu = CpuFeatures(
            name=cpu_name().rstrip('\x00'),
            vendor=cpu_vendor(),
            arch=cpu_microarchitecture()[0],
            sse41=_is_set(1, 2, 19) == 'Yes',
            sse42=_is_set(1, 2, 20) == 'Yes',
            aes=_is_set(1, 2, 25) == 'Yes',
            avx=_is_set(1, 2, 28) == 'Yes',
            avx2=_is_set(7, 1, 5) == 'Yes',
        )

    logging.getLogger().info("CPU %s", cpu)

    return cpu


@pytest.fixture(scope="module")
def test_data():
    return b'test', u'test'


for name in pyhash.__hasher__:
    def generate_fixture(name, hasher):
        @pytest.fixture(scope='module', name=name)
        def wrap():
            return hasher
        return wrap

    globals()[name] = generate_fixture(name, getattr(pyhash, name))


@pytest.fixture(scope="module")
def hash_tester(test_data):
    def do_test(hasher_type, bytes_hash, seed_hash, unicode_hash):
        assert hasher_type

        assert hasattr(hasher_type, 'seed')

        data, udata = test_data
        hasher = hasher_type()

        assert hasher
        assert hasattr(hasher, 'seed')
        assert hasher(data) in as_list(
            bytes_hash), "bytes hash should be %d" % hasher(data)
        assert hasher(data, seed=bytes_hash) in as_list(
            seed_hash), "bytes hash with seed should be %d" % hasher(data, seed=bytes_hash)
        assert hasher(data, data) in as_list(
            seed_hash), "hash(data, data) should be %d" % hasher(data, data)
        assert hasher(data, seed=hasher(data)) in as_list(
            seed_hash), "hasher(data, seed=hasher(data)) should be %d" % hasher(data, seed=hasher(data))
        assert hasher(udata) in as_list(
            unicode_hash), "unicode hash should be %d" % hasher(udata)

    return do_test


def as_list(v):
    if isinstance(v, list):
        return v

    return [v]


@pytest.fixture(scope="module")
def fingerprint_tester(test_data):
    def do_test(fingerprinter_type, bytes_fingerprint, unicode_fingerprint):
        assert fingerprinter_type

        assert not hasattr(fingerprinter_type, 'seed')

        data, udata = test_data
        fingerprinter = fingerprinter_type()

        assert fingerprinter
        assert not hasattr(fingerprinter, 'seed')
        assert bytes_fingerprint == fingerprinter(
            data), "bytes fingerprint should be %d" % fingerprinter(data)
        assert unicode_fingerprint == fingerprinter(
            udata), "unicode fingerprint should be %d" % fingerprinter(udata)

        bytes_fingerprints = fingerprinter(data, data)

        assert [bytes_fingerprint,
                bytes_fingerprint] == bytes_fingerprints, "bytes fingerprint should be %s" % bytes_fingerprints

    return do_test


@pytest.fixture(scope="module")
def hash_bencher():
    def do_bench(benchmark, hasher, hash, size=256):
        h = hasher()
        data = bytes(bytearray([i % 256 for i in range(size)]))

        @benchmark
        def result():
            return h(data)

        if isinstance(hash, list):
            assert result in hash
        else:
            assert result == hash

    return do_bench
