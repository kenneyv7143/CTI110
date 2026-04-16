#Valerie L Kenney        
# Date4/16/26
# P4HW1
# Validating scores

score_num= int(input(" How many scores do you want to enter?:"))
print()
#create an empty list
scores =[]

for num in range(1, score_num + 1):
    #collect scores
    score = float(input("Enter score #" + str(num) + ":"))
    while score < 0 or score > 100:
        print("\nInvalid SCORE entered!")
        print("Score should be between 0 and 100")  
        score = float(input("Enter score #" + str(num)+"again:"))   
    scores.append(score)
print()

# find lowest score

lowest = min(scores)
scores_modified = scores
scores_modified.remove(lowest)

#calculate average
avg = sum(scores_modified)/len(scores_modified)

if avg >= 90:
    grade = 'A'
elif avg >= 80:
    grade = 'B'
elif avg >= 70:
    grade = 'C'
elif avg >= 60:
    grade = 'D'
else:
    grade = 'F'
# display results

print("\n--------Results--------")
print("Lowest Score: {}".format(lowest))
print("Modified List: {}".format(scores_modified))
print("Average of Scores: {:.2f}".format(avg))
print("Grade: {}".format(grade))
print("-"*27)


#Ask user to enter for number of scores they would like to enter. (10 points)
#Create a loop to collect the number of scores the user wants to enter. (25 points)
#Note every time a score is entered, the following should be done
#Evaluate if the score is valid, it should be between 0 and 100 . 
#If it is not, notify the user and ask for a VALID score to be entered. (20 points)
#Hint - you will need to use more than one loop in this program
