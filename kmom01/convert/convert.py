

def celsius_to_fahrenheit(celsius):
    return celsius * 9 / 5 + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9

def main():
    print("Välkommen till konverteraren!")
    print("1. Celsius → Fahrenheit")
    print("2. Fahrenheit → Celsius")
    
    choice = input("Välj ett alternativ (1 eller 2): ")

    if choice == "1":
        c = float(input("Ange temperatur i Celsius: "))
        print(f"{c} °C = {celsius_to_fahrenheit(c):.2f} °F")
    elif choice == "2":
        f = float(input("Ange temperatur i Fahrenheit: "))
        print(f"{f} °F = {fahrenheit_to_celsius(f):.2f} °C")
    else:
        print("Fel: Ogiltigt val.")

if __name__ == "__main__":
    main()
