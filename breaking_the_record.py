def breakingRecords(scores):
    best=scores[0]
    worst=scores[0]
    c1=c2=0
    for scr in scores:
        
        if(scr>best):
            best=scr
            c1+=1
        if(scr<worst):
            worst=scr
            print(worst)
            c2+=1
    return [c1,c2]
if __name__ == '__main__':

    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)
    print(result)
