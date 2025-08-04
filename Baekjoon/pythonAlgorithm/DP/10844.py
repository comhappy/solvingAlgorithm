# 쉬운 계단 수

n = int(input())

if n == 1:
    print(9)
else:
    answer = [[1 for _ in range(10)] for _ in range(n)]	# 2차원 배열을 통한 계단 수 찾기
    answer[0][0] = 0	# 맨 앞의 숫자는 0이 될 수 없음

    for i in range(1, n):
        for j in range(10):
            if j == 0:	# 1의 자리가 0 인경우
                answer[i][j] = answer[i - 1][j + 1]
            elif j == 9:	# 1의 자리가 9 인경우
                answer[i][j] = answer[i - 1][j - 1]
            else:           
                answer[i][j] = (answer[i - 1][j - 1] + answer[i - 1][j + 1])

    print(sum(answer[n - 1]) % 1000000000)