from fab cimport fab_impl, print_bytes

def fab_defcallimpl(long a):
    return fab_impl(a)

cdef  long  fab_(long a):
    if a < 2:
        return a
    else:
        return a * fab_(a - 1)

def fab_defcallcdef(long a):
    return fab_(a)

cpdef  long  fab_cpdef(long a):
    if a < 2:
        return a
    else:
        return a * fab_cpdef(a - 1)

def fab_purepy(a):
    if a < 2:
        return a
    else:
        return a * fab_purepy(a - 1)

def pyprint(bytes data):
    print_bytes(data,len(data))