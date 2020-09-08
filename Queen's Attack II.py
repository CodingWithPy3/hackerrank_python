def queensAttack(n, k, r_q, c_q, obstacles):
    print("row")
    for i in range(n,0,-1):
        if ((4,2) < (4,i)):
            print((4,i))

    print("\ncol")
    for i in range(n,0,-1):
        if((3,2) < (i,3)):
            print((i,3))
    print("\n\\")
    for i in range(n,0,-1):
        if(())
    
    
if __name__ == '__main__':
    nk = input().split()
    n = int(nk[0])
    k = int(nk[1])
    r_qC_q = input().split()
    r_q = int(r_qC_q[0])
    c_q = int(r_qC_q[1])
    obstacles = []
    for _ in range(k):
        obstacles.append(list(map(int, input().rstrip().split())))

    result = queensAttack(n, k, r_q, c_q, obstacles)
