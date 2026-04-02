s = input()

cleaned = s.lower().replace(" ", "")

if cleaned == cleaned[::-1]:
    print(True)
else:
    print(False)