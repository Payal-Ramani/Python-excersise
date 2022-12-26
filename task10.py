from math import ceil,floor
# **_**
# *___* 
# _____ 
# *___*
# **_**
# #number 1 : 
n= int(input("enter the number of line in which you want this pattern :"))
for index in range(1,n+1):
    star = abs(ceil((n/2) - index)) % (n)
    space = n - 2*star
    print('*'*star,end='')
    print('_'*space,end='')
    print('*'*star,end='\n')
print()

#__*__ 
#_***_
#***** 
#_***_
#__*__
# number 2 :
for index in range(1,n+1):
    space2 = abs(ceil((n/2) - index)) % (n)
    star2 = n - 2*space2
    print('_'*space2,end='')
    print('*'*star2,end='')
    print('_'*space2,end='\n')
print()

# number 3 :
# * 
# **
# *_*
# *__* 
# *****
for line in range(n):
    if line == 0 or line == n-1:
        print("*"*(line+1),end="\n")
    elif line == n-(n-1):
        print("**")
    else:
        print("*",end="")
        print("_"*(line-1),end="")
        print("*",end="\n")
print()

 # number 4 :
 # ***** 
 # *___* 
 # *___* 
 # *___* 
 # *****
for line in range(n):    
    if line == 0 or line == n-1:
        print("*"*n,end="\n")
    else:
        print("*",end='')
        print("_"*(n-2),end='')
        print("*",end='\n')
print()

# number 5:
# 1 
# 2 3
# 4 5 6
# 7 8 9 10
# 11 12 13 14 15
num = 1
for i in range(1,n+1):
    for j in range(i):
        print(num,end=" ")
        num += 1
    print("\n")