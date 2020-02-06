import sys

count = int(input())
result = []
for i in range(count):
    a, b = map(int, sys.stdin.readline().split())
    print(a+b)
