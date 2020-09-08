##6
##1 2 2 3 1 2

def pickingNumbers(a):
    mx=0
    frq=[0]*100
    
    for i in a:
        frq[i]=frq[i]+1
    #print(frq)
    
    for i in range(len(frq)-1):
        if(frq[i]+frq[i+1]>mx):
            mx=frq[i]+frq[i+1]

    print(mx)
    
if __name__ == '__main__':
    
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)
    print(result)
