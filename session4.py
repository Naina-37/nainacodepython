#operators
# arithmetic operators
#+,-,*,**,/,//,%
product_price = 200
gst_tax = 0.18
price_to_pay = product_price + gst_tax * product_price
number = 10
# result = number/3
result = number // 3
print("result is:", result)
base=2
#result = base *2
result = base ** 3
print("result now is:" ,result)
backet_size = 7
hashcode = 120 % 7
print("hashcode of 120:", hashcode)



#Assignment operator
# =,+=,-=,*=,**=,/=,//=,%=
age=20

#update operation
# age = age + 10
age += 10 #age = age % 3
age %= 3
age -= 1
print("age now is:", age)

#increment and decrement
qty=1
qty += 1 # 2
qty -= 1
qty += 5
qty -= 1
qty **= 2
print("quantity is:", qty)