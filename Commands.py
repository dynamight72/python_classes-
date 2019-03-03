def make_list():
    result = []
    in_val = 0
    while in_val >= 0:
        in_val = int(input("Enter integer:"))
        if in_val >= 0:
                  result = result + [in_val]
    return result

def main():
    col = make_list()
    print(col)
main()

import time
from time import clock
import math
from math import sqrt
def count_prime(n):
    start = clock()
    count = 0
    for val in range(2,n):
        result = True
        root = int(sqrt(val)+1)
        trial_factor = 2
        while result and trial_factor <= root:
            result = (val % trial_factor!= 0)
            trial_factor += 1
        if result:
          count += 1

    stop = clock()
    print('Count = ',count,'Elapsed time = ',stop-start,'seconds')

def seive(n):
    start = clock()
    nonprime = n * [False]
    count = 0
    nonprime[0] = nonprime[1] = True
    for i in range(2,n):
        if nonprime[i] :
            count += 1
    for j in range(2*i,n,i):
        nonprime[j] = True
    stop = clock()
    print('Count = ', count, 'Elapsed time = ', stop - start, 'seconds')

