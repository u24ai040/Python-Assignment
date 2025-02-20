class Converter:
    conversion_factors = {
        "inches": 1,
        "feet": 1 / 12,
        "yards": 1 / 36,
        "miles": 1 / 63360,
        "kilometers": 1 / 39370.1,
        "meters": 1 / 39.3701,
        "centimeters": 1 / 0.393701,
        "millimeters": 1 / 0.0393701
    }

    def __init__(self, length, unit):
        if unit not in self.conversion_factors:
            raise ValueError("Invalid unit provided")
        self.length = length
        self.unit = unit
        self.base_length = length / self.conversion_factors[unit]

    def convert_to(self, target_unit):
        if target_unit not in self.conversion_factors:
            raise ValueError("Invalid target unit provided")
        return self.base_length * self.conversion_factors[target_unit]


length = float(input("Enter the length: "))
unit = input("Enter the unit (inches, feet, yards, miles, kilometers, meters, centimeters, millimeters): ").lower()
try:
    converter = Converter(length, unit)
    while True:
        print("\nConversion Options:")
        print("1. Inches")
        print("2. Feet")
        print("3. Yards")
        print("4. Miles")
        print("5. Kilometers")
        print("6. Meters")
        print("7. Centimeters")
        print("8. Millimeters")
        print("9. Exit")
        choice = input("Choose an option: ")

        units_list = ["inches", "feet", "yards", "miles", "kilometers", "meters", "centimeters", "millimeters"]
        if choice == '9':
            print("Exiting...")
            break
        elif choice.isdigit() and 1 <= int(choice) <= 8:
            target_unit = units_list[int(choice) - 1]
            print(f"{length} {unit} is {converter.convert_to(target_unit):.3f} {target_unit}.")
        else:
            print("Invalid choice. Please try again.")
except ValueError as e:
    print(e)
