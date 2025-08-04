# # 행운의 문자열

# def DFS(depth, before):
#     global answer

#     if depth == n:
#         answer += 1
#         return
#     else:
#         for i in range(26):
#             if alpha[i] > 0 and before != i:
#                 alpha[i] -= 1
#                 DFS(depth + 1, i)
#                 alpha[i] += 1
#         return

# s = input()
# n = len(s)
# alpha = [0 for _ in range(26)]

# for i in s:
#     alpha[ord(i) - 97] += 1

# answer = 0
# DFS(0, -1)

# print(answer)

# 행운의 문자열

# 행운의 문자열

def DFS(depth, string):
    global answer

    if depth == n:
        answer += 1
        return
    elif string == "":
        for i in range(26):
            if alpha[i] != 0:
                alpha[i] -= 1
                DFS(depth + 1, string + chr(i + 97))
                alpha[i] += 1
    else:
        for i in range(26):
            if alpha[i] != 0 and string[depth - 1] != chr(i + 97):
                alpha[i] -= 1
                DFS(depth + 1, string + chr(i + 97))
                alpha[i] += 1

s = input()
n = len(s)
alpha = [0 for _ in range(26)]

for i in s:
    alpha[ord(i) - 97] += 1

answer = 0
DFS(0, "")
print(answer)