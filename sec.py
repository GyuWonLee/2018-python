#str = input('초를 입력하세요 : ')
#second - int(str)

sec = int(input("몇 시간 몇 분 인지 알려주는 프로그램입니다. 양수를 입력하세요 : "))


min = sec // 60
sec = sec % 60
hour = min // 60
min = min % 60


print(hour,"시간",min,"분",sec,"초")