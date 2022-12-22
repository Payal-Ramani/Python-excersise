from collections import Counter
sentences = ['My name is Ram', 'He is a good person', 'You should be careful while coding', 'He can do better', 'The person is mysterious', 'Jay Shree Ram', 'It is my pen.']

# Here we did spliting of sentences from the list
splited_sentence = [sentence.split() for sentence in sentences]
print(splited_sentence)
print()
# here we put all the string in one list
string_arr = [string for broken_sentence in splited_sentence for string in broken_sentence]
# print(string_arr)  
# # finally we get the number of each string
print(Counter(string_arr))





