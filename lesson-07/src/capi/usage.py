#! /usr/bin/env python

import cutils

def main():
    l = list(range(1,6))
    res = cutils.accumulate(l)
    print(f"Sum of list elements is {res}")
    res = cutils.fibonacci(10)
    print(f"Result of fibonacci(10) is {res}")

if __name__ == "__main__":
    main()
