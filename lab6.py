# STANDARD_WORKING_WEEK = 39
# STANDARD_PAY_RATE = 35
# OVERTIME_PAY_RATE = 50
# TAX_PAID = 0.21
# NO_TAX_PAID_YEARLY_SALARY = 18000
# WEEKS_IN_YEAR = 52
#
# hours_worked = float(input("Enter hours worked: "))
#
# weekly_tax_allowance = NO_TAX_PAID_YEARLY_SALARY / WEEKS_IN_YEAR
#
# if hours_worked <= STANDARD_WORKING_WEEK:
#     standard_pay = hours_worked * STANDARD_PAY_RATE
# else:
#    standard_pay = STANDARD_WORKING_WEEK * STANDARD_PAY_RATE
# overtime_pay = (hours_worked - STANDARD_WORKING_WEEK) * OVERTIME_PAY_RATE
#
# gross_pay = standard_pay + overtime_pay
#
# yearly_salary = gross_pay * WEEKS_IN_YEAR
#
# if yearly_salary <= NO_TAX_PAID_YEARLY_SALARY:
#     tax = 0
# else:
#     if gross_pay >weekly_tax_allowance:
#         taxable_weekly_amount = gross_pay - weekly_tax_allowance
#     else:
#         taxable_weekly_amount = 0
#     tax = taxable_weekly_amount * 0.21
#
# net_pay = gross_pay - tax
#
# print("\nHours worked :", hours_worked)
# print("Standard pay amount :", standard_pay)
# print("Over-time pay amount :", overtime_pay)
# print("Gross Pay :", gross_pay)
# print("Total Tax :", tax)
# print("Net Pay :", net_pay)