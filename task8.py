numbers = [2, 5, 6, 1, 3, 8, 9, 10]
sorted_numbers = []

# To sort list of numbers
while numbers:
    min = numbers[0]
    for num in numbers:
        if num < min :
            min = num
    sorted_numbers.append(min)
    numbers.remove(min)    
print(sorted_numbers)

