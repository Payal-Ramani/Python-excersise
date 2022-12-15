numbers = [9, 4, 8, 10, 2, 4, 8, 3, 14, 4, 8]
# Take input from user
user_input = int(input("Enter the number :"))            
            
# Get pair which sum is equal to the user input
to_get_value_pair = [(num1,numbers[num2]) for num2 in range(len(numbers)) for num1 in numbers if num1+numbers[num2] == user_input]

# To remove duplicate
set_remove_duplicate = set(to_get_value_pair)

# Final output as we required after removing pair which meant to be same
set_remove_same_sum_tuple = set(tuple(sorted(item)) for item in set_remove_duplicate)
print(set_remove_same_sum_tuple)