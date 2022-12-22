import functools
list_of_numbers = [2, 4, 5, 2, 12, 44, 5, 1, 2, 3]

# TO find the length of list -----------------------
length_of_list = len(list_of_numbers)

# To find sum of odd numbers from the list -------------------------
# making list of odd numbers from list_of_numbers
list_of_odd_numbers = [num for num in list_of_numbers if num % 2 != 0]

# To find number of duplicate elements from the list ----------------------------
empty_list_forCountDuplicates = list(set([num for num in list_of_numbers if list_of_numbers.count(num) > 1]))

# to find list without duplicate elements ---------------------------------
list_without_duplicates = list(set(list_of_numbers))


# Taking input from user 
input_from_user = input(" A : length of list \n B : Displays first 3 numbers \n C : Displays sum of odd numbers \n D : Number of Duplicate numbers \n E : Display list without duplicate numbers \n Enter Your choice from A,B,C,D,E: " )

if(input_from_user == "A"):
    print(length_of_list)
#to find 1st three elemets of the list 
if(input_from_user == "B"):
    print(list_of_numbers[:3])
if(input_from_user == "C"):
    print(functools.reduce(lambda a,b : a+b,list_of_odd_numbers))
if(input_from_user == "D"):
    print(len(empty_list_forCountDuplicates))
if(input_from_user == "E"):
    print(list(list_without_duplicates))




# empty_list_forCountDuplicates = []
# for num in list_of_numbers:
#     if list_of_numbers.count(num) > 1:
#         if num not in empty_list_forCountDuplicates:
#             empty_list_forCountDuplicates.append(num)

# def Display_sum_of_odd_numbers(list):
#     sum = 0
#     for n in list:
#         if n % 2 != 0:
#             sum += n
#     return sum
# print(Display_sum_of_odd_numbers(list_of_numbers))