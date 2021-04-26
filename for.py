result = []
for i in range(1,11):
    if i%2 ==0:
        result.append(i**2)
print(result)

f1 = [i**2 for i in range(1,11) if i%2 ==0]
print(f1)