# Given a time in 12-hour AM/PM format, convert it to military (24-hour) time.
# Note: - 12:00:00AM on a 12-hour clock is 00:00:00 on a 24-hour clock.
# - 12:00:00PM on a 12-hour clock is 12:00:00 on a 24-hour clock.

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Extracting the P or M from AM/PM
    segment=s[-2:-1] 
    if segment =='P': # In case of PM
        # If hour is less than 12 then 12 is added, else just print input itself
        return str(int(s[:2])+12) + s[2:8] if s[:2]<'12'else s[:-2] 
    else:  # AM case
        # If hour is not 12 then print input itself, else make the hour zero
        # Instead of "make the hour zero", we can subtract by 12, but will result in a single zero '0'
        return s[:-2] if s[:2]!='12' else ("00" + s[2:8])

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()


# Sample Input
# 07:05:45PM

# Sample Output
# 19:05:45

# SOME CRITICAL TEST CASES:
# 1) INPUT: 12:40:22AM
#    OUTPUT: 00:40:22
# 2) INPUT: 12:45:54PM
#    OUTPUT: 12:45:54
