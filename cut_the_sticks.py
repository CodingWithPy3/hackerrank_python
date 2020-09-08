arr = [1 ,2 ,3, 4 ,3 ,3, 2,1]
l = len(arr)
res = []

for i in arr:
    cnt = 0
    try:
        cut = min(filter(lambda i: i > 0, arr))
    except ValueError:
        break
    for j in range(l):
        if(arr[j]==0):
            continue
        arr[j] = arr[j]-cut
        cnt+=1
    res.append(cnt)
print(res)
 
