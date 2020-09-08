##n=int(input())
##ar=[]
##for i in range(n):
##    ar.append(int(input()))
##ar.sort()
##ind=[]
##c=1
##for i in range(n-1):
##    if(not(ar[i]==ar[i+1])):
##        ind.append(ar[i])
##        c=c+1
##ind.append(ar[len(ar)-1])
##
##res=0
##for i in ind:
##    c=ar.count(i)
##    res=res+(c//2)
##print(res)


height = 0
prev_height = 0
cnt = 0
n = input()
s = raw_input().strip()
for i in range(len(s)):
    if (s[i] == 'U'):
        height += 1
    elif s[i] == 'D':
        height -= 1
    if height == 0 and prev_height < 0:
        cnt += 1
    prev_height = height
print (cnt)
