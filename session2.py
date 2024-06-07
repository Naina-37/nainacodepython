numbers=[10,20,30,40,50]
print(numbers,type(numbers),id(numbers))
print(numbers[1],type(numbers[1]),id(numbers[1]))
#REference COPY OPERATION->copy hashcode
my_numbers=numbers
print(numbers,type(numbers),id(numbers))
numbers[2]=1122
print(id(numbers[2]))
print(id(my_numbers[2]))
del numbers
print(my_numbers)
#print(numbers)