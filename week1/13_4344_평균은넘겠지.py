import sys
input = sys.stdin.readline

c = int(input())

for _ in range(c):
    # line = list(map(int, input().split()))
    # n = line[0]
    # scores = line[1:n+1]
    # avg = sum(map(float, scores)) / n
    # count = len([x for x in scores if x > avg])
    # ratio = float(count / n) * 100
    # output = round(ratio, 3)
    # print(f"{output:.3f}%")

    n, *scores = map(int, input().split())
    avg = sum(scores) / n
    count = sum(score > avg for score in scores)
    ratio = float(count / n) * 100
    print(f"{ratio:.3f}%")
