# Valeriekenney
 # Date2/20/26
 # P1HW2
 # BUDGET PROGRAM for Travel

#pseudocode
#Ask user to enter their budget
# Ask user to enter travel destination
# Ask user for amount they will spend on gas
# Ask user for amount they will spend on accommodation
# Ask user for amount they will spend on food
# Add expenses
# Subtract expenses from budget
# Display results

print("This program calculates and displays travel expenses\n")

budget=float(input("Enter Budget"))
print()
travel=input("Enter your travel destination.")
print()
gas=float(input("How much do you think you will spend on gas?"))
print()
hotel=float(input("approximately how much will you need for hotel/accomodations?"))
print()
food=float(input("How much will you need for food?"))
print()
print("-"*12+"Travel Expenses" +"-"*12)
print("Location",travel)
print("Initial Budget",budget)
print()
print("Fuel",gas)
print("Accomodation",hotel)
print("Food",food)
print()
balance=budget-gas-hotel-food
print("Remaining Balance:",balance)

