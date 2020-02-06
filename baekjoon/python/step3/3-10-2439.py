num = int(input())

for i in range(num, 0, -1):
    for j in range(i-1):
        print(" ", end='')
    for k in range(num-i+1):
        print("*", end='')
    print()
