# 1000
a, b = map(int, input().split())
print(a+b)

# 1001
a, b = map(int, input().split())
print(a-b)

# 1271
a, b = map(int, input().split())
c=a//b
d=a%b
print(c)
print(d)

# 1550

x=input()
print(x,16)

# 2338

x = int(input())
y = int(input())

print(x+y)
print(x-y)
print(x*y)

# 2475

a, b, c, d, e = map(int, input().split())

ans = (a**2 + b**2 + c**2 + d**2 + e**2) % 10

print(ans)

# 2558
a = int(input())
b = int(input())
print(a+b)

# 2845

a, b = map(int, input().split())
c,d,e,f,g = map(int, input().split())
key = a * b

for x in (c,d,e,f,g) :
    print(x-key)


