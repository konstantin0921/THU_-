# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

annual_salary = float(input("Enter your starting annual salary:"))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal:"))
total_cost = float(input("Enter the cost of your dream home:"))
semi_annual_raise = float(input("Enter the semi­annual raise, as a decimal: "))



portion_down_payment = 0.25
current_savings = 0 # start with a current savings of $0
r = 0.04 # annual return
cnt_months = 0
monthly_salary = annual_salary / 12

while current_savings < total_cost * portion_down_payment:
    if cnt_months > 1 and cnt_months % 6 == 1:
        annual_salary = annual_salary * (1 + semi_annual_raise)
        monthly_salary = annual_salary / 12
    current_savings += current_savings * r / 12
    current_savings += monthly_salary * portion_saved
    cnt_months += 1
    
print("Number of months:", cnt_months)
    
