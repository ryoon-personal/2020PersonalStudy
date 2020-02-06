num = input().split()
num = [int(i) for i in num]

num.remove(max(num))
num.remove(min(num))
print(num[0])
