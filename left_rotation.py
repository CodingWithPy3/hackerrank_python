import math
import os
import random
import re
import sys

# Complete the rotLeft function below.
def rotLeft(a, d):
    res=[]    
    for i in range(len(a)):
        ele=a[i]
        if(i<d):
            pos=-(d-i)
        else:
            pos=(i-d)
        
        res.insert(pos,ele)
        print(res)
    return res  
    
if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = list(map(int, input().rstrip().split()))

    result = rotLeft(a, d)
    print(result)
    #fptr.write(' '.join(map(str, result)))
    #fptr.write('\n')

    #fptr.close()
