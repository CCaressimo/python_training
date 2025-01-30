# print("nunber: " + str(len(input("enter"))))

print("Welcome to the tip calculator!")
bill = float(input("What was your total bill?\n$"))
tip = float(input("What perentage of tip did you give?\n%"))
people = int(input("How many people to split the bill?\n"))
bill_with_tip = tip / 100 * bill + bill
bill_split = bill_with_tip / people
print("Each person should pay: " + "$" + str(round(bill_split, 2)))