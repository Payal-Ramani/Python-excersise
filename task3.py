from collections import Counter
sentences = ['My name is Ram', 'He is a good person', 'You should be careful while coding', 'He can do better', 'The person is mysterious', 'Jay Shree Ram', 'It is my pen.']

# Here we did spliting of sentences from the list
splited_list = []
for sentence in sentences:
    splited_list.append(sentence.split())
print(splited_list)

# here we put all the string in one list
temp = []
for list in splited_list:
    for string in list :
        temp.append(string)
print(temp)

# finally we get the number of each string
print(Counter(temp))





