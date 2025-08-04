# 블루레이 만들기, 주어진 시간을 분할하는 최소값 찾기 문제

# 목표값이 최소값이기 때문에 조건을 만족할때 까지 반복해야함
def binary_search(s, e):
    result = e  # 최소값을 찾기 위해 최대값으로 설정

    while(s <= e):   # 시작 인덱스가 종료 인덱스보다 커질때 까지 반복
        mid = (s + e) // 2

        # 조건에 따른 이진탐색, 조건: 인덱스 크기만큼 lesson을 분할했을때의 분할된 개수
        part = check_con(mid)

        

        if part > M:    # 나누어진 부분이 많은 경우, 부분의 크기를 늘려야함
            s = mid + 1
        else:         # 나누어진 부분이 적거나 같은 경우, 부분의 크기를 줄여야함, 최소로 만들어야함
            e = mid - 1
            result = mid


        print("size of bl : " , mid, result)

    return result


def check_con(v):
    # 크기가 v만큼 검사 후 분할되는 개수를 구함
    part = 1
    vol = lesson[0]

    for i in range((len(lesson) - 1)):
        if vol + lesson[i + 1] > v:   # 부분을 나눠야함, 경계에서 검사하자
            part += 1
            vol = lesson[i + 1]
            print(lesson[i], end='  /  ') 
        else:
            vol += lesson[i + 1]

            print(lesson[i], end=" ")

    print(lesson[i + 1], end="              ")

    return part
            

# 데이터 입력
N, M = map(int, input().split())
lesson = list(map(int, input().split()))

s = max(lesson) # 시작 인덱스 값
e = sum(lesson) # 종료 인덱스 값

print(binary_search(s, e))