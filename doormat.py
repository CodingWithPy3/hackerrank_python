row,width=map(int,input().strip().split(" "))
print(row,width)

for i in range(1,row+1,2):
 print((i*'.|.').center(width,'-'))
print('welcome'.center(width,'-'))
for i in range(row,-1,-2):
 print((i*'.|.').center(width,'-'))
