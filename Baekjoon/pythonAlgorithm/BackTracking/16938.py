# 캠프 준비

def DFS(index, quiz):
    global answer, sum_of_quiz

    if len(quiz) >= 2:  # 선택된 문제가 2개 이상일 때
        if l <= sum_of_quiz <= r and quiz[-1] - quiz[0] >= x:
            answer += 1

    for i in range(index, n):
        quiz.append(A[i])
        sum_of_quiz += A[i]
        DFS(i + 1, quiz)
        quiz.pop()
        sum_of_quiz -= A[i]

    
n, l, r, x = map(int, input().split())
A = list(map(int, input().split()))
A.sort()    # 난이도 차이 계산을 위한 정렬

# n개의 문제 중 2개 이상을 고르는 방법
sum_of_quiz = 0 # 문제의 합

answer = 0  # 정답 경우의 수
DFS(0, [])
print(answer)