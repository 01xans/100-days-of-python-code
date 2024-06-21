#Tip Calculator

print("Welcome to the Tip Calculator!")

#Taking input of user's total bill
bill=float(input("What was the total bill? $"))

#Taking input of user's tip percentage
tip=int(input("What percentage would you like to give? 10, 12, or 15?"))

#Taking input of number of people
people=int(input("how many people to split the bill?"))

bill_with_tip= tip/100*bill+bill
bill_per_person= bill_with_tip/people
final_amount="{:.2f}".format(bill_per_person)

#Printing the amount to be paid by each person
print(f"Each person should pay: ${final_amount}")