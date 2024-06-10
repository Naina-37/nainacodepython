#condition 1:you can apply promo code iff min amount is 500 or amount should greater than 500
#Condition2:
promo_code = "GET200"
min_amount = 500
amount = float(input("enter you amount:"))

if amount>min_amount:
    print("you acn apply promo code" , promo_code)
    amount-=200
    print()
else:
    print("you can not apply promo code",promo_code)
    print("add items worth",(min_amount-amount),"moreee.....")
