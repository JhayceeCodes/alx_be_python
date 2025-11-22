FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5


def convert_to_celsius(fahrenheit):
    temp_in_celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return f"{fahrenheit}°F is {temp_in_celsius}°C"

def convert_to_fahrenheit(celsius):
    temp_in_fahrenheit = celsius * CELSIUS_TO_FAHRENHEIT_FACTOR + 32
    return f"{celsius}°C is {temp_in_fahrenheit}°F"


temp = float(input("Enter the temperature to convert: "))
temp_type = input("Is this temperature in Celsius or Fahrenheit? (C/F): ")

if type(temp).__name__ == "float":
    if temp_type == "C":
        print(convert_to_fahrenheit(temp))
    elif temp_type == "F":
        print(convert_to_celsius(temp))
    else:
        print("Please enter 'C' or 'F'.")
else:
    print("Invalid temperature. Please enter a numeric value.")

