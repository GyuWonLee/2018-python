"""
201712963 이규원
python 과제2
"""

num = int(input("정수를 입력하세요 : "))
convert = int(input("변환할 진법을 입력하세요 (2, 8, 16) : "))

if (convert==2): # 이진법 일 경우
    print("2진법 : ", bin(num)[2:])
elif (convert==8):
    print("8진법 : ", oct(num)[2:])
elif (convert==16):
    print("16진법 : ", hex(num)[2:])
else:
    print("잘못입력하셨습니다.")
    
    