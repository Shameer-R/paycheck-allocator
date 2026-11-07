TOTAL_MONTHY_EXPENSES = 938.18
MONTHLY_DEBT_MINIMUMS = 200.00

SPENDING = .30
DEBT = .60
SAVINGS = .10


def allocate_biweekly_paycheck(paycheckAmount):
    
    print(f"Total Paycheck: ${paycheckAmount}")
    
    paycheck_remaining = paycheckAmount
    
    # Allocate Half of Monthly Expenses
    total_bills = (TOTAL_MONTHY_EXPENSES/2)
    total_debt = (MONTHLY_DEBT_MINIMUMS/2)
    
    paycheck_remaining -= round(total_bills, 2)
    paycheck_remaining -= round(total_debt, 2)
    
    spending_allocation = round(paycheck_remaining * SPENDING, 2)
    debt_allocation = round(paycheck_remaining * DEBT, 2)
    savings_allocation = round(paycheck_remaining * SAVINGS, 2)
    
    paycheck_remaining -= spending_allocation
    paycheck_remaining -= debt_allocation
    paycheck_remaining -= savings_allocation
    
    print(f"Allocate ${total_bills} to bills")
    print(f"Allocate ${total_debt} to minimum debt payments")
    print(f"Allocate ${spending_allocation} to fun money")
    print(f"Allocate ${debt_allocation} to highest APR credit card")
    print(f"Allocate ${savings_allocation} to savings")
    print(f"${round(paycheck_remaining, 2)} remaining")
    
    
    
allocate_biweekly_paycheck(1102.04)