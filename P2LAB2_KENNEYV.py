#KENNEYVAL
2/26/2026
#P2LAB2_ValerieKenney
#THIS PROJECT WILL DEMO THE USE OF DICTIONARIES

#create the dictionary the car model is key and the mpg is the value

cars = {"Camaro": 18.21, "Prius" : 52.36,"Model S" : 110,"Silverado" : 26}

#display results show a list of all keys in the dictionary
keys = cars.keys()
print(keys)
print()
#get user input get the vehicle from the user
print()
car_input = input("Enter a vehicle to see its mpg: ")
print()
#get the corresponding mpg to the vehicle's name
mpg_output = cars[car_input]
#display output
print(f"The {car_input} gets {mpg_output} mpg.\n")
#get the distance traveled
distance = float(input(f"How many miles will you drive the car {car_input}? "))
print()
#calculate gallons of gas needed
gallons_needed = distance / mpg_output
## Display the car and # of gallons needed

print(f"{gallons_needed:,.2f} gallon(s) of gas needed to drive the {car_input} {distance}miles.")
    
