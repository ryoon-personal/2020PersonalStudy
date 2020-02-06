count = int(input())
result = []
for i in range(count):
    temp = map(int, input().split())
    result.append(list(temp))

sum = 0
for i in range(len(result)):
    for j in range(len(result[i])):
        sum = sum+result[i][j]
    print(sum)
    sum = 0

# count = int(input())
# for i in range(count):
#     a, b = map(int, input().split())
#     print(a+b)
