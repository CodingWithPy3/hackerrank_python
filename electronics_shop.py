##
##def getMoneySpent(keyboards, drives, b):
##    l=[]
##    for i in keyboards:
##        for j in drives:
##          l.append(i+j)
##
##    l.sort(reverse=True)
##    
##    for i in l:
##        if(i<=b):
##            return(i)
##    return(-1)        
##if __name__ == '__main__':
##
##    bnm = input().split()
##
##    b = int(bnm[0])
##
##    n = int(bnm[1])
##
##    m = int(bnm[2])
##
##    keyboards = list(map(int, input().rstrip().split()))
##
##    drives = list(map(int, input().rstrip().split()))
##
##
##    moneySpent = getMoneySpent(keyboards, drives, b)
##    #print(moneySpent )
##

n=5
r=1
while(not(n==0)):
    r*=n
    n-=1
print(r)







