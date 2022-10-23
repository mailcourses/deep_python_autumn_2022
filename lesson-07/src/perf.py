#! /usr/bin/env python

import time

import ctypes
import cffi

import cutils
from cython import cyutils

MAX_FIBONACCI_NUM = 35

def fibonacci(n: int) -> int:
    if n < 2:
        return 1
    return fibonacci(n-2) + fibonacci(n-1)

def main():
    print("==== python ====")
    start_ts = time.time()
    res_py = [fibonacci(n) for n in range(MAX_FIBONACCI_NUM)]
    end_ts = time.time()
    print(f"Time of execution of python fibonacci implementation is {end_ts-start_ts} seconds")

    print("==== ctypes ====")
    lib = ctypes.CDLL('./ctypes/libutilscpp.so')
    lib.fibonacci.argstype = [ctypes.c_int]
    lib.fibonacci.restype = ctypes.c_int

    start_ts = time.time()
    res_ctypes = [lib.fibonacci(n) for n in range(MAX_FIBONACCI_NUM)]
    end_ts = time.time()
    print(f"Time of execution of ctypes fibonacci implementation is {end_ts-start_ts} seconds")

    print("==== cffi ====")
    ffi = cffi.FFI()
    cffi_lib = ffi.dlopen('./cffi/libarea.so')
    ffi.cdef('''
    int fibonacci(int n);
    ''')

    start_ts = time.time()
    res_cffi = [cffi_lib.fibonacci(n) for n in range(MAX_FIBONACCI_NUM)]
    end_ts = time.time()
    print(f"Time of execution of cffi fibonacci implementation is {end_ts-start_ts} seconds")

    start_ts = time.time()
    res_capi = [cutils.fibonacci(n) for n in range(MAX_FIBONACCI_NUM)]
    end_ts = time.time()
    print(f"Time of execution of capi fibonacci implementation is {end_ts-start_ts} seconds")

    start_ts = time.time()
    res_cython = [cyutils.fibonacci(n) for n in range(MAX_FIBONACCI_NUM)]
    end_ts = time.time()
    print(f"Time of execution of cython fibonacci implementation is {end_ts-start_ts} seconds")
    print(f"{res_ctypes=}, {res_py=}, {res_cffi=}, {res_capi=}, {res_cython=}")
    assert res_ctypes == res_py == res_cffi == res_capi == res_cython

if __name__ == "__main__":
    main()
