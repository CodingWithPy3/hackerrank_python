arr=[1,2,3,4,5]
mini=100
maxi=-1
sm=sum(arr)
print(sm)
for i in range(len(arr)):
    res=sm-arr[i]
    if(res<mini):
        mini=res
    if(res>maxi):
        maxi=res
print(mini , maxi)
