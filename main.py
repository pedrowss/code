def int32(x):
    if(x < -2147483648 or x > 2147483647):
        return 1


def reverse(x):
    if(int32(x)):
        return 0

    x = str(x)

    x = x[::-1]

    if(x[len(x)-1] == '-'):
        x = x[:len(x) - 1]
        x = "-" + x

    x = int(x)

    if(int32(x)):
        return 0

    x = str(x)

    if(len(x) == 1 and x[0] == '0'):
        return 0

    if(x[0] == '0'):
        x = x[1:len(x)]

    # if(x[len(x)-1] == '-'):

    return int(x)


x2 = 1534236469
# 1534236469
# x2 = -123
# x = str(x2)
print(reverse(x2))
