def power(num,y=2):
    return num**2

print(power(4))

def max_num(num1, num2):
    if num1 > num2:
        return num1
    else:cxvddgs
        return num2



print(max_num(3,4))


def maxn(l):
    maxi = l[0]
    for i in l:
        if i > maxi:
            maxi = i
    return maxi


a = [-4, -8, -2, -9, -6]
print(maxn(a))


def power(num,num2):
    return num**num2

def powernum(x,y):
    result = 1 # 곱해나가는 것 
    for i in range(y):
        result = result * x
    return result

print(power(4,3))
print(powernum(4,3))