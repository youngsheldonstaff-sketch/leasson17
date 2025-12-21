# homework.py
bill = float(input("Enter bill: "))
paid = float(input("Enter paid: "))

due = bill - paid

if due > 0:
    print("Amount still due:", due)

if due < 0:
    # Multiply by -1 to show change as a positive number
    print("Change to return:", due * -1)

if due == 0:
    print("Bill settled.")

