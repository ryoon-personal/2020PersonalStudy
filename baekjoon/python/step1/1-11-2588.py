num1 = input()
num2 = input()

tempNum = []
for i in reversed(num2):
    tempNum.append(int(i)*int(num1))

for i in range(len(tempNum)):
    print(tempNum[i])

exp = []
exponent = list(range(len(tempNum)))
for i in exponent:
    exp.append(10**i)

result = 0
for i in range(len(tempNum)):
    result = result+exp[i]*tempNum[i]
print(result)
