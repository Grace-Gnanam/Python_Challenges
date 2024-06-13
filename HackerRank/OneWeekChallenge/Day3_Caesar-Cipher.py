# The classic Caesar Cipher, with a small twist

# Example 1:
# Original alphabet:      abcdefghijklmnopqrstuvwxyz
# Alphabet rotated +3:    defghijklmnopqrstuvwxyzabc

# Example 2:
# Provided: middle-Outz
# Key: 2
# Expected output: okffng-Qwvb

# Important Note: Test Cases also Contains Key of 87

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'caesarCipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#

def caesarCipher(s, k):
    # 65 to 90 for uppercase letters
    # 97 to 122 for lowercase letters
    result = ""
    
    for i in range(len(s)):
        char = s[i]
        if not char.isalpha():
            result+=char
            continue
        # Encrypt uppercase characters
        if (char.isupper()):
            result += chr((ord(char) + k-65) % 26 + 65)
 
        # Encrypt lowercase characters
        else:
            result += chr((ord(char) + k - 97) % 26 + 97)
 
    return str(result)

if __name__ == '__main__':
    s = input()
    k = int(input().strip())
    result = caesarCipher(s, k)
    print(result)
