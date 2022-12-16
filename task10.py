# **_**
# *___* 
# _____ 
# *___*
 
# **_**

#number 1 : 
n= 5
for line in range(n):
    if line == n-n or line == n-1:
        print("*"*2,end="")
        print("_"*(n-4),end="")
        print("*"*2,end="")
    elif line == n-(n-1) or line == n-2:
        print("*",end="")
        print("_"*(n-2),end='')
        print("*",end="")
    else :
        print("_"*n,end="")
    print("\r")
print('\n')

# __*__ 
# _***_
# ***** 
# _***_
# __*__

# number 2 :

for line in range(n):
    if line == n-n or line == n-1:
        print("_"*2,end="")
        print("*"*(n-4),end="")
        print("_"*2,end="")
    elif line == n-(n-1) or line == n-2:
        print("_",end="")
        print("*"*(n-2),end='')
        print("_",end="")
    else :
        print("*"*n,end="")
    print("\r")
print('\n')

# number 3 :
# * 
# **
# *_*
# *__* 
# *****


for line in range(n):
    if line == n-n or line == n-1:
        print("*"*(line+1),end="\n")
    elif line == n-(n-1):
        print("**")
    else:
        print("*",end="")
        print("_"*(line-1),end="")
        print("*",end="\n")
    
# number 4 :
# ***** 
# *___* 
# *___* 
# *___* 
# *****


for line in range(n):    
    if line == n-n or line == n-1:
        print("*"*n,end="\n")
    else:
        print("*",end='')
        print("_"*(n-2),end='')
        print("*",end='\n')

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
    print("\r")