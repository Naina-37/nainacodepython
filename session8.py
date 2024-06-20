def month_name_to_number(month_name):
    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    return months.index(month_name) + 1

def number_to_month_name(month_number):
    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    return months[month_number - 1]
while True:
    money_loan_amount = int(input("Enter the amount you want to take from bank UPTO 50,000 ONLY:    "))
    
    if money_loan_amount <= 50000:
        print("You can take a loan.")
    else:
        print("You need to wait until you have an upgrade.")
        

    max_payment = int(input("Enter max amount you will pay as your outstanding cost (first installment): "))

    min_first_installment = money_loan_amount * 0.10

    if max_payment == money_loan_amount:
        print("ALL AMOUNT PAID :) in first installment ")
        break  

    if max_payment < min_first_installment:
        print("INVALID EMI amount. Your first installment must be at least 10% of your loan amount. Thank you.")
    else:
        print("You can give an EMI.")
        total_interest = (money_loan_amount - max_payment) * 0.15
        total_amount_to_pay = money_loan_amount - max_payment + total_interest
        print("Total amount of interest:", total_interest, " AMOUNT OF MONEY TO PAY: ", total_amount_to_pay)
        print("You have to pay minimum amount:", money_loan_amount * 0.15)

    second_installment = int(input("Enter the amount for your upcoming installments: "))
    min_second_installment = money_loan_amount * 0.15

    if second_installment < min_second_installment:
        print("You can't pay your amount as the second installment amount must be at least 15% of your loan amount:", min_second_installment)
    else:
        print("You can successfully pay upcoming installments.")
        

        month_start = input("Enter the month name in which you have taken the loan: ")
        start_month_number = month_name_to_number(month_start)
        
        total_installments = 1 + ((money_loan_amount - max_payment) // second_installment)
        remaining_amount = (money_loan_amount - max_payment) % second_installment
        if remaining_amount > 0:
            total_installments += 1

        end_month_number = (start_month_number + total_installments - 1) % 12
    

        if end_month_number == 0:
            end_month_number = 12
        

        end_month_name = number_to_month_name(end_month_number)
        print("You will finish your installments in", end_month_name)
        print("all amount paid :)"   " AMOUNT LEFT TO PAY :)  0 ")
