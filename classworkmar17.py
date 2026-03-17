#get a grade from a user 
grade1 = float(input ("enter your first grade:"))
grade2 = float(input ("enter your second grade:"))
grade3 = float(input ("enter your third grade:"))
grade4 = float(input ("enter your fourth grade:"))
grade5 = float(input ("enter your fifth grade:"))
total = grade1 + grade2 + grade3 + grade4 
average = total/4
print(average)
#find leter grade based on the average
#use FTCC letter grade scale
#rule will be 90 to 100 is an A
if average >= 90:
    print ("A")
else:
    if average >= 80:
        print("B")
    if average >= 70:
        print("C")
    if average >=60:
        print("D")
#elif structure basically else + if shortened  
main()      
        
    