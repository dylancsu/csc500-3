currenttime = int(input("Enter the current time in hours since midnight: "))

if(currenttime>24 or currenttime<0):
    print("invalid starting time")
else:
    increase = int(input("Enter the number of hours to pass: "))
    if(increase<0):
        print("Invalid increase")
    else:
        print(f"The new time is {(currenttime+increase)%24}")
