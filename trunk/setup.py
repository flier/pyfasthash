#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import os
import math

is_py3k = sys.version_info[0] > 2

if is_py3k:
    import distribute_setup
    distribute_setup.use_setuptools()
else:
    import ez_setup
    ez_setup.use_setuptools()

from setuptools import setup, Extension

libraries = {
    'fnv': ['hash_32.c', 'hash_32a.c', 'hash_64.c', 'hash_64a.c'],
    'MurmurHash': ['MurmurHash1.cpp', 'MurmurHash2.cpp', 'MurmurHash3.cpp'],
    'lookup3': ['lookup3.c'],
    'SuperFastHash': ['SuperFastHash.c'],
}

source_files = [os.path.join('src', file) for file in ['Hash.cpp']]

for lib, files in libraries.items():
    source_files += [os.path.join('src', lib, file) for file in files]
    
macros = [
    ("BOOST_PYTHON_STATIC_LIB", None),
]
include_dirs = []
library_dirs = []
libraries = []
extra_compile_args = []
extra_link_args = []

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
    extra_link_args += ["/DLL", "/OPT:REF", "/OPT:ICF", "/MACHINE:X64" if is_64bit else "/MACHINE:X86"]
elif os.name == "posix" and sys.platform == "darwin":
    is_64bit = math.trunc(math.ceil(math.log(sys.maxsize, 2)) + 1) == 64
    include_dirs += [
        '/opt/local/include',
        '/usr/local/include'
    ]
    libraries += ["boost_python-mt"]
elif os.name == "posix":
    libraries += ["boost_python", "rt"]

pyhash = Extension(name="_pyhash",
                   sources=source_files,
                   define_macros=macros,
                   include_dirs=include_dirs,
                   library_dirs=library_dirs,
                   libraries=libraries,
                   extra_compile_args=extra_compile_args,
                   extra_link_args=extra_link_args,
                   )

extra = {}

if is_py3k:
    extra.update({
        'use_2to3': True
    })

setup(name='pyhash',
    version='0.5.0',
    description='Python Non-cryptographic Hash Library',
    long_description="pyhash is a python non-cryptographic hash library, "
                     "including FNV1, MurmurHash1/2/3, lookup3, SuperFastHash, etc",
    platforms="x86",
    author='Flier Lu',
    author_email='flier.lu@gmail.com',
    url='http://code.google.com/p/pyfasthash/',
    download_url='http://code.google.com/p/pyfasthash/downloads/list',
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
        'Programming Language :: Python :: 3',
        'Topic :: Internet',
        'Topic :: Software Development',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities'
    ], **extra)