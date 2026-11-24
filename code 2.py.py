# Case Study 4: Employee Payroll and Deduction Analysis

employees = [
    # (emp_id, name, basic, hra, da, ot_hours, ot_rate, incentive)
    ("E101", "Aarav", 30000.0, 8000.0, 4500.0, 10, 250.0, 2000.0),
    ("E102", "Diya", 55000.0, 15000.0, 8250.0, 5, 350.0, 4000.0),
]

for emp_id, name, basic, hra, da, ot_hours, ot_rate, incentive in employees:
    overtime_pay = ot_hours * ot_rate
    gross = basic + hra + da + overtime_pay + incentive

    # Progressive deductions: PF (12% of basic) + progressive tax/deduction slab
    pf = basic * 0.12
    if gross <= 40000:
        tax = gross * 0.05
    elif gross <= 75000:
        tax = gross * 0.10
    else:
        tax = gross * 0.15

    total_deductions = pf + tax
    net_pay = gross - total_deductions

    print("========================================")
    print(f"SALARY STATEMENT | {name} ({emp_id})")
    print("========================================")
    print(f"Basic Pay       : Rs. {basic:10.2f}")
    print(f"HRA + DA        : Rs. {hra + da:10.2f}")
    print(f"Overtime ({ot_hours}h)  : Rs. {overtime_pay:10.2f}")
    print(f"Incentive       : Rs. {incentive:10.2f}")
    print(f"GROSS SALARY    : Rs. {gross:10.2f}")
    print(f"PF (12% Basic)  : Rs. {pf:10.2f}")
    print(f"Progressive Tax : Rs. {tax:10.2f}")
    print(f"Total Deductions: Rs. {total_deductions:10.2f}")
    print(f"NET SALARY      : Rs. {net_pay:10.2f}")