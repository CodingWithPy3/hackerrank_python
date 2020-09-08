n=6
k=1
for row in range(n,0,-1):
    
    for i in range(0,row-1):
        print("_",end="")
    
    print("*"*k)
    k+=1
   
