mo = 678
sum = 0

while (mo > 0):
    na = mo % 10
    mo = mo // 10
    sum = sum + na
    print("나머지/몫/합")
    print(na,mo,sum)
print(sum)