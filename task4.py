# to find n-th element of fibonacci series 
num = int(input("Enter the number to see that which number is that position : "))
def func_for_fib(num):
    if num == 0 or num == 1:
        return num
    return func_for_fib(num-1) + func_for_fib(num-2)
print(func_for_fib(num))


# solution of reducing time complexity
dictinary_for_store_fib_value = { 0 : 0 , 1 : 1}

num1 = int(input("Enter the number to find the number at that position :"))
def func_for_fib_sol(num):
    if num in dictinary_for_store_fib_value:
        return dictinary_for_store_fib_value[num]
    
    dictinary_for_store_fib_value[num] = func_for_fib_sol(num-1) + func_for_fib_sol(num-2)
    return dictinary_for_store_fib_value[num]

list_of_fib_seq = [func_for_fib_sol(n) for n in range(num1+1)]
print(list_of_fib_seq[-1])

# second recursive functon question
numbers = [23, 44, 5, 67, 1, 1, 2, 4, 5]

def rec_fun_for_sum(size):
    if size == 0:
        return 0
    return numbers[size-1] + rec_fun_for_sum(size-1)
print(rec_fun_for_sum(len(numbers))) 
   
# Implementation with using different method 
def rec_func_for_list_sum(num_list_for_sum):
    if len(num_list_for_sum) == 0:
        return 0
    removed_element = num_list_for_sum.pop()
    return removed_element + rec_func_for_list_sum(num_list_for_sum)
print(rec_func_for_list_sum(numbers))


