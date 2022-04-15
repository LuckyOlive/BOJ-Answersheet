#--------#
#  5596  #
#--------#

a, b, c, d = map(int, input().split())
S= a + b + c + d

e, f, g, h =  map(int, input().split())
T = e + f + g + h

if S >= T :
    print(S)
else :
    print(T)

#--------#
#  5893  #
#--------#

x = str(input())
y = '0b' + x
z = int(y,2)
a = z * 17
b = bin(a)
c = int(b[2:])
print(c)