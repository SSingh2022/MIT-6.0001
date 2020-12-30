semi_annual_raise = .07
r = .04
total_cost = 1000000
down_payment = 0.25*total_cost
starting_salary = float(input("Enter the starting salary: "))
monthly_salary = starting_salary / 12
number_of_months = 0
num_guesses = 0
current_savings = 0
low =  0
high = 10000
portion_saved = float(((high + low)/2)/10000)
while number_of_months != 36:
    number_of_months = 0
    monthly_salary = starting_salary / 12
    num_guesses += 1
    while current_savings < down_payment - 100:
        current_savings += (r / 12 * current_savings)
        current_savings += (portion_saved * monthly_salary)
        number_of_months += 1
        if number_of_months % 6 == 0:
            monthly_salary += (monthly_salary * semi_annual_raise)
    if number_of_months < 36:
        high = portion_saved
    elif number_of_months > 36:
        low = portion_saved
    portion_saved = (high + low)/2
    current_savings = 0
if portion_saved >= 1.00:
    print("It is not possible to pay the down payment in three years.")
else:
    print("Best savings rate:", portion_saved)
    print("Steps in bisection search:", num_guesses)
