# cython: language_level=3
from libc.stdint cimport uint8_t, uint32_t
from libc.stdio cimport printf

cdef class Base:
    cdef:
        int f1
        int f2
    def __cinit__(self, *args, **kwargs):
        print(f"Base cinit f1:{args[0]}  f2:{args[1]}")
        self.f1 = <int> args[0]
        self.f2 = <int> args[1]

    def __init__(self, int f1, int f2):
        print(f"Base init f1:{f1}  f2:{f2}")

cdef class Sub(Base):
    cdef int f3

    def __cinit__(self, int f1, int f2, int f3):
        self.f3 = f3
        print(f"sub cinit f1:{f1}  f2:{f2} f3:{f3}")

    def __init__(self, int f1, int f2, int f3):
        print(f"sub init f1:{f1}  f2:{f2} f3:{f3}")
        super().__init__(f1, f2)

cpdef print_bytes(uint8_t *data, uint32_t len):
    cdef uint32_t i
    for i in range(len):
        printf("%u", data[i])
    printf("\n")
    cdef uint32_t *temp = <uint32_t*>data


