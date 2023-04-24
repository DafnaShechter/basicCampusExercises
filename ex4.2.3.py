temp = input("Insert the temperature you would like to convert: ")

if temp[-1] in ['c', 'C']:
    # convert Celsius to Fahrenheit
    celsius = float(temp[:-1])
    fahrenheit = (celsius * 9 / 5) + 32
    print(f"{fahrenheit:.1f}F")

elif temp[-1] in ['f', 'F']:
    # convert Fahrenheit to Celsius
    fahrenheit = float(temp[:-1])
    celsius = (fahrenheit - 32) * 5 / 9
    print(f"{celsius:.1f}C")

else:
    print("Invalid input. Temperature must end with 'C' or 'F'.")
