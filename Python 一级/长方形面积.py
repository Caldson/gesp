a = int(input())
result = 0
for i in range(1,a+1):
    for j in range(1,a+1):
        if i*j==a and (i >= j):
            result += 1
print(result)