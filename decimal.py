num = int(input("정수를 입력하세요 : "))
result = ""

while(num > 0):
    remainder = num % 2
    num = num // 2
    result = str(remainder) + result
print(result)