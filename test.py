from functools import partial
import timeit

from cymath import fab_cpdef, fab_defcallcdef, fab_purepy, fab_defcallimpl, pyprint

default_number = 10000000

# print(f"纯py {timeit.timeit('fab(20)', number=default_number, globals=globals())}")
# print(f"cpdef {timeit.timeit('fab_cpdef(20)', number=default_number, globals=globals())}")
# print(f"defcallcdef {timeit.timeit('fab_defcallcdef(20)', number=default_number, globals=globals())}")
# # print(f"purepy {timeit.timeit('fab_purepy(20)', number=default_number, globals=globals())}")
# print(f"purec {timeit.timeit('fab_defcallimpl(20)', number=default_number, globals=globals())}")

from cymath import test


class Context:
    def __init__(self):
        self.closed = False

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("close")
        self.closed = True


#
# def test():
#     con = Context()
#     try:
#         print("要返回了",con.closed)
#         return con
#     finally:
#         con.closed = True
#
#
# def main():
#     con = test()
#     print("调用返回了")
#     print(con.closed)
list(range(20))
data = bytes(list(range(20)))
print(data)
pyprint(data)
# print(data)
# test.print_bytes(data, len(data))
