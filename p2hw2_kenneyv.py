#valerie l kenney
#2/5/26
#grade list


#grade listgrade list = []
#get grades from user
grade1 = float(input ("Enter grade for Module 1: "))
grade2 = float(input ("Enter grade for Module 2: "))
grade3 = float(input ("Enter grade for Module 3: "))
grade4 = float(input ("Enter grade for Module 4: "))
grade5 = float(input ("Enter grade for Module 5: "))
grade6 = float(input ("Enter grade for Module 6: "))

#add grades to the list
gradelist = [grade1,grade2,grade3,grade4,grade5,grade6]
print ("-"*15, "Results","-"*15)
lowest = min(gradelist)
highest = max(gradelist)
total = sum(gradelist)
avg = sum(gradelist)/len(gradelist)

# print results
print(f'{"Lowest Grade:":<20}{lowest}')
print(f'{"Highest Grade:":<20}{highest}')
print(f'{"Sum of Grades:":<20}{total}')
print(f'{"Average:":<20}{avg:.2f}')
print("-"*35)


#pseudocode
'''Display the following: (10 points each)
The lowest grade in the list
The highest grade in the list
Sum of grades
The grades' average
'''


