names = ['Smith', 'Johnson', 'Williams', 'Jones', 'Brown', 'Davis', 'Miller', 'Wilson', 'Moore', 'Taylor', 'Anderson', 'Thomas', 'Jackson', 'White']

# Print the entire list
print("Names:",names)

# Print the length of each element of the list
Name_length = [len(name) for name in names]
print("Name lengths : ",Name_length)

sorted_len = list(set(Name_length))
my_dict = {}

for i in sorted_len:
    my_dict[i] = Name_length.count(i)

sorted_dict = sorted(my_dict.items()) #this sort by key 
# sorted_dict = sorted(my_dict.items(),key = lambda i : i[1]) # this sort by value

most_frequent_3 = sorted_dict[:3]
least_frequent_3 = sorted_dict[-3:]

# To print the most three frequent lengths of the list:
print("The three most frequent name lenghts are: ")

for key,value in most_frequent_3:
    list_for_store_values = []
    for name in names:
        if(len(name) == key):
            list_for_store_values.append(name)
    print(f"{value} names of length {key} = {list_for_store_values} ")

# To print three least frequent lengths of the list
print("The three least frequent name lenghts are: ")
for key,value in least_frequent_3:
    list_for_store_values = []
    for name in names:
        if(len(name) == key):
            list_for_store_values.append(name)
    print(f"{value} names of length {key} = {list_for_store_values} ")





