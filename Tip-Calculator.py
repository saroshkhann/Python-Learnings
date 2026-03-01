print("Welcome to the Tip Calculator!")

totalBill = float(input("What was the total bill? $"))

tipGiven = float(input("How much tip would you like to give? 10, 12, or 15?"))
tip = (totalBill * (tipGiven / 100)) + totalBill
splitBill = int(input("How many people will split the bill?"))
splitting = tip / splitBill
finalBill = round(splitting,2)
billPay = print(f"Each person should pay${finalBill}")