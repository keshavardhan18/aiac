# Temperature Conversion Program

def celsius_to_fahrenheit(c):
    return c * 9/5 + 32

def celsius_to_kelvin(c):
    return c + 273.15

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

def fahrenheit_to_kelvin(f):
    return (f - 32) * 5/9 + 273.15

def kelvin_to_celsius(k):
    return k - 273.15

def kelvin_to_fahrenheit(k):
    return (k - 273.15) * 9/5 + 32

print("Choose the conversion you want to perform:")
print("1. Celsius to Fahrenheit")
print("2. Celsius to Kelvin")
print("3. Fahrenheit to Celsius")
print("4. Fahrenheit to Kelvin")
print("5. Kelvin to Celsius")
print("6. Kelvin to Fahrenheit")

choice = int(input("Enter your choice (1-6): "))

if choice == 1:
    temp = float(input("Enter temperature in Celsius: "))
    result = celsius_to_fahrenheit(temp)
    print(f"{temp} Celsius = {result} Fahrenheit")
elif choice == 2:
    temp = float(input("Enter temperature in Celsius: "))
    result = celsius_to_kelvin(temp)
    print(f"{temp} Celsius = {result} Kelvin")
elif choice == 3:
    temp = float(input("Enter temperature in Fahrenheit: "))
    result = fahrenheit_to_celsius(temp)
    print(f"{temp} Fahrenheit = {result} Celsius")
elif choice == 4:
    temp = float(input("Enter temperature in Fahrenheit: "))
    result = fahrenheit_to_kelvin(temp)
    print(f"{temp} Fahrenheit = {result} Kelvin")
elif choice == 5:
    temp = float(input("Enter temperature in Kelvin: "))
    result = kelvin_to_celsius(temp)
    print(f"{temp} Kelvin = {result} Celsius")
elif choice == 6:
    temp = float(input("Enter temperature in Kelvin: "))
    result = kelvin_to_fahrenheit(temp)
    print(f"{temp} Kelvin = {result} Fahrenheit")
else:
    print("Invalid choice. Please enter a number between 1 and 6.")