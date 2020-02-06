count = int(input())
sum = []
flag = 1
for i in range(count):
    a, b = map(int, input().split())
    print('Case #'+str(flag)+":", a+b)
    flag += 1
