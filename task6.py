string = 'PQRQRQRQ' 
substring = 'QRQ'

count = 0
for index in range(len(string)-(len(substring)-1)):
    if substring in string[index:index+len(substring)]:
        count += 1
print(count)