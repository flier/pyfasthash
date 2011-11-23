//-----------------------------------------------------------------------------
// MurmurHash1 was written by Austin Appleby, and is placed in the public
// domain. The author hereby disclaims copyright to this source code.

#ifndef _MURMURHASH1_H_
#define _MURMURHASH1_H_

//-----------------------------------------------------------------------------
// Platform-specific functions and macros

// Microsoft Visual Studio

#if defined(_MSC_VER)

typedef unsigned char uint8_t;
typedef unsigned long uint32_t;
typedef unsigned __int64 uint64_t;

// Other compilers

#else	// defined(_MSC_VER)

#include <stdint.h>

#endif // !defined(_MSC_VER)

//-----------------------------------------------------------------------------

uint32_t MurmurHash1        ( const void * key, int len, uint32_t seed );
uint32_t MurmurHash1Aligned ( const void * key, int len, uint32_t seed );

//-----------------------------------------------------------------------------

#endif // _MURMURHASH1_H_
