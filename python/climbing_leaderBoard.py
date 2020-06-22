def climbingLeaderboard(scores, alice):
    scores = sorted(list(set(scores)))
    ind = 0
    res = []
    l = len(scores)
    for sc in alice:
        while (l > ind and sc >= scores[ind]):
            ind += 1
        res.append((l+1)-ind) 
    return res
    
    
if __name__ == '__main__':
    scores_count = int(input())
    scores = list(map(int, input().rstrip().split()))
    alice_count = int(input())
    alice = list(map(int, input().rstrip().split()))
    result = climbingLeaderboard(scores, alice)
    print(result)


##7
##100 100 50 40 40 20 10
##4
##5 25 50 120
