
# Complete the utopianTree function below.



def utopianTree(n):
    height=1
    for i in range(1,n+1):
        if(i%2==1):
            #double
            height=height*2
        else:
            #add 1
            height=height+1
    print(height)

if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())
        result = utopianTree(n)
        
