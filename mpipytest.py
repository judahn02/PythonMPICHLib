import ctypes as CT
import atexit

class MPIpyWrongArgument(Exception):
    pass

class C_Functions:
    
    c_code = CT.CDLL('./libtest_c.so')

    def __init__(self):

        self.__add = C_Functions.c_code.add
        self.__add.argtypes = [CT.c_int, CT.c_int]
        self.__add.restype = CT.c_int

        # self.__finalize = C_Functions.c_code.MPI_Finalize

        C_Functions.c_code.MPI_Init()
        atexit.register(self.__finalize)

    

    def add(self, a: int, b: int):
        if type(a) == int and type(b) == int:
            return self.__add(a, b)
        else:
            raise MPIpyWrongArgument("Arguments for function are incorrect")
