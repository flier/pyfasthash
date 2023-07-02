from __future__ import unicode_literals

import sys

import pytest

import pyhash

# https://github.com/flier/pyfasthash/issues/3


def test_error_return_none():
    if hasattr(sys, "getrefcount"):  # skip pypy
        h = pyhash.fnv1_64()

        old_refcnt = sys.getrefcount(None)

        for _ in range(10000):
            try:
                h(None)

                pytest.fail("fail to raise exception")
            except TypeError:
                pass

        new_refcnt = sys.getrefcount(None)

        assert old_refcnt >= new_refcnt


# https://github.com/flier/pyfasthash/issues/24


def test_default_string_type():
    hasher = pyhash.murmur3_32()

    assert hasher("foo") == hasher("foo")
    assert hasher("foo") != hasher(b"foo")
