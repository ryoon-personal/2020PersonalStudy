num, benchmark = map(int, input().split())

sequence = list(map(int, input().split()))

for i in range(num, len(sequence)):
    sequence.pop()
for i in sequence:
    if i < benchmark:
        print(i, end=' ')
