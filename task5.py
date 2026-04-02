s = input()
k = int(input())

k = k % len(s)

result = s[-k:] + s[:-k]

print(result)

