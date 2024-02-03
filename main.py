
bill = float(input("Enter the amount of your bill? "))
split = int(input("How many of people split the bill? "))
precentage = int(input("Enter the tip percentage 10/12/15"))

totbill = ((bill + (bill * precentage/100)))
totpayable = round(totbill/split)

print(f"Each one should pay {totpayable}$ for the meal.")