# 0 만들기

import sys
input = sys.stdin.readline

def DFS(num, depth, oper):
    if depth == n:
        exp = ""

        for i in range(n - 1):
            exp += str(i + 1)
            if oper[i] == " ":
                exp += ""
            else:
                exp += oper[i]

        exp += str(n)

        if eval(exp) == 0:
            for i in range(n - 1):
                print(i + 1, end='')
                print(oper[i], end='')
            print(n)
    else:
        oper.append(" ")
        DFS(num + 1, depth + 1, oper)
        oper.pop()

        oper.append("+")
        DFS(num + 1, depth + 1, oper)
        oper.pop()

        oper.append("-")
        DFS(num + 1, depth + 1, oper)
        oper.pop()
        

t = int(input())

for _ in range(t):
    n = int(input())

    DFS(1, 1, [])
    print()