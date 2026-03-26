#KenneyV
#Mar242026
#P3HW2
# Calculating ot pay

name = input("Enter employee's name: ")
hoursWorked = float(input ("Enter number of hours worked: "))
payRate = float(input ("Enter employee's pay rate: "))   

if hoursWorked > 40:
    #calculate overtime
    overTimeHours = hoursWorked - 40
    #calculate overtime pay
    overPay = overTimeHours * (payRate * 1.5)
    # calculate salary for reg hours worket
    regPay = 40 * payRate
    # calculate gross pay
    grossPay = regPay + overPay
else:
    overPay = 0
    overTimeHours = 0
    regPay = hoursWorked * payRate
    grossPay = regPay
print ("-"*20)
print("Employee Name:",name, "\n")
print(f'{"Hours Worked":<15}{"Pay Rate":<12}{"Over Time":<12}{"Over Time Pay":<20}{"RegHour Pay":<20}{"Gross Pay"}')
print("-"*90)
print(f'{hoursWorked:<15}{payRate:<12}{overPay:<12}{overTimeHours:<20} ${regPay:<20}${grossPay:.2f}')

'''
print(overPay)
print("overTimeHours")
print(regPay)
print(grossPay)
          
'''
