h, m, s = int(input()), int(input()), int(input())
s += int(input())
while s>=60:
    s -= 60;m += 1
while m>=60:
    m -= 60;h += 1
while h>=24:
    h -= 24
print(f"{h} {m} {s}")