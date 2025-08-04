N = int(input())
number = list()

for i in range(N):
    num = int(input())
    number.append(num) 

#버블정렬
for i in range(N-1, 0, -1):
    for j in range(i):
        if number[j] > number[j+1]:
            temp = number[j]
            number[j] = number[j+1]
            number[j+1] = temp

for i in range(len(number)):
    print(number[i])