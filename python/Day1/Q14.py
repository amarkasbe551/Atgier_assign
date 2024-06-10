# Assume suitable value for Ramesh's basic salary.
# His dearness allowance is 40% of basic salary and house rent allowance is 20% of basic salary. Calculte his gross salary (basic+dearness+hra=gross)

# Ramesh's basic salary is 
basic_Sal = 50000

# Accoding to first condi:-
dearness = basic_Sal*(40/100)
# Accoding to second condi:-
hra = basic_Sal*(20/100)
# Accoding to third condi:-
gross = basic_Sal+dearness+hra

print(f"Ramesh Basic Salary is {basic_Sal}\nHis Dearness is {dearness}\nHis Hra is {hra}")
