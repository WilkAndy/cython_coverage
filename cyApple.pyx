# cython: linetrace=True
from libcpp.list cimport list as clist
from libcpp.string cimport string
from libc.stdlib cimport malloc

cdef extern from "apple.h" namespace "mango" :
    cdef cppclass apple:
            apple(int)
            int execute()
cdef class pyApple:
    cdef apple* aa
    def __init__(self, number):
            self.aa = new apple(number)

    def  getSquare(self):
            return self.aa.execute()
	    