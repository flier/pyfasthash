from __future__ import unicode_literals

import sys
import platform

import pytest

import pyhash


def test_string(city_64):
    hasher = city_64()

    assert hasher
    assert hasattr(hasher, 'seed')

    assert hasher('hello') == 359204553733634674
    assert hasher('hello world') == 489096247858400539
    assert hasher('hello', ' ', 'world') == 416726000223957297
    assert hasher('world', seed=hasher(
        ' ', seed=hasher('hello'))) == 416726000223957297

    assert hasher(b'hello') == 2578220239953316063

    assert hasher('') == 0
    assert hasher(u'') == 0
    assert hasher(b'') == 0


def test_list(city_64):
    hasher = city_64()

    with pytest.raises(TypeError, message="unsupported argument type"):
        assert hasher(list(b'hello')) == 2578220239953316063


def test_array(city_64):
    from array import array

    hasher = city_64()

    assert hasher(array('B', b'hello')) == 2578220239953316063


def test_buffer(city_64):
    if sys.version_info.major < 3:
        hasher = city_64()

        assert hasher(buffer(b'hello')) == 2578220239953316063


def test_bufferview(city_64):
    hasher = city_64()

    assert hasher(memoryview(b'hello')) == 2578220239953316063


def test_bytearray(city_64):
    hasher = city_64()

    assert hasher(bytearray(b'hello')) == 2578220239953316063


def test_error(city_64, city_128):
    if sys.version_info.major < 3:
        with pytest.raises(TypeError):
            city_64.__call__()

        with pytest.raises(TypeError):
            city_64.__call__(None)

        with pytest.raises(TypeError):
            city_64.__call__(city_128())
    else:
        with pytest.raises(ValueError):
            city_64.__call__()

        with pytest.raises(TypeError):
            city_64.__call__(None)

        with pytest.raises(RuntimeError):
            city_64.__call__(city_128())
