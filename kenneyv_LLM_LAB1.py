
#n = int(input("How many names?: "))
#names = []
#for i in range(n):
 #   name = input(f"Name {i+1}: ").strip()
  #  names.append(name)
#print("Names:", names)  

# Simple Python Calculator
def add(x, y): return x + y
def subtract(x, y): return x - y
def multiply(x, y): return x * y
def divide(x, y): return x / y if y != 0 else "Error"

print("Select: 1.Add 2.Subtract 3.Multiply 4.Divide")
while True:
    choice = input("Enter choice (1-4): ")
    if choice in ('1', '2', '3', '4'):
        try:
            n1, n2 = float(input("Num1: ")), float(input("Num2: "))
            if choice == '1': print(n1 + n2)
            elif choice == '2': print(n1 - n2)
            elif choice == '3': print(n1 * n2)
            elif choice == '4': print(divide(n1, n2))
            if input("Again? (y/n): ").lower() == 'n': break
        except ValueError: print("Invalid number")
    else: print("Invalid choice")