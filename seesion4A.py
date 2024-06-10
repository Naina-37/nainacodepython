#Conditional operator
# ==,!=,>,<,>=,<=
cab_fare = 500
e_wallet = 200
result = e_wallet > cab_fare
print("can I book the cab:" , result)
print(type(result))
# logical operators
email = input("enter email: ")
password = input("enter password :  ")
print("is login success ????")
result = (email == "nainagupta9914@gmail.com") and (password == "john123")
print(result)
otp = 2810
user_otp = int(input("enter the otp recieved"))
print("is otp correct???" , otp == user_otp)
# MEmbership testing
 # is, is not
a = 10
b = 10
print(a==b)
print(a is b)
print(a is not b)