#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import os
import platform
from glob import glob

from setuptools import setup, Extension

here = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(here, 'README.md')) as f:
    long_description = f.read()

machine = platform.machine()
IS_X86 = machine in ['i386', 'i686', 'x86_64']
IS_ARM = machine in ['aarch64', 'aarch64_be', 'armv8b', 'armv8l']
IS_PPC = machine in ['ppc', 'ppc64', 'ppc64le', 'ppc64le']
IS_POSIX = os.name == "posix"
IS_64BITS = sys.maxsize > 2**32


def cpu_features():
    from collections import namedtuple

    CpuFeatures = namedtuple(
        "CpuFeatures", ['sse41', 'sse42', 'aes', 'avx', 'avx2'])

    sse41 = sse42 = aes = avx = avx2 = False

    if IS_X86:
        try:
            from cpuid import _is_set

            sse41 = IS_X86 and _is_set(1, 2, 19),
            sse42 = IS_X86 and _is_set(1, 2, 20),
            aes = IS_X86 and _is_set(1, 2, 25),
            avx = IS_X86 and _is_set(1, 2, 28),
            avx2 = IS_X86 and _is_set(7, 1, 5),
        except ImportError:
            if IS_64BITS:
                sse41 = sse42 = aes = avx = avx2 = True

    return CpuFeatures(sse41, sse42, aes, avx, avx2)


cpu = cpu_features()


macros = []
include_dirs = [
    "src/pybind11/include",
    "src/highwayhash",
]
library_dirs = []
libraries = []
extra_macros = []
extra_compile_args = []
extra_link_args = []

if os.name == "nt":
    macros += [
        ("WIN32", None),
    ]

    python_home = os.environ.get('PYTHON_HOME')

    if python_home:
        include_dirs += [
            os.path.join(python_home, 'include'),
        ]
        library_dirs += [
            os.path.join(python_home, 'libs'),
        ]

    extra_macros += [("WIN32", 1)]
    extra_compile_args += ["/O2", "/GL", "/MT", "/EHsc", "/Gy", "/Zi"]
    extra_link_args += ["/DLL", "/OPT:REF", "/OPT:ICF",
                        "/MACHINE:X64" if IS_64BITS else "/MACHINE:X86"]
else:
    macros += [
        ('SUPPORT_INT128', 1),
    ]

    if IS_POSIX:
        if sys.platform == "darwin":
            include_dirs += [
                '/opt/local/include',
                '/usr/local/include'
            ]

            extra_compile_args += [
                "-Wdeprecated-register",
                "-stdlib=libc++",
            ]
        else:
            libraries += ["rt", "gcc"]

if IS_X86 and IS_POSIX:
    extra_compile_args += list(filter(None, [
        "-msse4.2" if cpu.sse42 else None,
        "-maes" if cpu.aes else None,
        "-mavx" if cpu.avx else None,
        "-mavx2" if cpu.avx2 else None,
    ]))

if IS_ARM:
    extra_compile_args += [
        '-mfloat-abi=hard',
        '-march=armv7-a',
        '-mfpu=neon',
    ]

c_libraries = [(
    'fnv', {
        "sources": [
            'src/fnv/hash_32.c',
            'src/fnv/hash_32a.c',
            'src/fnv/hash_64.c',
            'src/fnv/hash_64a.c'
        ],
        "macros": extra_macros,
    }
), (
    'smhasher', {
        "sources": [
            'src/smhasher/MurmurHash1.cpp',
            'src/smhasher/MurmurHash2.cpp',
            'src/smhasher/MurmurHash3.cpp',
            'src/smhasher/City.cpp',
            'src/smhasher/Spooky.cpp',
            'src/smhasher/SpookyV2.cpp',
            'src/smhasher/metrohash/metrohash64.cpp',
            'src/smhasher/metrohash/metrohash64crc.cpp',
            'src/smhasher/metrohash/metrohash128.cpp',
            'src/smhasher/metrohash/metrohash128crc.cpp',
        ],
        "cflags": extra_compile_args + [
            "-std=c++11",
        ],
    }
), (
    't1ha', {
        "sources": list(filter(None, [
            'src/t1ha/src/t1ha0.c',
            'src/t1ha/src/t1ha0_ia32aes_avx.c' if cpu.avx else None,
            'src/t1ha/src/t1ha0_ia32aes_avx2.c' if cpu.avx2 else None,
            'src/t1ha/src/t1ha0_ia32aes_noavx.c',
            'src/t1ha/src/t1ha1.c',
            'src/t1ha/src/t1ha2.c',
        ])),
        "macros": [
            ("T1HA0_AESNI_AVAILABLE", 1 if cpu.aes else 0),
            ("T1HA0_RUNTIME_SELECT", 1),
        ],
        "cflags": extra_compile_args,
    }
), (
    'farm', {
        "sources": ['src/smhasher/farmhash-c.c'],
        "macros": extra_macros,
    }
), (
    'lookup3', {
        "sources": ['src/lookup3/lookup3.c'],
        "macros": extra_macros,
    }
), (
    'SuperFastHash', {
        "sources": ['src/SuperFastHash/SuperFastHash.c'],
        "macros": extra_macros,
    }
), (
    "highwayhash", {
        "sources": list(filter(None, [
            "src/highwayhash/highwayhash/arch_specific.cc",
            "src/highwayhash/highwayhash/instruction_sets.cc",
            "src/highwayhash/highwayhash/os_specific.cc",
            "src/highwayhash/highwayhash/hh_portable.cc",
            "src/highwayhash/highwayhash/hh_sse41.cc" if cpu.sse41 else None,
            "src/highwayhash/highwayhash/hh_avx2.cc" if cpu.avx2 else None,
            "src/highwayhash/highwayhash/hh_neon.cc" if IS_ARM else None,
            "src/highwayhash/highwayhash/hh_vsx.cc" if IS_PPC else None,
        ])),
        "cflags": extra_compile_args + [
            "-Isrc/highwayhash",
            "-std=c++11"
        ],
    }
), (
    "xxhash", {
        "sources": ["src/xxHash/xxhash.c"],
    }
)]

libraries += [libname for (libname, _) in c_libraries]

pyhash = Extension(name="_pyhash",
                   sources=['src/Hash.cpp'],
                   depends=glob('src/*.h'),
                   define_macros=macros,
                   include_dirs=include_dirs,
                   library_dirs=library_dirs,
                   libraries=libraries,
                   extra_compile_args=extra_compile_args + ["-std=c++11"],
                   extra_link_args=extra_link_args,
                   )

setup(name='pyhash',
      version='0.9.4',
      description='Python Non-cryptographic Hash Library',
      long_description=long_description,
      long_description_content_type='text/markdown',
      url='https://github.com/flier/pyfasthash',
      download_url='https://github.com/flier/pyfasthash/releases',
      platforms=["x86", "x64"],
      author='Flier Lu',
      author_email='flier.lu@gmail.com',
      license="Apache Software License",
      packages=['pyhash'],
      libraries=c_libraries,
      ext_modules=[pyhash],
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Intended Audience :: Developers',
          'Intended Audience :: System Administrators',
          'License :: OSI Approved :: Apache Software License',
          'Natural Language :: English',
          'Operating System :: Microsoft :: Windows',
          'Operating System :: POSIX',
          'Programming Language :: C++',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: Implementation :: PyPy',
          'Topic :: Internet',
          'Topic :: Software Development',
          'Topic :: Software Development :: Libraries :: Python Modules',
          'Topic :: Utilities'
      ],
      keywords='hash hashing fasthash',
      tests_require=['pytest', 'pytest-runner', 'pytest-benchmark'])
