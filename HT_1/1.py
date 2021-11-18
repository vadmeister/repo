#Task1. Write a script which accepts a sequence of comma-separated numbers from user and generate a list and a tuple
numbers = input("Input comma separated numbers here: ")
list = numbers.split(",")
tuple = tuple(list)
print('List : ',list)
print('Tuple : ',tuple)