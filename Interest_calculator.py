# compound interest calculator

while True:
    principle = input("Enter the principle amount in rupees: ")

    try:
        principle = float(principle)
        if principle <= 0:
            print("Principle can't be negative or zero")
        else:
            break

    except ValueError or ZeroDivisionError:
        print("Only numbers are allowed")

while True:
    rate = input("Enter the rate: ")
    try:
        rate = float(rate)
        if rate <= 0:
            print("rate can't be negative or zero")
        else:
            break

    except ValueError or ZeroDivisionError:
        print("Only numbers are allowed")

while True:
    time = input("Enter the time in years: ")
    try:
        time = float(time)
        if time <= 0:
            print("time can't be negative or zero")
        else:
            break

    except ValueError or ZeroDivisionError:
        print("Only numbers are allowed")

total = principle * pow((1 + rate/100), time)
print(f"Balance after {time} year/s: Rs. {total:.2f}")
