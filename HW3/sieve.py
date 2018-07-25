# description: Eratosthenes prime
# name: Wang Zezhi
# date: Sep.27th 2015

import math

def sieve(n):
    list0 = []
    
    for i in range(2,n+1):
        list0.append(i)
    
    for i in range(2,int(math.sqrt(n))+1):
        for j in list0:
            if j == i:
                continue
            elif j % i == 0:
                list0.remove(j)
    
    print list0