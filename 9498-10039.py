#--------#
#  9498  #
#--------#

a = int(input())

if a >= 90 and a <= 100 :
    print("A")
elif a >= 80 and a <= 89 :
    print("B")
elif a >= 70 and a <= 79 :
    print("C")
elif a >= 60 and a <= 69 :
    print("D")
else :
    print("F")

#-------#
# 10039 #
#-------#

a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())

if a <= 40 :
    a = 40

if b <= 40 :
    b = 40

if c <= 40 :
    c = 40

if d <= 40 :
    d = 40

if e <= 40 :
    e = 40

print((a+b+c+d+e)//5)