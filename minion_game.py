S = input()
n = len(S)

stuart = 0
kevin = 0

for i in range(n):
    print(S[i])
    if S[i] in ('A', 'E', 'I', 'O', 'U'):
        kevin += n - i
        print ('Kevin %d' %kevin)
    else:
        stuart += n - i
        print ('Stuart %d ' %stuart)

if kevin > stuart:
    print ('-----------Kevin %d' %kevin)
elif stuart > kevin:
    print ('-----------Stuart %d ' %stuart)
else:
    print ('Draw')
