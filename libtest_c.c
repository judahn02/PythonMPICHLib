#include <stdlib.h>
#include <stdio.h>
#include "mpi.h"

/*
    To Compile:
    mpicc libtest_c.c -shared -fPIC -o libtest_c.so
*/

/*
    Notes:
    MPI_Init() and MPI_Finalize() are used in the Python
    library but not defined here.
*/

// extern int add(int, int) ;
// void MPI_Finalize() ;

int add(int a, int b) {
    return a + b ;
}
