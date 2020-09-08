from decimal import *
def print_formatted(number):
    b=bin(number)
    i1=b.find('b')
    l=len(b)-i1-1    
    for i in range(1,number+1):
        print(str(i)+'\t'+str(Decimal(i))[:l]+'\t'+str(oct(i))[l:]+'\t'+bin(i)[l:])

 
if __name__ == '__main__':
    n =2 # int(input())
    print_formatted(n)
