##from math import degrees,atan2
##AB = int(input())
##BC = int(input())
##
##print(round(degrees(atan2(AB,BC))))

from collections import Counter
a = Counter("aabbbccde")
a = sorted(a)
for keys in a:
    if(a[keys]>1):
        print(keys,a[keys])
