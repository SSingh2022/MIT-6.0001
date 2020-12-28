annual_salary = float(input("Enter your annual salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost = float(input("Enter the cost of your dream home: "))
portion_down_payment = 0.25
current_savings = 0
down_payment = total_cost * portion_down_payment
monthly_salary = annual_salary / 12
r = .04
number_of_months = 0
while current_savings < down_payment:
    current_savings += (r / 12 * current_savings)
    current_savings += (portion_saved * monthly_salary)
    number_of_months += 1
print("Number of months:", number_of_months)
