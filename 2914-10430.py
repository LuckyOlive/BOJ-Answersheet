# 2914

b, c = map(int, input().split())

a = (c-1) * b

print(a)

# 3003

a, b, c, d, e, f = map(int, input().split())

print(1-a, 1-b, 2-c, 2-d, 2-e, 8-f)

# 3046

R1, S = map(int, input().split())

R2 = 2 * S - R1

print(R2)

# 5337

print(".  .   .")
print("|  | _ | _. _ ._ _  _")
print("|/\\|(/.|(_.(_)[ | )(/.")

# 5338

print("       _.-;;-._")
print("\'-..-\'|   ||   |")
print("\'-..-\'|_.-;;-._|")
print("\'-..-'|   ||   |")
print("\'-..-\'|_.-''-._|")

# 5339

print("     /~\\")
print("    ( oo|")
print("    _\=/_")
print("   /  _  \\")
print("  //|/.\\|\\\\")
print(" ||  \\ /  ||")
print("============")
print("|          |")
print("|          |")
print("|          |")

# 5522

ans = 0

for _ in range(5) :
    ans = ans + int(input())
print(ans)

# 5554

a = int(input())
b = int(input())
c = int(input())
d = int(input())

ansX = int((a+b+c+d)/60)
ansY = (a+b+c+d)%60

print(ansX)
print(ansY)

# 6749

a = int(input())
b = int(input())

c = b-a
ans = b + c
print(ans)

# 8370

a, b, c, d = map(int, input().split())

ans = a * b + c * d

print(ans)

# 8871

a = int(input())

print(2*(a+1), 3*(a+1))


# 9653

print("    8888888888  888    88888")
print("   88     88   88 88   88  88")
print("    8888  88  88   88  88888")
print("       88 88 888888888 88   88")
print("88888888  88 88     88 88    888888")
print("")
print("88  88  88   888    88888    888888")
print("88  88  88  88 88   88  88  88")
print("88 8888 88 88   88  88888    8888")
print(" 888  888 888888888 88  88      88")
print("  88  88  88     88 88   88888888")

# 96654

print("SHIP NAME      CLASS          DEPLOYMENT IN SERVICE")
print("N2 Bomber      Heavy Fighter  Limited    21        ")
print("J-Type 327     Light Combat   Unlimited  1         ")
print("NX Cruiser     Medium Fighter Limited    18        ")
print("N1 Starfighter Medium Fighter Unlimited  25        ")
print("Royal Cruiser  Light Combat   Limited    4         ")

# 10170

print("""NFC West       W   L  T
-----------------------
Seattle        13  3  0
San Francisco  12  4  0
Arizona        10  6  0
St. Louis      7   9  0

NFC North      W   L  T
-----------------------
Green Bay      8   7  1
Chicago        8   8  0
Detroit        7   9  0
Minnesota      5  10  1""")

# 10171

print("""\\    /\\
 )  ( \')
(  /  )
 \\(__)|""")

# 10430

A, B, C = map(int, input().split())

print((A+B)%C)
print(((A%C) + (B%C))%C)
print((A*B)%C)
print(((A%C) * (B%C))%C)

