# 암호 만들기

def DFS(st_index):    # st_index는 추가되는 문자열의 인덱스
    if len(answer) == L:
        count = 0

        # 모음 개수
        for i in answer:
            if i in ess:
                count += 1

        # 암호문 조건
        if count >= 1 and (len(answer) - count) >= 2:
            for st in answer:
                print(st, end='')
            print()
    else:
        for i in range(st_index, C):
            answer.append(cyperlist[i])
            DFS(i + 1)
            answer.pop()

    
L, C = map(int, input().split())
cyperlist = list(input().split())

cyperlist.sort()

answer = list()
ess = ['a', 'e', 'i', 'o', 'u']

DFS(0)