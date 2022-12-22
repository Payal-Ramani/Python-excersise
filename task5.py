from itertools import combinations
numbers = [9, 4, 8, 10, 2, 4, 8, 3, 14, 4, 8]

# Take input from user
user_input = int(input("Enter the number :"))            
            
every_pair_from_numbers_list = set(combinations(numbers,2))
list_of_pair_of_sum = [pair for pair in every_pair_from_numbers_list if sum(pair) == user_input]

# # Final output as we required after removing pair which meant to be same
set_remove_same_sum_tuple = set(tuple(sorted(item)) for item in list_of_pair_of_sum)
print(set_remove_same_sum_tuple)