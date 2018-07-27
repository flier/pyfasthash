#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import os
import math

from setuptools import setup, Extension
from setuptools.glob import glob
from distutils.sysconfig import customize_compiler

here = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(here, 'README.md')) as f:
    long_description = f.read()

macros = []
include_dirs = [
    "src/pybind11/include",
]
library_dirs = []
libraries = []
extra_compile_args = []
extra_link_args = []

if os.name != "nt":
    macros += [
        ('SUPPORT_INT128', 1),
    ]

if os.name == "nt":
    import platform
    is_64bit = platform.architecture()[0] == "64bit"

    macros += [
        ("WIN32", None),
    ]
    include_dirs += [
        os.path.join(os.environ.get('PYTHON_HOME'), 'include'),
    ]
    library_dirs += [
        os.path.join(os.environ.get('PYTHON_HOME'), 'libs'),
    ]

    extra_compile_args += ["/O2", "/GL", "/MT", "/EHsc", "/Gy", "/Zi"]
    extra_link_args += ["/DLL", "/OPT:REF", "/OPT:ICF",
                        "/MACHINE:X64" if is_64bit else "/MACHINE:X86"]
elif os.name == "posix" and sys.platform == "darwin":
    is_64bit = math.trunc(math.ceil(math.log(sys.maxsize, 2)) + 1) == 64
    include_dirs += [
        '/opt/local/include',
        '/usr/local/include'
    ]

    extra_compile_args += ["-msse4.2", "-maes", "-mavx", "-mavx2", ]
elif os.name == "posix":
    import platform

    libraries += ["rt", "gcc"]

    extra_compile_args += ["-msse4.2", "-maes", "-mavx", "-mavx2", ]

c_libraries = [(
    'fnv', {
        "sources": [
            'src/fnv/hash_32.c',
            'src/fnv/hash_32a.c',
            'src/fnv/hash_64.c',
            'src/fnv/hash_64a.c'
        ]
    }
), (
    'smhasher', {
        "sources": [
            'src/smhasher/MurmurHash1.cpp',
            'src/smhasher/MurmurHash2.cpp',
            'src/smhasher/MurmurHash3.cpp',
            'src/smhasher/City.cpp',
            'src/smhasher/Spooky.cpp',
            'src/smhasher/metrohash64.cpp',
            'src/smhasher/metrohash64crc.cpp',
            'src/smhasher/metrohash128.cpp',
            'src/smhasher/metrohash128crc.cpp',
            'src/smhasher/xxhash.c',
        ],
        "cflags": extra_compile_args,
    }
), (
    't1ha', {
        "sources": [
            'src/smhasher/t1ha/t1ha0.c',
            'src/smhasher/t1ha/t1ha0_ia32aes_avx.c',
            'src/smhasher/t1ha/t1ha0_ia32aes_avx2.c',
            'src/smhasher/t1ha/t1ha0_ia32aes_noavx.c',
            'src/smhasher/t1ha/t1ha1.c',
            'src/smhasher/t1ha/t1ha2.c',
        ],
        "macros": [
            ("T1HA0_AESNI_AVAILABLE", 1),
            ("T1HA0_RUNTIME_SELECT", 1),
        ],
        "cflags": extra_compile_args,
    }
), (
    'lookup3', {
        "sources": ['src/lookup3/lookup3.c']
    }
), (
    'SuperFastHash', {
        "sources": ['src/SuperFastHash/SuperFastHash.c']
    }
)]

if os.name != "nt":
    c_libraries[1][1]['sources'].append('src/smhasher/farmhash-c.c')

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
      version='0.9.0',
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
          'Topic :: Internet',
          'Topic :: Software Development',
          'Topic :: Software Development :: Libraries :: Python Modules',
          'Topic :: Utilities'
      ],
      keywords='hash hashing fasthash',
      setup_requires=['pytest-runner', 'pytest-benchmark'],
      tests_require=['pytest'],
      use_2to3=True)
