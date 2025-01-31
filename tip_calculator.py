# print("nunber: " + str(len(input("enter"))))

print("Welcome to the tip calculator!")
bill = float(input("What was your total bill?\n$"))
tip = float(input("What perentage of tip did you give?\n"))
people = int(input("How many people to split the bill?\n"))
tip = tip / 100 * bill
bill_split = (bill + tip) / people
s_bill = "$" + f"{bill:,.2f}"
s_tip = "$" + f"{tip:,.2f}"
s_split = "$" + f"{bill_split:,.2f}"
print(f"""
Bill:       {s_bill:>9}
Gratuity:   {s_tip:>9}
Split:      {s_split:>9}
      """)