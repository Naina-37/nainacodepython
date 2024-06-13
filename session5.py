"""
ZOMATO :20% OFF
MIN VALUE: 300
BINGO:50%
:MIN VALUE:500
:MAX DISCOUNT:100
 # Indentation: PEP (Python Enhancement Proposal)
    # https://peps.python.org/pep-0001/
"""

promo_code = input("Enter promo code: ")
amount = float(input("Enter the amount: "))

if promo_code == "ZOMATO":
    print("Promo code applied: ZOMATO")
    if amount > 300:
        discount = 0.20 * amount
        print("ZOMATO applied", discount)
        print("You can pay:", amount - discount)
    else:
        print("Amount is less, please add items worth", 300 - amount, "more")
elif promo_code == "BINGO":
    print("BINGO can be applied")
    if amount > 500:
        discount = 0.50 * amount
        if discount > 100:
            discount = 100
        print("BINGO applied", discount)
        print("You can pay:", amount - discount)
    else:
        print("Amount is less, please add items worth", 500 - amount, "more")
else:
    print("Invalid promo code")
