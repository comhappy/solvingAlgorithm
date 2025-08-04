# 매직스타

def check_star():
    # 6줄 검사
    #    0
    # 1 2 3 4 
    #  5   6
    # 7 8 9 10
    #    11
    number = list()

    number.append(star[0] + star[2] + star[5] + star[7])
    number.append(star[7] + star[8] + star[9] + star[10])
    number.append(star[0] + star[3] + star[6] + star[10])
    number.append(star[1] + star[2] + star[3] + star[4])
    number.append(star[1] + star[5] + star[8] + star[11])
    number.append(star[11] + star[9] + star[6] + star[4])

    for i in number:
        if i != 26:
            return False
        
    return True

def print_star():
    k = 0

    for i in range(5):
        for j in range(9):
            if hexa[i][j] != ".":
                print(chr(star[k] + 64), end='')
                k += 1
            else:
                print(hexa[i][j], end='')
        print()


def DFS(index, depth):
    global answer

    if depth == n:
        if check_star():
            print_star()
            answer = 1
        return
    elif answer == 0:
        if star[index] != 0:
            DFS(index + 1, depth)
        else:
            for i in range(1, 13):
                if number[i] == 0:
                    number[i] = 1
                    star[index] = i
                    DFS(index + 1, depth + 1)
                    number[i] = 0
                    star[index] = 0
        return
                

hexa = list(list(input()) for _ in range(5))
star = list()   # 1~12까지
number = [0 for _ in range(13)]
n = 0
answer = 0

for i in range(5):
    for j in range(9):
        if hexa[i][j] == "x":
            star.append(0)
            n += 1
        elif hexa[i][j] != ".":
            star.append(ord(hexa[i][j]) - 64)
            number[ord(hexa[i][j]) - 64] = 1

# 나머지 숫자 채우기
DFS(0, 0)

