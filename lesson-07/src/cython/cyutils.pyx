cdef float x = 0.5

cpdef int test(int x):
    cdef int y = 1
    cdef int i
    for i in range(1, x+1):
        y *= i
    return y

cpdef fibonacci(int n):
    if n < 2:
        return 1
    return fibonacci(n-2) + fibonacci(n-1)
