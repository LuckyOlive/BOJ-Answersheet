#------#
# 5928 #
#------#

D, H, M = map(int, input().split())
t1 = D*24*60 + H*60 + M
t2 = 11*24*60 + 11*60 + 11
t = t1 - t2
if t < 0:
    print(-1)
else:
    print(t)

#------#
# 6763 #
#------#

lim = int(input())
spd = int(input())
para = spd - lim
if para <= 0 :
    print("Congratulations, you are within the speed limit!")
else :
    if para >= 1 and para <= 20 :
        print("You are speeding and your fine is $100.")
    elif para >= 21 and para <= 30 :
        print("You are speeding and your fine is $270.")
    elif para >= 31 :
        print("You are speeding and your fine is $500.")