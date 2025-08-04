# 연산자 끼워넣기(2)

def DFS(oper, num):
    global answer_max, answer_min

    if oper == n - 1:   # 계산이 끝난 경우
        answer_max = max(answer_max, num)
        answer_min = min(answer_min, num)

        return
    else:
        for i in range(4):
            if oper_len[i] != 0:    # 연산자가 남아있는 경우
                oper_len[i] -= 1
                
                if i == 0:
                    DFS(oper + 1, num + A[oper + 1])
                elif i == 1:
                    DFS(oper + 1, num - A[oper + 1])
                elif i == 2:
                    DFS(oper + 1, num * A[oper + 1])
                elif i == 3:
                    if num * A[oper + 1] < 0:   # 양수 음수가 각각 하나씩 있는 경우
                        DFS(oper + 1, (abs(num) // abs(A[oper + 1])) * (-1))
                    else:
                        DFS(oper + 1, num // A[oper + 1])

                oper_len[i] += 1


n = int(input())
A = list(map(int, input().split())) # 수열 A
oper_len = list(map(int, input().split()))  # 연산자 개수(+, -, x, //)

answer_max = -1000000001
answer_min = 1000000001

DFS(0, A[0])

print(answer_max)
print(answer_min)