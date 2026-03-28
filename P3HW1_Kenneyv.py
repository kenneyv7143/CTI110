##valerie l kenney
#3/26/26
#Debugging assignment

# This program takes a number grade , determines average and displays letter grade for average.


#get grades from user
# Enter grades for six modules

mod_1 = float(input ("Enter grade for Module 1: "))
mod_2 = float(input ("Enter grade for Module 2: "))
mod_3 = float(input ("Enter grade for Module 3: "))
mod_4 = float(input ("Enter grade for Module 4: "))
mod_5 = float(input ("Enter grade for Module 5: "))
mod_6 = float(input ("Enter grade for Module 6: "))




# add grades entered to a list

gradelist = [ mod_1,mod_2,mod_3, mod_4, mod_5,mod_6]
#Printingresults
print ("-"*15, "Results","-"*15)


# TO DO: determine lowest, highest , sum and average for grades

low = min(gradelist)
high = max(gradelist)
sum = sum(gradelist)
avg = sum / len(gradelist)

print(f'{"Lowest Grade:":<20}{low}')
print(f'{"Highest Grade:":<20}{high}')
print(f'{"Sum of Grades:":<20}{sum}')
print(f'{"Average:":<20}{avg:.2f}')
print()
print("-"*35)

# determine letter grade for average
if avg >= 90:
    print('Your grade is: A')
else:
    if avg > 80:
        print('Your grade is: B')
    else:
        print('Your grade is: F') 
        # TO DO: finish this

