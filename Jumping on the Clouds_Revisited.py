n=19
k=19
i=k
e=100
c=list(map(int,input().split()))
if(i>n-1):
        i=i-n
while(1):
    if(i==0):
        if(c[i]==1):
            e -= 3
        else:
            e-=1
        print(i)
        break
        
    if(c[i]==1):
        e -= 3
    else:
        e-=1
    i+=k

    if(i>n-1):
        i=i-n
    print(i)
