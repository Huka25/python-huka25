
print("\nHello and welcome to the unit converter!")
user_input = input("Enter a value to convert: ")

try:
    value = float(user_input)
except ValueError:
    print("Invalid value, please enter a number.")
    exit()

print("Choose what to convert: ")
print("P: Price, before & after discount and tax: ")
print("S: Speed, km/h > mph: ")

convert = input().strip().upper()
if convert == "P":
    discount = 10
    moms = 0.20
    price_later = (value - discount) * (1 + moms)
    print(
        f"The final price of {round(value, 2)} after 10kr discount and 20% is: {round(price_later, 2)}"
    )
elif convert == "S":
    mph = value * 0.62137
    print(f"{round(value, 2)} km/h in mph is {round(value, 2)} mph")
else:
    print("Invalid converted, please enter S or P")
    exit()
