#! /usr/bin/env python

import ctypes

def libc_func():
    libc = ctypes.CDLL('libc.so.6')
    #char *strstr(char *text, char *pattern)
    libc.strstr.argstype = [ctypes.c_char_p, ctypes.c_char_p]
    libc.strstr.restype = ctypes.c_char_p
    res = libc.strstr(b"ababacd", b"baba")
    print(res)

def libutils_func():
    utils_lib = ctypes.cdll.LoadLibrary('./libutils.so')
    utils_lib.func1.argstype = [ctypes.c_int]
    utils_lib.func1.restype = ctypes.c_int
    for i in range(5):
        print(i, utils_lib.func1(i))

    utils_lib.func2.argstype = [ctypes.c_char_p, ctypes.c_int]
    utils_lib.func2.restype = ctypes.c_void_p

    text = ctypes.c_char_p(b"hello, world")
    l = ctypes.c_int(10)
    utils_lib.func2(text, l)

def libutilscpp_func():
    libutilscpp = ctypes.CDLL('./libutilscpp.so')
    libutilscpp.func3.argstype = [ctypes.c_int]
    libutilscpp.func3.restype = ctypes.c_void_p

    libutilscpp.free_memory.argstype = [ctypes.c_void_p]
    libutilscpp.free_memory.restype = ctypes.c_void_p

    res_func3 = libutilscpp.func3(100500)
    print(type(res_func3))
    print(ctypes.c_char_p(res_func3).value)
    print(ctypes.c_char_p(res_func3))
    libutilscpp.free_memory(ctypes.c_char_p(res_func3))

def main():
    libc_func()
    libutils_func()
    libutilscpp_func()

if __name__ == "__main__":
    main()
