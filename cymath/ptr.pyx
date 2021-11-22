cdef extern from *:
    pass


cdef class Voidptr:
    """wrap a void*"""
    cdef void * p

    @staticmethod
    cdef Voidptr from_ptr(void * p):
        cdef Voidptr self = Voidptr.__new__(Voidptr)
        self.p = p
        return self

    @property
    def value(self) -> int:
        return <int> self.p