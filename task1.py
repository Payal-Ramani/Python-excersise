list_of_numbers = [2, 4, 5, 2, 12, 44, 5, 1, 2, 3]
length_of_list = len(list_of_numbers)

first_three_numbers = []
for i in range(3):
    first_three_numbers.append(list_of_numbers[i])

def Display_sum_of_odd_numbers(list):
    sum = 0
    for n in list:
        if n % 2 != 0:
            sum += n
    return sum


empty_list_forCountDuplicates = []
for num in list_of_numbers:
    if list_of_numbers.count(num) > 1:
        if num not in empty_list_forCountDuplicates:
            empty_list_forCountDuplicates.append(num)

list_without_duplicates = set(list_of_numbers)

input_from_user = input(" A : length of list \n B : Displays first 3 numbers \n C : Displays sum of odd numbers \n D : Number of Duplicate numbers \n E : Display list without duplicate numbers \n Enter Your choice from A,B,C,D,E: " )

if(input_from_user == "A"):
    print(length_of_list)
if(input_from_user == "B"):
    print(list_of_numbers[:3])
if(input_from_user == "C"):
    print(Display_sum_of_odd_numbers(list_of_numbers))
if(input_from_user == "D"):
    print(len(empty_list_forCountDuplicates))
if(input_from_user == "E"):
    print(list(list_without_duplicates))
