# Valeriekenney
 # Date4/15/26
 # P4LAB2
 # LOOPS
runAgain = 'yes'
while (runAgain.lower() == 'yes'):
    num= int(input ("enter an integer:"))
    print('\n')
    if num>=0:
        for i in range (1,13):
            print(f'{num} * {i} = {num *i}')
        print('\n')
    else:
        print("This program does not handle negative numbers!")
        print('\n')
    runAgain = input ("Do you want to run the program again? Enter yes or no: ")
    print('\n')
        
print("The program has exited")