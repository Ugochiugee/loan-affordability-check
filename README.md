# Loan Affordability Check

A command-line program that reads a gross monthly income and a proposed monthly loan payment, then reports whether the payment is affordable based on its share of income. It is intended for anyone who wants a quick first check before taking on a loan.

## How it decides

| Payment as % of income | Result |
|---|---|
| 28% or less | AFFORDABLE |
| Above 28%, up to 36% | CAUTION |
| Above 36% | NOT AFFORDABLE |

Accepted ranges: income from $1.00 to $1,000,000.00, payment from $0.00 to $1,000,000.00. Letters, empty entries and out-of-range values are rejected with a message, and the program asks again.

## Setup

Requires Python 3.11 or later.

```
git clone https://github.com/Ugochiugee/loan-affordability-check
cd loan-affordability-check
python -m venv .venv
source .venv/bin/activate    # macOS/Linux
.venv\Scripts\Activate.ps1    # Windows PowerShell
.venv\Scripts\activate.bat    # Windows Command Prompt
pip install -r requirements.txt
```

If PowerShell blocks activation, run `Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned`, answer Y, and try again.

`requirements.txt` installs nothing because the program uses only the standard library. The step is kept so the setup is the same for every project.

## Run

```
python loan_check.py
```

## Example

```
Enter your gross monthly income ($): abc
'abc' is not a number. Please enter digits only, for example 4500.
Enter your gross monthly income ($): 5000
Enter the proposed monthly loan payment ($): 1600

Income $5,000.00 | Payment $1,600.00 | Ratio 32.0%
Result: CAUTION. The payment is manageable but leaves little room for other debt.
```

## Known limitations

- Looks at one loan payment only. It does not include rent, other debts or living costs, so it is not a full debt service ratio.
- The 28% and 36% thresholds are common rules of thumb, not lender policy. Real lenders use their own criteria.
- Uses gross (pre-tax) income. It does not calculate taxes or take-home pay.
- Amounts are in one currency and are not tied to any specific country.
- Commas and a leading $ are accepted, but other formats such as "5k" are rejected.
- Amounts are stored as floats, which is fine for a ratio check but not exact enough for real money calculations. The decimal module would be the next step.
- Not financial advice.
