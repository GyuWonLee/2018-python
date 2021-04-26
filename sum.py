sum = 0
sum_exp = '' #문자열 선언
for x in range(10):
    sum = sum + x
    sum_exp = sum_exp +'+'+ str(x)
    print(sum_exp)
print(sum)