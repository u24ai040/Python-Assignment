# QUESTION 4

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __add__(self, other):
        if isinstance(other, Employee):
            return self.salary + other.salary
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, Employee):
            return self.salary - other.salary
        return NotImplemented

    def display(self):
        print(f"Name: {self.name}, Salary: ₹{self.salary}")

print("Enter details for Employee 1:")
name1 = input("Name: ")
salary1 = float(input("Salary: "))
emp1 = Employee(name1, salary1)

print("\nEnter details for Employee 2:")
name2 = input("Name: ")
salary2 = float(input("Salary: "))
emp2 = Employee(name2, salary2)

while True:
        print("\nEmployee Operations:")
        print("1. Display Employee Details")
        print("2. Add Salaries of Employees")
        print("3. Compare Salaries (Difference)")
        print("4. Exit")

        choice = input("Choose an option 1 to 4 : ")

        if choice == '1':
            print("\nEmployee 1 Details:")
            emp1.display()
            print("Employee 2 Details:")
            emp2.display()

        elif choice == '2':
            total_salary = emp1 + emp2
            print(f"Combined Salary: ₹{total_salary}")

        elif choice == '3':
            salary_diff = emp1 - emp2
            print(f"Salary Difference: ₹{abs(salary_diff)}")
            if salary_diff > 0:
                print(f"{emp1.name} has a higher salary.")
            elif salary_diff < 0:
                print(f"{emp2.name} has a higher salary.")
            else:
                print("Both employees have the same salary.")

        elif choice == '4':
            print("Exiting...")
            break

        else:
            print("Invalid choice! Please try again.")
