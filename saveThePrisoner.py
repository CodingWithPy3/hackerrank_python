def saveThePrisoner(n, m, s):
   l = (s - 1 + m) % n
   if l == 0:
       l = n
   print(l)
    
t = int(input())
for t_itr in range(t):
    nms = input().split()

    n = int(nms[0])

    m = int(nms[1])

    s = int(nms[2])

    result = saveThePrisoner(n, m, s)
