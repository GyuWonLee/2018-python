s = input("문자열을 입력하세요 : ")
alpha = 'abcdefghijklmnopqrstuvwxyzABC'
number = '0123456789'
a_num = 0
s_num = 0
n_num = 0

for letter in s:
    if letter in alpha:
        a_num += 1 
    elif letter == '':
        s_num += 1
    elif letter in number:
        n_num += 1
        
print(a_num)
print(s_num)
print(n_num)