# 2530

h, m, s = map(int, input().split())
t = int(input())

news = s + t
anss = news % 60

newm = m + news // 60
ansm = newm % 60

newh = h + newm //60
ansh = newh % 24

print(ansh, ansm, anss)

# 2588
a = int(input())
b = list(input())

c = int(b[2]) * a
d = int(b[1]) * a
e = int(b[0]) * a

print(c)
print(d)
print(e)
print(c+d*10+e*100)

# 2572

a, b, c = map(int, input().split())
d = sorted([a, b, c])
print(d[0],d[1],d[2])

# 2753

a = int(input())
if (a%4 == 0 and a % 100 != 0 ) :
    print(1)
elif a % 400 == 0 :
    print(1)
else:
    print(0)

# 3004

a = int(input())

if a % 2 != 0 :
    print(((a-1)//2+2)*((a-1)//2+1))
else :
    print((a-(a // 2 - 1)) ** 2)

# 4299

a, b=map(int,input().split())
if a < b:
    print(-1)
else:
    x=(a+b)//2
    y=(a-b)//2
    if x+y==a and x-y==b:
        print(x, y)
    else:
        print(-1)

# 5532

l = int(input())
a = int(input())
b = int(input())
c = int(input())
d = int(input())

if a%c == 0 :
    newac = a//c
else:
    newac = a//c + 1

if b%d == 0 :
    newbd = b//d
else:
    newbd = b//d +1

ans = max(newac,newbd)
print(l-ans)

# 5543

a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())

ham=sorted([a,b,c])
liq=sorted([d,e])

print(int(ham[0]) + int(liq[0]) - 50 )