# DSLR

from collections import deque
import sys
input = sys.stdin.readline

def D(n):
    nx = (n * 2) % 10000

    return nx

def S(n):
    if n == 0:
        return 9999
    else:
        return n - 1

def L(n):   # 왼쪽 shift
    nx = (n * 10 + n // 1000) % 10000

    return nx

def R(n):   # 오른쪽 shift
    nx = n // 10 + (n % 10) * 1000
    
    return nx

def BFS(n):
    que = deque()
    que.append([n, list()])
    visited[n] = 1

    while(que):
        number, order = que.popleft()

        if number == B:
            print(order)
            return
        else:
            nx = D(number)
            if visited[nx] == 0:
                order.append("D")
                que.append([nx, order])
                visited[nx] = 1

            nx = S(number)
            if visited[nx] == 0:
                order.append("S")
                que.append([nx, order])
                visited[nx] = 1

            nx = L(number)
            if visited[nx] == 0:
                order.append("L")
                que.append([nx, order])
                visited[nx] = 1

            nx = R(number)
            if visited[nx] == 0:
                order.append("R")
                que.append([nx, order])
                visited[nx] = 1


t = int(input())

for _ in range(t):
    A, B = map(int, input().split())
    visited = [0 for _ in range(10000)]

    BFS(A)