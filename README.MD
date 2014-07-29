pyhash is a python non-cryptographic hash library. It provide several common hash algorithms with C/C++ implementation for performance.
```
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
```
$sudo easy_install pyhash
```
pyhash support the following hash algorithms

* FNV (Fowler-Noll-Vo) hash
  - fnv1_32
  - fnv1a_32
  - fnv1_64
  - fnv1a_64
* MurmurHash 1/2/3
  - murmur1_32
  - murmur1_aligned_32
  - murmur2_32
  - murmur2a_32
  - murmur2_aligned_32
  - murmur2_neutral_32
  - murmur2_x64_64a
  - murmur2_x86_64b
  - murmur3_32
  - murmur3_x86_128 *NEW!*
  - murmur3_x64_128 *NEW!*
* lookup3
  - lookup3 # base on sys.byteorder
  - lookup3_little
  - lookup3_big
* SuperFastHash
  - super_fast_hash
* City Hash RECOMMENDED
  - city_64 *NEW!*
  - city_128 *NEW!* **build with SSE 4.2 supports**
* Spooky Hash
  - spooky_32 *NEW!*
  - spooky_64 *NEW!*
  - spooky_128 *NEW!*
