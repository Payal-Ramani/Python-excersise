from math import ceil
# **_**
# *___* 
# _____ 
# *___*
# **_**

#number 1 : 
n= 9

for i in range(1,n+1):
    if i <= ceil(n/2):
        for j in range(int((n/2)-i+1),0,-1):
            print("*",end='')
        for j in range(1,2*i):
            print("_",end="")
        for j in range(int((n/2)-i+1),0,-1):
            print("*",end='')
        print()
for i in range(1,n+1):
    if i < ceil(n/2):
        for j in range(i):
            print("*",end='')
        for j in range(n-(2*i),0,-1):
            print("_",end='')
        for j in range(i):
            print("*",end='')
        print()

# __*__ 
# _***_
# ***** 
# _***_
# __*__

# number 2 :
for i in range(1,n+1):
    if i <= ceil(n/2):
        for j in range(int((n/2)-i+1),0,-1):
            print("_",end='')
        for j in range(1,2*i):
            print("*",end="")
        for j in range(int((n/2)-i+1),0,-1):
            print("_",end='')
        print()
for i in range(1,n+1):
    if i < ceil(n/2):
        for j in range(i):
            print("_",end='')
        for j in range(n-(2*i),0,-1):
            print("*",end='')
        for j in range(i):
            print("_",end='')
        print()

# # number 3 :
# # * 
# # **
# # *_*
# # *__* 
# # *****


for line in range(n):
    if line == n-n or line == n-1:
        print("*"*(line+1),end="\n")
    elif line == n-(n-1):
        print("**")
    else:
        print("*",end="")
        print("_"*(line-1),end="")
        print("*",end="\n")
    
# # number 4 :
# # ***** 
# # *___* 
# # *___* 
# # *___* 
# # *****


for line in range(n):    
    if line == n-n or line == n-1:
        print("*"*n,end="\n")
    else:
        print("*",end='')
        print("_"*(n-2),end='')
        print("*",end='\n')

# # number 5:
# # 1 
# # 2 3
# # 4 5 6
# # 7 8 9 10
# # 11 12 13 14 15

num = 1
for i in range(1,n+1):
    for j in range(i):
        print(num,end=" ")
        num += 1
    print("\n")