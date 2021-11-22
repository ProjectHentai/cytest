from .cymath import fab_defcallcdef, fab_cpdef, fab_purepy, fab_defcallimpl, pyprint

# import abc
# from _collections_abc import _check_methods


def fab(a):
    if a < 2:
        return a
    else:
        return a * fab(a - 1)


"""
func fab_go(a int){
    if a<2 {
        return a
    }
    return a*fab_go(a-1)
}

for i:=0;i<1000000;i++{
fab_go(20)
}
"""
#
#
# class 批(abc.ABC):
#     def __init__(self):
#         self.count = 0
#
#     @abc.abstractmethod
#     def 透(self):
#         raise NotImplementedError
#
#     @classmethod
#     def __subclasshook__(cls, c):
#         if cls is 批:
#             return _check_methods(c, "透")
#         return NotImplemented
#
#
# class 原批(批):
#
#     def 透(self):
#         self.count += 1
#         return self
#
#
# class 脆脆(批):
#     pass
