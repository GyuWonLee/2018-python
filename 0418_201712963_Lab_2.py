"""
Title : [실습과제 #4] 룰렛 게임 시뮬레이션
Programer : 201712963 경영정보학과 이규원
Date : 2018-04-18 WED
=================================================================
Outline : 과속티켓을 방지할 속도 변환표를 출력하는 프로그램을 작성하라.

<Seudo Code>
1. 속도 변환표 간략하게 설명한다.
2. mph의 범위를 10부터 140까지의 5씩 증가하여 작성한다.
3. kph = mph * 1.61 의 공식을 이용하여 계산한다.
4. mph의 값과 변환한 kph의 값을 출력한다. (단, kph의 값이 소수일 경우 반올림한다.)
5. 
"""


print("\n             < 속도 변환표 >")
print("\n\n\t mph에서 kph로 변환합니다.")
print("\t변환한 kph의 값이 소수이면 반올림 되어 알려줍니다.\n\n")
print("="*40)
print("   \t mph     |    \t kph     |")
print("="*40)

    
for mph in range(10, 145, 5): # mph
    print("-"*35)
    kph = mph * 1.61 # kph 계산 (mph -> kph)
    print("|   \t", mph,  "\t |      ",round(kph),"\t  |") # mph, kph 출력 (단, 소수이면 kph는 반올림한다)

print("-"*35)
