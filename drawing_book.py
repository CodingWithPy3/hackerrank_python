def pageCount(n, p):
    if (n==p):
        return 0
    else:
        return ((((n-p)//2))-1)
    
if __name__ == '__main__':
    n = int(input())
    p = int(input())
    result = pageCount(n, p)
    print(result)
    
    
