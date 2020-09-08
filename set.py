m=int(input())
mset= set(map(int, input().split()))
n=int(input())
nset= set(map(int, input().split()))

res=(mset-nset).union(nset-mset)
print(res)
for i in res:
    print(i)
