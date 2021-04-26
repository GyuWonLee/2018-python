import random
com_num = []
for i in range(3):
    while True:
        num = random.randint(0,9)
        if str(num) not in com_num:
            com_num.append(str(num))
            break
        
print(com_num)

count = 0
while True:
    user_num = input("세자리 숫자를 입력하세요 : ")
    count += 1
    strike = 0
    ball = 0
    for i in range(3):
        if user_num[i] == com_num[i]:
            strike += 1
        elif user_num[i] in com_num:
            ball += 1
    print("strike : ",strike,"ball : ",ball)
    if strike == 3:
        print("You Win!")
        print("You have played", count, "time.")
        break
        