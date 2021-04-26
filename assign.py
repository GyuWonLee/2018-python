import random
num = random.sample(range(000,999),3)

try_cnt = 0
str_cnt = 0
ball_cnt = 0

print("♡숫자 야구게임♡")
print("-"*10)
print("규칙 : 1에서 9사이 안 겹치는 숫자 3개 입력 : ")

while (str_cnt < 3):
    num = input("숫자를 입력하세요 : ")
    if(num [0] == num [1] == num[2]):
        print("각기 다른 숫자 3개를 입력하세요")
        try_cnt += 1
        continue
    elif (num [0] == num [1]):
        print("각기 다른 숫자 3개를 입력하세요")
        try_cnt += 1
        continue       
    elif (num [0] == num [2]):
        print("각기 다른 숫자 3개를 입력하세요")
        try_cnt += 1
        continue
    elif (num [1] == num [2]):
        print("각기 다른 숫자 3개를 입력하세요")
        try_cnt += 1
        continue
    else:
        pass
    
    
 
    for i in range(0, 3):
        for j in range(0, 3):
            if(num[i] == str(num[j]) and i == j):
                str_cnt += 1
            else:
                ball_cnt += 1
        print(str_cnt,"스타라이크",ball_cnt,"볼")
        try_cnt += 1
        
print(try_cnt,"번만에 스트라이크")