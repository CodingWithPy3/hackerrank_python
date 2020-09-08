from collections import Counter
words = [input() for _ in range(int(input()))]
res = Counter(words)
print(len(res))
print(*res.values())
