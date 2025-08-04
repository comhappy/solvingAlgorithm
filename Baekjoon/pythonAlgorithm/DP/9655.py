# 돌 게임

n = int(input())

if n == 1:
    print("SK")
elif n == 2:
    print("CY")
elif n == 3:
    print("SK")
else:
    game = [n for _ in range(n + 1)]

    game[1] = 1
    game[2] = 2
    game[3] = 1

    for i in range(4, n + 1):
        game[i] = min(game[i - 3], game[i - 1]) + 1

    print(game)

    if game[n] % 2 == 0:
        print("CY")
    else:
        print("SK")