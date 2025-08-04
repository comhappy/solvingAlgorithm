# 줄어드는 수

def DFS():
    if len(num) > 0:
        result.append(int("".join(map(str, num))))

    for i in range(0, 10):
        if len(num) == 0 or num[-1] > i:
            num.append(i)
            DFS()
            num.pop()
        

n = int(input())

num = list()
result = list()

DFS()

result.sort()

if n > len(result):
    print(-1)
else:
    print(result[n - 1])