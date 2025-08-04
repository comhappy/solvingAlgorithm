# 영재의 시험

def DFS(question_num, pre_answer, num_of_pre_answer):
    global result

    if num_of_pre_answer == 2:    # 3개의 정답이 오는 경우
        return
    elif question_num == len(answer):
        if sum(score) >= 5:
            result += 1
        return
    else:
        for i in range(1, 6):   # 선택하는 번호
            if i == answer[question_num]:   # 정답을 맞춘 경우
                score[question_num] = 1
                if i == pre_answer:
                    DFS(question_num + 1, i, num_of_pre_answer + 1)
                else:
                    DFS(question_num + 1, i, 0)
            else:
                if i == pre_answer:
                    DFS(question_num + 1, i, num_of_pre_answer + 1)
                else:
                    DFS(question_num + 1, i, 0)

            score[question_num] = 0
        return


answer = list(map(int, input().split()))
result = 0
score = [0 for _ in range(len(answer))]
DFS(0, 0, 0)
print(result)