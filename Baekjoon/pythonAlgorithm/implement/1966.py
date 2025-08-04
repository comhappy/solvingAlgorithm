# 프린터 큐

from collections import deque
import sys
input = sys.stdin.readline


t = int(input())
printlist = list()

for _ in range(t):
    n, m = map(int, input().split())
    prio = deque(map(int, input().split()))

    answer = 1
    print_flag = True
    
    max_prio = 1
    for i in prio:
        if max_prio < i:
            max_prio = i
    
    while(print_flag):
        print_0 = prio.popleft()

        if max_prio > print_0:  # 우선순위가 밀리는 경우
            prio.append(print_0)

            if m == 0:  # m의 index 관리
                m = len(prio) - 1
            else:
                m -= 1

        elif m == 0:    # 원하는 것이 출력되는 경우
            print_flag = False

        else:   # 출력하는 경우
            max_prio = 1
            for i in prio:  # 최대 우선순위 변경
                if max_prio < i:
                    max_prio = i    
            answer += 1
            m -= 1
    
    print(answer)