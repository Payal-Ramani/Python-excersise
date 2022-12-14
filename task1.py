list_of_numbers = [2, 4, 5, 2, 12, 44, 5, 1, 2, 3]
length_of_list = len(list_of_numbers)

first_three_numbers = []
for i in range(3):
    first_three_numbers.append(list_of_numbers[i])

def Display_sum_of_odd_numbers(list):
    sum = 0
    for i in list:
        if i % 2 != 0:
            sum += i
    return sum


empty_list = []
for i in list_of_numbers:
        if list_of_numbers.count(i) > 1:
            empty_list.append(i)
            newlist = list(set(empty_list))

list_without_duplicates = []
for i in list_of_numbers:
    if i not in list_without_duplicates:
        list_without_duplicates.append(i)

input_from_user = input(" A : length of list \n B : Displays first 3 numbers \n C : Displays sum of odd numbers \n D : Number of Duplicate numbers \n E : Display list without duplicate numbers \n Enter Your choice from A,B,C,D,E: " )

if(input_from_user == "A"):
    print(length_of_list)
if(input_from_user == "B"):
    print(first_three_numbers)
if(input_from_user == "C"):
    print(Display_sum_of_odd_numbers(list_of_numbers))
if(input_from_user == "D"):
    print(len(newlist))
if(input_from_user == "E"):
    print(list_without_duplicates)
