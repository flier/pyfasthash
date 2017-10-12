#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import os
import math

from setuptools import setup, Extension

libraries = {
    'fnv': ['hash_32.c', 'hash_32a.c', 'hash_64.c', 'hash_64a.c'],
    'smhasher': ['MurmurHash1.cpp',
                 'MurmurHash2.cpp',
                 'MurmurHash3.cpp',
                 'City.cpp',
                 'Spooky.cpp',
                 'metrohash64.cpp',
                 'metrohash64crc.cpp',
                 'metrohash128.cpp',
                 'metrohash128crc.cpp',
                 't1ha.c',
                 'xxhash.c'],
    'lookup3': ['lookup3.c'],
    'SuperFastHash': ['SuperFastHash.c'],
}

if os.name != "nt":
    libraries['smhasher'].append('farmhash-c.c')

source_files = [os.path.join('src', filename) for filename in ['Hash.cpp']]

for lib, files in libraries.items():
    source_files += [os.path.join('src', lib, filename) for filename in files]

macros = [
    ("BOOST_PYTHON_STATIC_LIB", None),
]
include_dirs = []
library_dirs = []
libraries = []
extra_compile_args = []
extra_link_args = []

if os.name != "nt":
    extra_compile_args += ["-DSUPPORT_INT128=1"]

if os.name == "nt":
    import platform
    is_64bit = platform.architecture()[0] == "64bit"

    macros += [
        ("WIN32", None),
    ]
    include_dirs += [
        os.environ.get('BOOST_HOME'),
        os.path.join(os.environ.get('PYTHON_HOME'), 'include'),
    ]
    library_dirs += [
        os.path.join(os.environ.get('BOOST_HOME'), 'stage/lib'),
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
    libraries += ["boost_python-mt"]
    extra_compile_args += ["-msse4.2", "-maes"]
elif os.name == "posix":
    libraries += [
        "boost_python-py%d%d" % (sys.version_info.major,
                                 sys.version_info.minor),
        "rt",
        "gcc"
    ]
    extra_compile_args += ["-msse4.2", "-maes"]

if os.getenv('TRAVIS') == 'true':
    print("force to link boost::python base on Python v%d.%d" %
          (sys.version_info.major, sys.version_info.minor))

    os.remove('/usr/lib/libboost_python.so')
    os.symlink('/usr/lib/libboost_python-py%d%d.so' % (sys.version_info.major, sys.version_info.minor),
               '/usr/lib/libboost_python.so')

pyhash = Extension(name="_pyhash",
                   sources=source_files,
                   define_macros=macros,
                   include_dirs=include_dirs,
                   library_dirs=library_dirs,
                   libraries=libraries,
                   extra_compile_args=extra_compile_args,
                   extra_link_args=extra_link_args,
                   )

setup(name='pyhash',
      version='0.8.1',
      description='Python Non-cryptographic Hash Library',
      long_description="a python non-cryptographic hash library",
      url='https://github.com/flier/pyfasthash',
      download_url='https://github.com/flier/pyfasthash/releases',
      platforms=["x86", "x64"],
      author='Flier Lu',
      author_email='flier.lu@gmail.com',
      license="Apache Software License",
      py_modules=['pyhash'],
      ext_modules=[pyhash],
      classifiers=[
          'Development Status :: 4 - Beta',
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
      install_requires=[],
      test_suite='pyhash',
      use_2to3=True)
