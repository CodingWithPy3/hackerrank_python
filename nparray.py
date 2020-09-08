import numpy
np=numpy

def arrays(arr):
    a=np.zeros(len(arr))
    for i in range(len(arr)):
        a[i]=float(arr[i])

    return np.flipud(a)
        

arr = input().strip().split(' ')
result = arrays(arr)
print(result)
