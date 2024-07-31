pretax = float(input("Enter the restaurant cost: "))
tax = pretax * 0.07
tip = pretax * 0.18
print(f"With a ${tax:.2f} tax and a ${tip:.2f} tip, the total comes to ${(pretax+tax+tip):.2f}")
