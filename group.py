arr=[1,1,0,1,0,1,1,0,1,1,1,1,0,1]
res=0
i=0

while(i!=len(arr)):
    if(arr[i]==1):
        c=0
        while(arr[i+c]==0):
            print("cal")
            c=+1
        if(c!=0):
            res+=1
        i=i+c
    else:
        print("s")
        i=i+1
        
print(res)
