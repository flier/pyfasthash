from __future__ import unicode_literals

import sys
import platform

import pytest

import pyhash


def test_string(city_fingerprint_256):
    fp = city_fingerprint_256()

    assert fp
    assert not hasattr(fp, 'seed')

    assert fp(
        'hello') == 85269287788015250159504678996909715671377074579298442842859846348216760383456
    assert fp('hello', ' ', 'world') == [
        85269287788015250159504678996909715671377074579298442842859846348216760383456,
        96002752956723026543986242229272779665913536958721069786304092822660732998180,
        48731312164395256331902723544149022249026467417384836741664854409465211001225
    ]

    assert fp(
        b'hello') == 32224966601437776796805147064203168097183942002141386838543322678917249904243

    assert fp(
        '') == 105392963878170340009271248359803826743454413279965606456743994508350154550720
    assert fp(
        u'') == 105392963878170340009271248359803826743454413279965606456743994508350154550720
    assert fp(
        '') == 105392963878170340009271248359803826743454413279965606456743994508350154550720


def test_list(city_fingerprint_256):
    fp = city_fingerprint_256()

    with pytest.raises(TypeError, message="unsupported argument type"):
        assert fp(list(b'hello')) == 2578220239953316063


def test_array(city_fingerprint_256):
    from array import array

    fp = city_fingerprint_256()

    assert fp(array('B', b'hello')
              ) == 32224966601437776796805147064203168097183942002141386838543322678917249904243


def test_buffer(city_fingerprint_256):
    if sys.version_info.major < 3:
        fp = city_fingerprint_256()

        assert fp(buffer(
            b'hello')) == 32224966601437776796805147064203168097183942002141386838543322678917249904243


def test_bufferview(city_fingerprint_256):
    fp = city_fingerprint_256()

    assert fp(memoryview(
        b'hello')) == 32224966601437776796805147064203168097183942002141386838543322678917249904243


def test_bytearray(city_fingerprint_256):
    fp = city_fingerprint_256()

    assert fp(bytearray(
        b'hello')) == 32224966601437776796805147064203168097183942002141386838543322678917249904243


def test_error(farm_fingerprint_32, farm_fingerprint_64):
    if sys.version_info.major < 3:
        with pytest.raises(TypeError):
            farm_fingerprint_32.__call__()

        with pytest.raises(TypeError):
            farm_fingerprint_32.__call__(None)

        with pytest.raises(TypeError):
            farm_fingerprint_32.__call__(farm_fingerprint_64())
    else:
        with pytest.raises(ValueError):
            farm_fingerprint_32.__call__()

        with pytest.raises(TypeError):
            farm_fingerprint_32.__call__(None)

        with pytest.raises(RuntimeError):
            farm_fingerprint_32.__call__(farm_fingerprint_64())
