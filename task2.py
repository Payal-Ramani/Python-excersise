names = ['Smith', 'Johnson', 'Williams', 'Jones', 'Brown', 'Davis', 'Miller', 'Wilson', 'Moore', 'Taylor', 'Anderson', 'Thomas', 'Jackson', 'White']

# Print the entire list
print("Names:",names)

# Print the length of each element of the list
names_length = [len(name) for name in names]
print("Name lengths : ",names_length)

unique_name_lengths = list(set(names_length))
my_dict = {}

for num in unique_name_lengths:
    my_dict[num] = names_length.count(num)

sorted_dict = sorted(my_dict.items()) #this sort by key 
# sorted_dict = sorted(my_dict.items(),key = lambda i : i[1]) # this sort by value

most_frequent_3 = sorted_dict[:3]
least_frequent_3 = sorted_dict[-3:]

# To print the most three frequent lengths of the list:
print("The three most frequent name lenghts are: ")

for key,value in most_frequent_3:
    for_store_filtered_names = [name for name in names if len(name) == key]
    print(f"{value} names of length {key} = {for_store_filtered_names} ")

# To print three least frequent lengths of the list
print("The three least frequent name lenghts are: ")
for key,value in least_frequent_3:
    for_store_filtered_names = [name for name in names if len(name) == key]
    print(f"{value} names of length {key} = {for_store_filtered_names} ")


