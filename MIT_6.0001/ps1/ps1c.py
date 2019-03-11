#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 15:20:35 2019

@author: Apple
"""

annual_salary = float(input("Enter your starting annual salary:"))
total_cost = 1000000
semi_annual_raise = 0.07
portion_down_payment = 0.25

r = 0.04 # annual return




def get_months_to_achieve(portion_saved, annual_salary):
    '''renturns the months to save enough down payment
    '''
    current_savings = 0 # start with a current savings of $0
    cnt_months = 0
    
    monthly_salary = annual_salary / 12
    
    while total_cost * portion_down_payment - current_savings > 100:
        cnt_months += 1
        if cnt_months > 1 and cnt_months % 6 == 1:
            annual_salary = annual_salary * (1 + semi_annual_raise)
            monthly_salary = annual_salary / 12
        current_savings += current_savings * r / 12
        current_savings += monthly_salary * portion_saved
        
    return cnt_months




def get_best_savings_rate(starting_salary):
    ''' use bisection search to find the best savings rate.
    
    returns: the number of steps, best savings rate
    '''
    cnt = {'cnt':0}

    def bisect_search(L, cnt):
        '''
        returns Bool
        '''
        cnt['cnt'] = cnt['cnt'] + 1
        if len(L) == 0:
            return (False, 0)
        elif len(L) == 1:
            return (get_months_to_achieve(L[0], starting_salary) == 36, L[0])
        else:
            half = len(L) // 2
            months_need = get_months_to_achieve(L[half], starting_salary)
            if months_need  == 36:
                return (True, L[half])
            elif months_need < 36:
                return bisect_search(L[:half], cnt)
            else:
                return bisect_search(L[half:], cnt)
                
    # portion_saved from 0.01% to 100%
    savings_rates = [i / 10000 for i in range(1,10000)]
    search_result = bisect_search(savings_rates, cnt)
    print(search_result)
    if search_result[0]:
        print("Best savings rate: ",search_result[1])
        print("Steps in bisection search: ", cnt)
    else:
        print("It is not possible to pay the down payment in three years.")
        print("Steps in bisection search: ", cnt)
    
    
get_best_savings_rate(annual_salary)

#print(get_months_to_achieve(0.4411, annual_salary))
#print(get_months_to_achieve(0.2266, annual_salary))