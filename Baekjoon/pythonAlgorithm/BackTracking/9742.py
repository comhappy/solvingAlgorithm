# 순열

def DFS(permutation, depth):
    global p_index, answer

    if depth == len(string):
        p_index += 1
        if p_index == index:
            answer = 1
            print("{} {} = {}".format(string, index, permutation))

        return
    elif answer == 0:
        for i in range(len(string)):
            if visited[i] == 0:
                visited[i] = 1
                DFS(permutation + string[i], depth + 1)
                visited[i] = 0


while(1):
    try:
        string, index = input().split()
        index = int(index)

        p_index = 0
        answer = 0
        visited = [0 for _ in range(len(string))]

        DFS("", 0)

        if answer == 0:
            print("{} {} = No permutation".format(string, index))
    except:
        break