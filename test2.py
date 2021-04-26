number = 1234
sum = 0
while number > 0:
    digit = number%10
    print(digit)
    print("-"*40)
    sum = sum + digit
    print(sum)
    print("-"*40)
    number = number // 10
    print(number)
print("자리수의 합은 %d 입니다." % sum)