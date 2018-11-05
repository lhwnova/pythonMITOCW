# -*- coding: utf-8 -*-
"""
Created on Fri Oct 12 23:37:18 2018

@author: hello
"""

# part A
annual_salary = float(input("Enter your annual salary: "))

portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))

total_cost = float(input("Enter the cost of your dream home: "))

monthly_salary = annual_salary/12
monthly_saving = monthly_salary*portion_saved

portial_down_payment = 0.25*total_cost

current_saving = 0
month = 0

while current_saving < portial_down_payment:
    current_saving = current_saving + ((current_saving*0.04)/12)
    current_saving = current_saving + monthly_saving
    month = month + 1 
    
    
print(month)


# Part B

annual_salary = float(input("Enter your annual salary: "))

portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))

total_cost = float(input("Enter the cost of your dream home: "))

semi_annual_raise = float(input("Enter the semiannual raise, as a decimal: "))

monthly_salary = annual_salary/12
monthly_saving = monthly_salary*portion_saved

portial_down_payment = 0.25*total_cost

current_saving = 0
month = 0

while current_saving < portial_down_payment:
    if month != 0 and month%6 == 0:
        annual_salary = annual_salary*(1+semi_annual_raise)
        monthly_salary = annual_salary/12
        monthly_saving = monthly_salary*portion_saved
        
    current_saving = current_saving + ((current_saving*0.04)/12)
    current_saving = current_saving + monthly_saving
    month = month + 1 
    
    
print("Number of months: ", month)


# Part C

starting_salary = float(input("Enter the starting salary: "))
total_cost = 1000000.0
portial_down_payment = 0.25*total_cost
semi_annual_raise = 0.07


month = 36
steps = 0
minrate = 0 
maxrate = 10000
midrate = 0
found = False

while abs(minrate - maxrate) > 1 :
    
    steps = steps + 1
    current_saving = 0
    midrate = (maxrate + minrate)//2
    portion_saved = midrate/10000.0
    current_saving = 0
    annual_salary = starting_salary
    
    monthly_salary = annual_salary/12
    monthly_saving = monthly_salary*portion_saved
    
    for i in range(1, month + 1):
        current_saving = current_saving + ((current_saving*0.04)/12)
        current_saving = current_saving + monthly_saving
        
        if abs(current_saving - portial_down_payment) < 100:
            minrate = maxrate
            found = True
            break
         
        if i%6 == 0:
            annual_salary = annual_salary*(1+semi_annual_raise)
            monthly_salary = annual_salary/12
            monthly_saving = monthly_salary*portion_saved
        
    if current_saving < (portial_down_payment - 100):
        minrate = midrate 
    elif current_saving > (portial_down_payment + 100):
        maxrate = midrate 
    
if found == True:
    print("Best savings rate:", midrate/10000.0)
    print("Steps in bisection search: ", steps)    
else:
    print("It is not possible to pay the down payment in three years.")
    

