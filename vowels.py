s = input("문자열을 입력하세요 : ")
vowels = "aeiouAEIOU"
v = ['a','e','i','o','u']
number = 0
cnt = 0
result = ""
for letter in s:
    if letter in vowels:
        result += letter
        cnt +=1
        
        
print(result)
print("모음의 개수 : ",cnt)
print(len(result))

