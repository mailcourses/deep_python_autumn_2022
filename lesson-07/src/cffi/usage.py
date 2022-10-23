#! /usr/bin/env python

import cffi

def ABI():
    ffi = cffi.FFI()
    lib = ffi.dlopen('./libarea.so')
    ffi.cdef('''
    struct Point {
        int x;
        int y;
    };

    int area(struct Point *p1, struct Point *p2);
    ''')

    p1 = ffi.new('struct Point *')
    p2 = ffi.new('struct Point *')
    p1.x, p1.y = (1, 0)
    p2.x, p2.y = (5, 10)
    area = lib.area(p1, p2)
    print(area)
    #baba_joe = ffi.new('struct BabaJoe *')

def API():
    ffibuilder = cffi.FFI()
    ffibuilder.cdef('''
    int sum(int *arr, int len);
    ''')
    ffibuilder.set_source('cffisum',
    r'''
    #include <stdlib.h>

    int sum(int *arr, int len)
    {
        int res = 0;
        for (int i = 0; i < len; ++i)
        {
            res += arr[i];
        }
        return res;
    }
    ''')
    arr = list(range(1, 6))
    c_arr = ffibuilder.new('int []', arr)
    ffibuilder.compile()

    from cffisum import lib
    print(lib.sum(c_arr, len(arr)))

def main():
    ABI()
    API()

if __name__ == "__main__":
    main()
