from functools import reduce

def multi(x, y):
    return x * y

numbers=[1,2,3,4,5]

product = reduce(multi, numbers)

print(product)