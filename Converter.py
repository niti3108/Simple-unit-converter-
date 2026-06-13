print("Unit Converter")
print("1. Kilometers to Miles")
print("2. Celsius to Fahrenheit")

choice = int(input("Choose conversion (1 or 2): "))

if choice == 1:
    km = float(input("Enter kilometers: "))
    miles = km * 0.621371
    print(f"{km} KM is {miles:.2f} Miles.")

elif choice == 2:
    celsius = float(input("Enter temperature in Celsius: "))
    fahrenheit = (celsius * 9/5) + 32
    print(f"{celsius}°C is {fahrenheit:.2f}°F.")

else:
    print("Invalid choice!")
