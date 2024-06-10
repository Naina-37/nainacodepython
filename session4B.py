# BITWISE OPERATOR
# & , | ,^
num1 = 10
num2 = 8
print("num1 in binary is : ", bin(num1))
print("num2 in binary is : ", bin(num2))
result1 = num1 & num2 #1000
result2 = num1 | num2 #1010
result3 = num1 ^ num2 #0010
print("result: " ,result1)
print("result: " ,result2)
print("result: " ,result3)
# shift operators
# >>,<<
num1 = 8
num2 = 2
# 8 >>  2
result1= num1 >> num2 
print("result right shift is:",result1)
# 8 <<  2
result2= num1 << num2 
print("result left shift is:",result2)
number=-11
result = number >> 2
print(number,">> 2 is:" , result)
#   11
#   0 0 0 0  1 0 1 1
#   >> 2
#   _ _ 0 0  0 0 1 0 -> 2
#   0 0 0 0  0 0 1 0 -> 2

#   -11
#  0 0 0 0  1 0 1 1
#  1 1 1 1  0 1 0 0
#                 1
#  1 1 1 1  0 1 0 1
#  >> 2
#  _ _ 1 1  1 1 0 1
#  1 1 1 1  1 1 0 1
#  0 0 0 0  0 0 1 0
#                 1
#  0 0 0 0  0 0 1 1 -> -3

#  13
#  0 0 0 0   1 1 0 1
#  >> 2
#  _ _ 0 0   0 0 1 1 -> 3

#  -13
#  0 0 0 0   1 1 0 1
#  >> 2
#  _ _ 0 0   0 0 1 1 -> 3