# Payroll System

employees = []

TAX_RATE = 0.10
SSS_RATE = 0.05
PHILHEALTH_RATE = 0.03


def add_employee():
    print("\n--- Add Employee ---")
    name = input("Enter Employee Name: ")
    hours = float(input("Enter Hours Worked: "))
    rate = float(input("Enter Hourly Rate: "))

    gross_pay = hours * rate
    tax = gross_pay * TAX_RATE
    sss = gross_pay * SSS_RATE
    philhealth = gross_pay * PHILHEALTH_RATE
    total_deductions = tax + sss + philhealth
    net_pay = gross_pay - total_deductions

    employee = {
        "name": name,
        "hours": hours,
        "rate": rate,
        "gross_pay": gross_pay,
        "tax": tax,
        "sss": sss,
        "philhealth": philhealth,
        "deductions": total_deductions,
        "net_pay": net_pay
    }

    employees.append(employee)

    print("\n--- Payslip ---")
    print(f"Name           : {employee['name']}")
    print(f"Hours Worked   : {employee['hours']}")
    print(f"Hourly Rate    : {employee['rate']:.2f}")
    print(f"Gross Pay      : {employee['gross_pay']:.2f}")
    print(f"  Tax (10%)    : {employee['tax']:.2f}")
    print(f"  SSS (5%)     : {employee['sss']:.2f}")
    print(f"  PhilHealth   : {employee['philhealth']:.2f}")
    print(f"Total Deductions: {employee['deductions']:.2f}")
    print(f"Net Pay        : {employee['net_pay']:.2f}")


def view_all_payslips():
    print("\n--- All Payslips ---")
    if not employees:
        print("No employees found.")
        return
    for i, emp in enumerate(employees, start=1):
        print(f"\n[{i}] {emp['name']}")
        print(f"    Hours: {emp['hours']}  |  Rate: {emp['rate']:.2f}")
        print(f"    Gross Pay: {emp['gross_pay']:.2f}  |  Deductions: {emp['deductions']:.2f}  |  Net Pay: {emp['net_pay']:.2f}")


def search_employee():
    print("\n--- Search Employee ---")
    query = input("Enter Employee Name to Search: ").strip().lower()
    results = [emp for emp in employees if query in emp["name"].lower()]

    if not results:
        print("No employee found.")
        return

    for emp in results:
        print(f"\nName           : {emp['name']}")
        print(f"Hours Worked   : {emp['hours']}")
        print(f"Hourly Rate    : {emp['rate']:.2f}")
        print(f"Gross Pay      : {emp['gross_pay']:.2f}")
        print(f"Deductions     : {emp['deductions']:.2f}")
        print(f"Net Pay        : {emp['net_pay']:.2f}")


def main():
    while True:
        print("\n====== Payroll System ======")
        print("1. Add Employee")
        print("2. View All Payslips")
        print("3. Search Employee")
        print("4. Exit")
        choice = input("Select option (1-4): ").strip()

        if choice == "1":
            add_employee()
        elif choice == "2":
            view_all_payslips()
        elif choice == "3":
            search_employee()
        elif choice == "4":
            print("Exiting... All data cleared.")
            break
        else:
            print("Invalid option. Please enter 1, 2, 3, or 4.")


if __name__ == "__main__":
    main()