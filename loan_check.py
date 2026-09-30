"""Loan affordability check.

Reads a monthly income and a proposed monthly loan payment, then reports
whether the payment-to-income ratio is within a safe threshold.
"""

MIN_INCOME = 1.0
MAX_INCOME = 1_000_000.0
MIN_PAYMENT = 0.0
MAX_PAYMENT = 1_000_000.0

SAFE_RATIO_LIMIT = 0.28
CAUTION_RATIO_LIMIT = 0.36


def read_amount(prompt_text, minimum, maximum):
    """Ask for a dollar amount until the user enters a valid number in range."""
    while True:
        raw_entry = input(prompt_text).strip().replace(",", "").lstrip("$")

        if raw_entry == "":
            print("No value entered. Please type a number.")
            continue

        try:
            amount = float(raw_entry)
        except ValueError:
            print(f"'{raw_entry}' is not a number. Please enter digits only, for example 4500.")
            continue

        if amount != amount or amount in (float("inf"), float("-inf")):
            print("Please enter a real, finite number.")
            continue

        if amount < minimum or amount > maximum:
            print(f"Value must be between ${minimum:,.2f} and ${maximum:,.2f}.")
            continue

        return amount


def classify_ratio(payment_ratio):
    """Return an affordability label for a payment-to-income ratio."""
    if payment_ratio <= SAFE_RATIO_LIMIT:
        return "AFFORDABLE", "The payment is within the safe threshold."
    elif payment_ratio <= CAUTION_RATIO_LIMIT:
        return "CAUTION", "The payment is manageable but leaves little room for other debt."
    else:
        return "NOT AFFORDABLE", "The payment is above the safe threshold."


def main():
    print("Loan Affordability Check")
    print(f"Safe limit: {SAFE_RATIO_LIMIT:.0%} of gross monthly income. "
          f"Caution zone: up to {CAUTION_RATIO_LIMIT:.0%}.\n")

    monthly_income = read_amount("Enter your gross monthly income ($): ", MIN_INCOME, MAX_INCOME)
    monthly_payment = read_amount("Enter the proposed monthly loan payment ($): ", MIN_PAYMENT, MAX_PAYMENT)

    payment_ratio = monthly_payment / monthly_income
    status_label, status_detail = classify_ratio(payment_ratio)

    print(f"\nIncome ${monthly_income:,.2f} | Payment ${monthly_payment:,.2f} | "
          f"Ratio {payment_ratio:.1%}")
    print(f"Result: {status_label}. {status_detail}")


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print("\nInput cancelled. Exiting.")
