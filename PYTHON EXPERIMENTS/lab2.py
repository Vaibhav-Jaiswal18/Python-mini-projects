while True:

    print("\n" + "=" * 60)
    print("      ELECTRICITY BILL & EMPLOYEE SALARY MANAGEMENT")
    print("=" * 60)

    print("\n1. Electricity Bill Calculation")
    print("2. Employee Salary Calculation")
    print("3. Exit")

    choice = int(input("\nEnter your choice: "))

    # ---------------- ELECTRICITY BILL ----------------
    if choice == 1:

        print("\n--------- Electricity Bill ---------\n")

        consumer_no = input("Enter Consumer Number : ")
        consumer_name = input("Enter Consumer Name   : ")
        units = float(input("Enter Units Consumed  : "))

        # Calculate electricity bill
        if units <= 100:
            bill = units * 1.50

        elif units <= 200:
            bill = (100 * 1.50) + ((units - 100) * 2.50)

        elif units <= 300:
            bill = (100 * 1.50) + (100 * 2.50) + ((units - 200) * 4.00)

        else:
            bill = (
                (100 * 1.50)
                + (100 * 2.50)
                + (100 * 4.00)
                + ((units - 300) * 6.00)
            )

        # Calculate surcharge
        if bill > 1000:
            surcharge = bill * 0.05
        else:
            surcharge = 0

        total_bill = bill + surcharge

        # Display electricity bill
        print("\n----------- Electricity Bill -----------")
        print("Consumer Number :", consumer_no)
        print("Consumer Name   :", consumer_name)
        print("Units Consumed  :", units)
        print("Energy Charges  : ₹", round(bill, 2))
        print("Surcharge       : ₹", round(surcharge, 2))
        print("Total Bill      : ₹", round(total_bill, 2))

    # ---------------- EMPLOYEE SALARY ----------------
    elif choice == 2:

        print("\n--------- Employee Salary ---------\n")

        emp_id = input("Enter Employee ID : ")
        emp_name = input("Enter Employee Name : ")

        # Validate basic salary
        while True:

            try:
                basic = float(input("Enter Basic Salary : "))

                if basic <= 0:
                    print("Salary cannot be zero or negative.")
                    continue

                break

            except ValueError:
                print("Please enter a valid salary.")

        # Calculate allowances
        hra = basic * 0.20
        da = basic * 0.15
        ta = basic * 0.10

        # Calculate PF
        pf = basic * 0.12

        # Calculate gross salary
        gross = basic + hra + da + ta

        # Calculate income tax
        if gross <= 50000:
            tax = 0

        elif gross <= 100000:
            tax = gross * 0.10

        else:
            tax = gross * 0.20

        # Calculate net salary
        net_salary = gross - pf - tax

        # Salary Slip
        print("\n-------------- Salary Slip ----------------")
        print("Employee ID      :", emp_id)
        print("Employee Name    :", emp_name)
        print("-------------------------------------------")
        print("Basic Salary     : ₹", round(basic, 2))
        print("HRA (20%)        : ₹", round(hra, 2))
        print("DA (15%)         : ₹", round(da, 2))
        print("TA (10%)         : ₹", round(ta, 2))
        print("Gross Salary     : ₹", round(gross, 2))
        print("PF (12%)         : ₹", round(pf, 2))
        print("Income Tax       : ₹", round(tax, 2))
        print("-------------------------------------------")
        print("Net Salary       : ₹", round(net_salary, 2))

    # ---------------- EXIT ----------------
    elif choice == 3:

        print("\nThank You for using the system.")
        break

    # ---------------- INVALID CHOICE ----------------
    else:

        print("\nInvalid Choice.")

    # Ask whether user wants to continue
    again = input("\nDo you want to continue (Y/N): ")

    if again.upper() == "Y":
        continue

    else:
        print("\nProgram Terminated.")
        break