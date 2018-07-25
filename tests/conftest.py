from __future__ import unicode_literals

import pytest


@pytest.fixture(scope="module")
def test_data():
    return b'test', u'test'


@pytest.fixture(scope="module")
def hash_tester():
    def do_test(hasher_type, bytes_hash, seed_hash, unicode_hash):
        if hasher_type:
            data, udata = test_data()
            hasher = hasher_type()

            assert hasher
            assert bytes_hash == hasher(data)
            assert seed_hash == hasher(data, seed=bytes_hash)
            assert seed_hash == hasher(data, data)
            assert unicode_hash == hasher(udata)
        else:
            print("WARN: skip test cases for `%s` hasher", hasher_type)

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
