# mortgage.py
#
# Exercise 1.7

principal = 500000.0
rate = 0.05
base_payment = 2684.11
total_paid = 0.0

extra_payment_start_month = 60
extra_payment_end_month = 108
extra_payment = 1000

month = 1
while principal > 0:
    if month >= extra_payment_start_month and month <= extra_payment_end_month:
        payment = min(base_payment + extra_payment, principal * (1 + rate/12))
    else: 
        payment = min(base_payment, principal * (1 + rate/12))
    
    principal = principal * (1 + rate/12) - payment
    total_paid = total_paid + payment

    print(month, round(total_paid, 2), round(principal, 2))

    month += 1

print(f'Total paid {total_paid: 0.2f}')
print(f'Months {month-1}')