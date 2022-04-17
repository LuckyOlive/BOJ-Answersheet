#-------#
# 10101 #
#-------#

a = int(input())
b = int(input())
c = int(input())

if a == 60 and b == 60 and c == 60 :
    print("Equilateral")
elif a + b + c == 180 :
    if a == b :
        print("Isosceles")
    elif b == c :
        print("Isosceles")
    elif c == a :
        print("Isosceles")
    elif a != b != c :
        print("Scalene")
else :
    print("Error")

#-------#
# 15680 #
#-------#

a = int(input())

if a == 0 :
    print("YONSEI")
elif a == 1 :
    print("Leading the Way to the Future")

