a= list(map(int, input().rstrip().split()))
uni=[]
for i in a:
    if(not(i in uni)):
        uni.append(i)
c=[]
for i in uni:
    c.append(a.count(i))


print(uni[c.index(max(c))])
##uni=[]
##    for i in arr:
##        if(not(i in uni)):
##            uni.append(i)
##    c=[]
##    for i in uni:
##        c.append(arr.count(i))
##    
##    return(uni[c.index(max(c))])
