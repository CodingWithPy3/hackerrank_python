if __name__ == '__main__':
    nm=[]
    grd=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        nm.append(name)
        grd.append(score)

uni=[]
for i in grd:
    if not(i in uni):
        uni.append(i)

uni.remove(min(uni))
uni.sort()
low=uni[0]
res=[]
for i in range(len(grd)) :
    if(grd[i]==low):
        res.append(nm[i])
res.sort()

print (*res, sep = "\n")
