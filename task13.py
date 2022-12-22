import functools
class Numbers:
    def __init__(self,numbers):
        self.numbers = numbers 

    def get(self):
        return self.numbers

    def change_original_values(self, func : lambda x: x):
        self.func = func
        doubled_values = map(self.func,self.numbers)
        return list(doubled_values)

    def filter_values(self, filter_func: lambda x: x):
        self.filter_func = filter_func
        filtered_values = filter(self.filter_func,self.numbers)
        return list(filtered_values)

    def compound_the_numbers(self, reduce_func: lambda compound, d: compound + d):
        self.reduce_func = reduce_func
        reduced_values = functools.reduce(self.reduce_func,self.numbers)
        return reduced_values
    
    def sort(self):
        return  sorted(self.numbers)
       
if __name__ == "__main__":
    numbers = [2, 5, 1, 66, 22, 11, 10]
    
n1 = Numbers(numbers)
print(f"Numbers : {n1.get()}")
print(f"Doubled Numbers : {n1.change_original_values(func = lambda x : x*2)}")
print(f"Filtered Numbers : {n1.filter_values(filter_func = lambda x : x % 2 == 0)}" )
print(f"Compounded Value : {n1.compound_the_numbers(reduce_func = lambda x , y : x + y )}")
print(f"Sorted List : {n1.sort()}")