from __future__ import unicode_literals

import pytest


@pytest.fixture(scope="module")
def test_data():
    return b'test', u'test'


@pytest.fixture(scope="module")
def hash_tester():
    def do_test(hasher_type, bytes_hash, seed_hash, unicode_hash):
        assert hasher_type

        assert hasattr(hasher_type, 'seed')

        data, udata = test_data()
        hasher = hasher_type()

        assert hasher
        assert hasattr(hasher, 'seed')
        assert bytes_hash == hasher(
            data), "bytes hash should be %d" % hasher(data)
        assert seed_hash == hasher(
            data, seed=bytes_hash), "bytes hash with seed should be %d" % hasher(data, seed=bytes_hash)
        assert seed_hash == hasher(data, data)
        assert seed_hash == hasher(data, seed=hasher(data))
        assert unicode_hash == hasher(
            udata), "unicode hash should be %d" % hasher(udata)

    return do_test


@pytest.fixture(scope="module")
def fingerprint_tester():
    def do_test(fingerprinter_type, bytes_fingerprint, unicode_fingerprint):
        assert fingerprinter_type

        assert not hasattr(fingerprinter_type, 'seed')

        data, udata = test_data()
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

        assert result == hash

    return do_bench
