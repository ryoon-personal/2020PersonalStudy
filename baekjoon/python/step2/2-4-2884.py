num = input().split()
hour = int(num[0])
minute = int(num[1])

number = hour*60+minute-45

if number < 45:
    number = number+60*24

alertHour = int(number/60)
alertMinute = number % 60

print(alertHour, alertMinute)
