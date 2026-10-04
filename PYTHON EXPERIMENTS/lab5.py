HRA_PERCENT = 20
DA_PERCENT = 15
PF_PERCENT = 12
TAX_PERCENT = 5


# ---------------- DISPLAY HEADING ----------------
def display_heading():

    print("\n")
    print("=" * 60)
    print("        EMPLOYEE PAYROLL MANAGEMENT SYSTEM")
    print("=" * 60)


# ---------------- CALCULATE ALLOWANCES ----------------
def calculate_allowances(basic_salary):

    hra = basic_salary * HRA_PERCENT / 100
    da = basic_salary * DA_PERCENT / 100

    return hra, da


# ---------------- CALCULATE BONUS ----------------
def calculate_bonus(basic_salary, bonus_percent=10):

    return basic_salary * bonus_percent / 100


# ---------------- CALCULATE DEDUCTIONS ----------------
def calculate_deductions(gross_salary):

    pf = gross_salary * PF_PERCENT / 100
    tax = gross_salary * TAX_PERCENT / 100

    return pf, tax


# ---------------- CALCULATE GROSS SALARY ----------------
def calculate_gross_salary(basic_salary, hra, da, bonus):

    gross = basic_salary + hra + da + bonus

    return gross


# ---------------- CALCULATE NET SALARY ----------------
def calculate_net_salary(gross_salary, pf, tax):

    net = gross_salary - (pf + tax)

    return net


# ---------------- EXTRA ALLOWANCES ----------------
def extra_allowances(*allowances):

    total = sum(allowances)

    return total


# ---------------- PRINT SALARY SLIP ----------------
def print_salary_slip(**details):

    print("\n")
    print("=" * 60)
    print("                SALARY SLIP")
    print("=" * 60)

    for key, value in details.items():

        print(f"{key:20}: {value}")

    print("=" * 60)


# Lambda function for festival bonus
special_bonus = lambda salary: salary * 0.03


# ================= MAIN PROGRAM =================

while True:

    display_heading()

    try:

        emp_id = int(input("Enter Employee ID        : "))
        emp_name = input("Enter Employee Name      : ")
        department = input("Enter Department          : ")
        designation = input("Enter Designation        : ")
        basic_salary = float(input("Enter Basic Salary       : "))
        overtime_hours = int(input("Enter Overtime Hours     : "))
        overtime_rate = float(input("Enter Overtime Rate      : "))

        # Calculate overtime amount
        overtime_amount = overtime_hours * overtime_rate

        # Calculate HRA and DA
        hra, da = calculate_allowances(basic_salary)

        # Calculate regular bonus
        bonus = calculate_bonus(basic_salary)

        # Calculate festival bonus using lambda
        festival_bonus = special_bonus(basic_salary)

        # Fixed allowances
        medical_allowance = 2500
        travel_allowance = 1800

        # Calculate all extra allowances
        other_allowance = extra_allowances(
            overtime_amount,
            medical_allowance,
            travel_allowance,
            festival_bonus
        )

        # Calculate gross salary
        gross_salary = calculate_gross_salary(
            basic_salary,
            hra,
            da,
            bonus
        )

        # Add extra allowances
        gross_salary = gross_salary + other_allowance

        # Calculate deductions
        pf, tax = calculate_deductions(gross_salary)

        # Calculate net salary
        net_salary = calculate_net_salary(
            gross_salary,
            pf,
            tax
        )

        # Display salary slip
        print_salary_slip(

            Employee_ID=emp_id,
            Employee_Name=emp_name,
            Department=department,
            Designation=designation,
            Basic_Salary=basic_salary,
            HRA=hra,
            DA=da,
            Bonus=bonus,
            Festival_Bonus=festival_bonus,
            Medical_Allowance=medical_allowance,
            Travel_Allowance=travel_allowance,
            Overtime=overtime_amount,
            Gross_Salary=gross_salary,
            Provident_Fund=pf,
            Income_Tax=tax,
            Net_Salary=net_salary
        )

    except ValueError:

        print("\nInvalid input!")
        print("Please enter numeric values correctly.")

    except ZeroDivisionError:

        print("\nDivision by zero is not allowed.")

    except Exception as e:

        print("\nUnexpected Error :", e)

    choice = input("\nCalculate Salary Again? (Y/N): ")

    if choice.lower() != 'y':

        print("\nThank You for using Employee Payroll Management System.")

        break