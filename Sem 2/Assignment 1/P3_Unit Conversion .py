
feet = float(input("Enter a length in feet: "))

# List of conversion factors and their corresponding units
conversions = [ (12, "inches"),             # 1 foot = 12 inches
                (1 / 3, "yards"),           # 1 foot = 1/3 yards
                (1 / 5280, "miles"),        # 1 foot = 1/5280 miles
                (304.8, "millimeters"),     # 1 foot = 304.8 millimeters
                (30.48, "centimeters"),     # 1 foot = 30.48 centimeters
                (0.3048, "meters"),         # 1 foot = 0.3048 meters
                (1 / 3280.84, "kilometers") # 1 foot = 1/3280.84 kilometers
                ]

# List of conversion options
print("\nSelect a conversion option:")
print("1 for Inches")
print("2 for Yards")
print("3 for Miles")
print("4 for Millimeters")
print("5 for Centimeters")
print("6 for Meters")
print("7 for Kilometers")

# Asking user's choice
choice = int(input("\nEnter the number for conversion: "))

if 1<=choice<=7:
    #Performing Appropriate Conversion
    factor, unit = conversions[choice - 1]
    converted_value = feet * factor
    print(f"Answer = {converted_value} {unit}.")
else:
    print("Invalid choice. Please enter a number between 1 and 7.")
