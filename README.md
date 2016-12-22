[![Travis CI Status](https://travis-ci.org/flier/pyfasthash.svg?branch=master)](https://travis-ci.org/flier/pyfasthash)

  pyhash is a python non-cryptographic hash library. It provide several common hash algorithms with C/C++ implementation for performance.

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

Note: Please use pyhash to install it from pypi

```bash
$sudo easy_install pyhash
```

pyhash support the following hash algorithms

* [FNV](http://isthe.com/chongo/tech/comp/fnv/) (Fowler-Noll-Vo) hash
  - fnv1_32
  - fnv1a_32
  - fnv1_64
  - fnv1a_64
* [MurmurHash](http://code.google.com/p/smhasher/) 1/2/3
  - murmur1_32
  - murmur1_aligned_32
  - murmur2_32
  - murmur2a_32
  - murmur2_aligned_32
  - murmur2_neutral_32
  - murmur2_x64_64a
  - murmur2_x86_64b
  - murmur3_32
  - murmur3_x86_128 **NEW!**
  - murmur3_x64_128 **NEW!**
* [lookup3](http://burtleburtle.net/bob/hash/doobs.html)
  - lookup3 # base on sys.byteorder
  - lookup3_little
  - lookup3_big
* [SuperFastHash](http://www.azillionmonkeys.com/qed/hash.html)
  - super_fast_hash
* [City Hash](https://code.google.com/p/cityhash/) **RECOMMENDED**
  _ city_32 **NEW!**
  - city_64
  - city_128
  - city_crc_128 **NEW!**
* [Spooky Hash](http://burtleburtle.net/bob/hash/spooky.html)
  - spooky_32
  - spooky_64
  - spooky_128
* [FarmHash](https://github.com/google/farmhash)
  - farm_32 **NEW!**
  - farm_64 **NEW!**
  - farm_128 **NEW!**