# Given an array of integers, calculate the ratios of its elements that are positive, negative, and zero. 
# Print the decimal value of each fraction on a new line with 6 places after the decimal.
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    #user written code:
    neg=pos=zero=0
    for i in arr:
        if i<0:
            neg+=1
        elif i>0:
            pos+=1
        else:
            zero+=1
    narr=[pos,neg,zero]
    
    for i in range(len(narr)):
        narr[i]=round(narr[i]/n, 6)
    
    for x in narr:
        print(x)
# user written code ends
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    
    plusMinus(arr)
    
# Sample Input:
# 6
# -4 3 -9 0 4 1

# Sample Output:
# 0.500000
# 0.333333
# 0.166667
