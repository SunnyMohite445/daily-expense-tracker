"""
DAILY EXPENSE TRACKER & ANALYTICS SYSTEM
Author: Analyst Prototype
Purpose:
- Track daily spending
- Analyze spending behavior
- Identify waste and control areas
- Provide actionable financial insights
"""

print("=" * 70)
print("        DAILY EXPENSE TRACKER  ANALYST SUMMARY REPORT")
print("=" * 70)

# -----------------------------------------------------
# 1. CONFIGURATION / BUSINESS ASSUMPTIONS
# -----------------------------------------------------

NECESSARY_TYPES = ["necessary", "essential"]
UNNECESSARY_TYPES = ["unnecessary", "waste"]

# -----------------------------------------------------
# 2. INPUT: DAILY BUDGET
# -----------------------------------------------------

daily_budget = float(input("\nEnter today's total budget: "))

# -----------------------------------------------------
# 3. DATA STORAGE STRUCTURES
# -----------------------------------------------------
# We store raw transactions and aggregated metrics separately
# This mirrors real-world analytical thinking

transactions = []

category_totals = {}
payment_mode_totals = {}

total_spent = 0
necessary_spent = 0
unnecessary_spent = 0

# -----------------------------------------------------
# 4. DATA COLLECTION LOOP
# -----------------------------------------------------

while True:
    print("\n--- New Expense Entry ---")

    amount = float(input("Expense amount: "))
    category = input("Category (food, travel, shopping, rent, etc.): ").lower()
    necessity = input("Type (necessary / unnecessary): ").lower()
    payment_mode = input("Payment mode (cash / card / upi): ").lower()

    # Store transaction (raw data)
    transaction = {
        "amount": amount,
        "category": category,
        "necessity": necessity,
        "payment_mode": payment_mode
    }
    transactions.append(transaction)

    # Update totals
    total_spent += amount

    if necessity in NECESSARY_TYPES:
        necessary_spent += amount
    else:
        unnecessary_spent += amount

    # Category aggregation
    if category in category_totals:
        category_totals[category] += amount
    else:
        category_totals[category] = amount

    # Payment mode aggregation
    if payment_mode in payment_mode_totals:
        payment_mode_totals[payment_mode] += amount
    else:
        payment_mode_totals[payment_mode] = amount

    # Continue?
    choice = input("Add another expense? (yes/no): ").lower()
    if choice == "no":
        break

# -----------------------------------------------------
# 5. DERIVED METRICS & KPIs
# -----------------------------------------------------

remaining_balance = daily_budget - total_spent

if total_spent > 0:
    waste_percentage = (unnecessary_spent / total_spent) * 100
    necessary_percentage = (necessary_spent / total_spent) * 100
else:
    waste_percentage = 0
    necessary_percentage = 0

# Identify highest spending category
highest_category = ""
highest_category_amount = 0

for category in category_totals:
    if category_totals[category] > highest_category_amount:
        highest_category_amount = category_totals[category]
        highest_category = category

# -----------------------------------------------------
# 6. ANALYST REPORT – NUMERICAL SUMMARY
# -----------------------------------------------------

print("\n" + "=" * 70)
print("                    DAILY FINANCIAL SUMMARY")
print("=" * 70)

print(f"Daily Budget           : {daily_budget}")
print(f"Total Spent Today      : {total_spent}")
print(f"Remaining Balance      : {remaining_balance}")
print(f"Total Transactions     : {len(transactions)}")

print("\n--- Category-wise Spending ---")
for category, amount in category_totals.items():
    print(f"{category.capitalize():15} : {amount}")

print("\n--- Payment Mode Usage ---")
for mode, amount in payment_mode_totals.items():
    print(f"{mode.capitalize():15} : {amount}")

# -----------------------------------------------------
# 7. ANALYTICAL INSIGHTS
# -----------------------------------------------------

print("\n" + "=" * 70)
print("                    ANALYTICAL INSIGHTS")
print("=" * 70)

print(f"Highest Spending Category : {highest_category.capitalize()}")
print(f"Amount Spent There        : {highest_category_amount}")

print(f"\nNecessary Spending        : {necessary_spent}")
print(f"Unnecessary Spending     : {unnecessary_spent}")

print(f"Necessary % of Spend     : {round(necessary_percentage, 2)}%")
print(f"Waste % of Spend         : {round(waste_percentage, 2)}%")

# -----------------------------------------------------
# 8. DECISION RULES (REAL ANALYST LOGIC)
# -----------------------------------------------------

print("\n" + "=" * 70)
print("                RISK & CONTROL ASSESSMENT")
print("=" * 70)

if waste_percentage > 35:
    print(" High Risk: Excessive unnecessary spending detected.")
    print("Immediate cost control required.")
elif waste_percentage > 20:
    print(" Moderate Risk: Spending discipline needs improvement.")
else:
    print(" Healthy: Spending behavior is under control.")

if remaining_balance < 0:
    print("\n⚠ Budget Breach: You exceeded today's budget.")
elif remaining_balance < daily_budget * 0.1:
    print("\n⚠ Low Balance: Savings margin is very low.")
else:
    print("\n Budget Status: Managed within limits.")

# -----------------------------------------------------
# 9. ACTIONABLE RECOMMENDATIONS (WHAT ANALYSTS ACTUALLY DO)
# -----------------------------------------------------

print("\n" + "=" * 70)
print("            ACTIONABLE RECOMMENDATIONS FOR TOMORROW")
print("=" * 70)

print("- Review high-spending category:", highest_category.capitalize())

if unnecessary_spent > necessary_spent:
    print("- Unnecessary expenses exceed essential ones.")
    print("- Set a strict discretionary spending limit.")

if highest_category in ["shopping", "junk", "entertainment"]:
    print("- This category is discretionary. Reduce frequency.")

print("- Track expenses in real-time, not end of day.")
print("- Prefer planned spending over impulse purchases.")

if payment_mode_totals.get("cash", 0) > payment_mode_totals.get("upi", 0):
    print("- High cash usage detected. Digital payments improve visibility.")

print("\nFinancial Discipline grows from awareness + control.")

print("\n" + "=" * 70)
print("                 END OF ANALYST REPORT")
print("=" * 70)
