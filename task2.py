num = input()
power = len(num)

total = 0
for digit in num:
    total += int(digit) ** power

if total == int(num):
    print(True)
else:
    print(False)