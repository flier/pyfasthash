# Introduction [![Travis CI Status](https://travis-ci.org/flier/pyfasthash.svg?branch=master)](https://travis-ci.org/flier/pyfasthash) [![codecov](https://codecov.io/gh/flier/pyfasthash/branch/master/graph/badge.svg)](https://codecov.io/gh/flier/pyfasthash)

  pyhash is a python non-cryptographic hash library. It provides several common hash algorithms with C/C++ implementation for performance.

```python
>>> import pyhash
>>> hasher = pyhash.fnv1_32()
>>> hasher('hello world')
2805756500L

>>> hasher('hello', ' ', 'world')
2805756500L

>>> hasher('hello ')
406904344
>>> hasher('world', seed=406904344)
2805756500L
```

# Installation

Please use pyhash to install it with `pip`.

```bash
$sudo pip install pyhash
```

**Notes** `pyhash` only support `pypy` v6.0 or newer, please [download and install](https://pypy.org/download.html) the latest `pypy`.

# Algorithms

pyhash supports the following hash algorithms

- [FNV](http://isthe.com/chongo/tech/comp/fnv/) (Fowler-Noll-Vo) hash
  - fnv1_32
  - fnv1a_32
  - fnv1_64
  - fnv1a_64
- [MurmurHash](http://code.google.com/p/smhasher/)
  - murmur1_32
  - murmur1_aligned_32
  - murmur2_32
  - murmur2a_32
  - murmur2_aligned_32
  - murmur2_neutral_32
  - murmur2_x64_64a
  - murmur2_x86_64b
  - murmur3_32
  - murmur3_x86_128
  - murmur3_x64_128
- [lookup3](http://burtleburtle.net/bob/hash/doobs.html)
  - lookup3
  - lookup3_little
  - lookup3_big
- [SuperFastHash](http://www.azillionmonkeys.com/qed/hash.html)
  - super_fast_hash
- [City Hash](https://code.google.com/p/cityhash/)
  _ city_32
  - city_64
  - city_128
  - city_crc_128
- [Spooky Hash](http://burtleburtle.net/bob/hash/spooky.html)
  - spooky_32
  - spooky_64
  - spooky_128
- [FarmHash](https://github.com/google/farmhash)
  - farm_32
  - farm_64
  - farm_128
- [MetroHash](https://github.com/jandrewrogers/MetroHash)
  - metro_64
  - metro_128
  - metro_crc_64
  - metro_crc_128
- [MumHash](https://github.com/vnmakarov/mum-hash)
  - mum_64
- [T1Hash](https://github.com/leo-yuriev/t1ha)
  - t1ha2 _(64-bit little-endian)_
  - t1ha2_128 _(128-bit little-endian)_
  - t1ha1 _(64-bit native-endian)_
  - t1ha1_le _(64-bit little-endian)_
  - t1ha1_be _(64-bit big-endian)_
  - t1ha0 _(64-bit, choice fastest function in runtime.)_
  - t1ha0_ia32aes_noavx _(64-bit, x86 with AES-NI without AVX extensions)_
  - t1ha0_ia32aes_avx _(64-bit, x86 with AES-NI and AVX extensions)_
  - t1ha0_ia32aes_avx2 _(64-bit, x86 with AES-NI and AVX2 extensions)_
  - t1ha0_32 _(32-bit native-endian)_
  - t1ha0_32le _(32-bit little-endian)_
  - t1ha0_32be _(32-bit big-endian)_
  - ~~t1_32~~
  - ~~t1_32_be~~
  - ~~t1_64~~
  - ~~t1_64_be~~
- [XXHash](https://github.com/Cyan4973/xxHash)
  - xx_32
  - xx_64

**Notes**

Python has two types can be used to present string literals, the hash values of the two types are definitely different.

- For Python 2.x [String literals](https://docs.python.org/2/reference/lexical_analysis.html#string-literals), `str` will be used by default, `unicode` can be used with the `u` prefix.
- For Python 3.x [String and Bytes literals](https://docs.python.org/3/reference/lexical_analysis.html#string-and-bytes-literals), `unicode` will be used by default, `bytes` can be used with the `b` prefix.

For example,

```
$ python2
Python 2.7.15 (default, Jun 17 2018, 12:46:58)
[GCC 4.2.1 Compatible Apple LLVM 9.1.0 (clang-902.0.39.2)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import pyhash
>>> hasher = pyhash.murmur3_32()
>>> hasher('foo')
4138058784L
>>> hasher(u'foo')
2085578581L
>>> hasher(b'foo')
4138058784L
```

```
$ python3
Python 3.7.0 (default, Jun 29 2018, 20:13:13)
[Clang 9.1.0 (clang-902.0.39.2)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import pyhash
>>> hasher = pyhash.murmur3_32()
>>> hasher('foo')
2085578581
>>> hasher(u'foo')
2085578581
>>> hasher(b'foo')
4138058784
```

You can also import [unicode_literals](http://python-future.org/unicode_literals.html) to use unicode literals in Python 2.x

```python
from __future__ import unicode_literals
```

> In general, it is more compelling to use unicode_literals when back-porting new or existing Python 3 code to Python 2/3 than when porting existing Python 2 code to 2/3. In the latter case, explicitly marking up all unicode string literals with u'' prefixes would help to avoid unintentionally changing the existing Python 2 API. However, if changing the existing Python 2 API is not a concern, using unicode_literals may speed up the porting process.
