def my_sum(a, b):
    return a + b

total = my_sum(1,2)
print(total) # 3

def my_sum(*args):
    result = 0
    # Iterating over the Python args tuple
    for x in args:
        result += x
    return result

total = my_sum(1,2,3,5,7)
print(total) # 18

def my_product(a, b):
    return a * b

total = my_product(2,3)
print(total) # 6

def my_product(*args):
    result = 1 # Must be 1 as 0*2 = 0
    # Iterating over the Python args tuple
    for x in args:
        result *= x
    return result

total = my_product(2,3,4,5)
print(total)
