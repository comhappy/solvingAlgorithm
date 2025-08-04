# LCS(Longest Common Subsequence)

def DP():
    answer = [[0 for _ in range(n1 + 1)] for _ in range(n2 + 1)]

    # DP 테이블 체우기
    for i in range(1, n2 + 1):
        for j in range(1, n1 + 1):
            if li2[i - 1] == li1[j - 1]:    # 추가된 문자가 같은 경우
                answer[i][j] = answer[i - 1][j - 1] + 1
            else:
                answer[i][j] = max(answer[i - 1][j], answer[i][j - 1])

    print(answer[n2][n1])

li1 = input()
li2 = input()

n1 = len(li1)
n2 = len(li2)

DP()