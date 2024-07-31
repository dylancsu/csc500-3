pretax = float(input("Enter the restaurant cost"))
tax = pretax * 1.07
tip = pretax * 1.18
print(f"With a ${tax} tax and a ${tip} tip, the total comes to ${pretax+tax+tip}")
