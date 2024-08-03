# Current approach to running
compile with: mpicc libtest_c.c -shared -fPIC -o libtest_c.so
run with: mpirun -np 2 python3 ./testing.py

This is tested with Ubuntu 22.04, Python3.12, MPICH 4.2.0, gcc version 13.2.0 (Ubuntu 13.2.0-23ubuntu4) 
This code used to run two years ago but for the life of me, I cannot figure out what is going on?
