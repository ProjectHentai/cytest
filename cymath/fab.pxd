from libc.stdint cimport uint8_t, uint32_t
cdef extern from "fab.h" nogil:
    long fab_impl(long a)
    void print_bytes(uint8_t *data, uint32_t len)
