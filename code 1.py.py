# Case Study 2: Progressive Electricity Billing

monthly_units = [
    ("Jan", 120),
    ("Feb", 135),
    ("Mar", 260),
    ("Apr", 140),
]

fixed_charge = 100.0
surcharge_rate = 0.05  # 5% surcharge on energy + fixed
rebate_low_usage = 50.0  # Rs 50 rebate if units <= 150
spike_threshold = 0.30  # Flag if bill increases by > 30% over previous month

bills = []  # List of tuples: (month, units, total_bill)

for month, units in monthly_units:
    energy_charge = 0.0
    remaining = units

    # Slab 1: first 100 units @ Rs 3.00
    if remaining > 0:
        slab1 = min(remaining, 100)
        energy_charge += slab1 * 3.0
        remaining -= slab1

    # Slab 2: next 100 units (101-200) @ Rs 4.50
    if remaining > 0:
        slab2 = min(remaining, 100)
        energy_charge += slab2 * 4.5
        remaining -= slab2

    # Slab 3: above 200 units @ Rs 6.50
    if remaining > 0:
        energy_charge += remaining * 6.5

    subtotal = energy_charge + fixed_charge
    surcharge = subtotal * surcharge_rate
    rebate = rebate_low_usage if units <= 150 else 0.0
    total_bill = round(subtotal + surcharge - rebate, 2)
    bills.append((month, units, total_bill))

print("=== Monthly Electricity Bills ===")
for i in range(len(bills)):
    month, units, bill = bills[i]
    status = "Normal"
    if i > 0:
        prev_bill = bills[i - 1][2]
        if prev_bill > 0:
            pct_change = (bill - prev_bill) / prev_bill
            if pct_change > spike_threshold:
                status = f"UNUSUAL INCREASE (+{pct_change * 100:.1f}%)"
    print(f"{month}: {units} units -> Rs. {bill:.2f} | {status}")