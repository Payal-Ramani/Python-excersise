import functools
class Numbers:
    def __init__(self,numbers):
        self.numbers = numbers 

    def get(self):
        return self.numbers

    def modify_by_multiplying(self, func : lambda x :x):
        self.func = func
        return list(map(self.func,self.numbers))

    def filter_by_dividing_number(self, filter_func: lambda x: x):
        self.filter_func = filter_func
        return list(filter(self.filter_func,self.numbers))

    def compound_the_numbers(self, reduce_func: lambda compound, d: compound + d):
        self.reduce_func = reduce_func
        return functools.reduce(self.reduce_func,self.numbers)
    
    def sort(self):
        return  sorted(self.numbers)
       
if __name__ == "__main__":
    numbers = [2, 5, 1, 66, 22, 11, 10]
    
n1 = Numbers(numbers)
print(f"Numbers : {n1.get()}")

mul_num = int(input("enter the number with which you want to multiply the list of numbers : "))
print(f"Doubled Numbers : {n1.modify_by_multiplying(func = lambda x : x * mul_num)}")

div_num = int(input("enter the number with which you want to divide the list of numbers : "))
print(f"Filtered Numbers : {n1.filter_by_dividing_number(filter_func = lambda x : x % div_num == 0)}" )

print(f"Compounded Value : {n1.compound_the_numbers(reduce_func = lambda x , y : x + y )}")
print(f"Sorted List : {n1.sort()}")