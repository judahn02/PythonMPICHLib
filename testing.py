import mpipytest as MPIpy

theClass = MPIpy.C_Functions()

check = theClass.add(4,5)
if check == 9:
    print("pass")
else:
    print("fail")
    
