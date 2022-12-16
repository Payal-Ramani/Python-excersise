from collections import Counter
sentences = ['My name is Ram', 'He is a good person', 'You should be careful while coding', 'He can do better', 'The person is mysterious', 'Jay Shree Ram', 'It is my pen.']

# Here we did spliting of sentences from the list
splited_sentence = []
for sentence in sentences:
    splited_sentence.append(sentence.split())
print(splited_sentence)

# here we put all the string in one list
temp = []
for word in splited_sentence:
    for string in word :
        temp.append(string)
print(temp)

# finally we get the number of each string
print(Counter(temp))





