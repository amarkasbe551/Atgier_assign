# Take user choice
choice = int(input(f"Enter your choice\n1. for with third variable\n2. for without third variable)\n:-- "))

# Take input numbers
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

if choice == 1:
    # Swap with third variable
    temp = num1
    num1 = num2
    num2 = temp
elif choice == 2:
    # Swap without third variable
    num1 = num1 + num2
    num2 = num1 - num2
    num1 = num1 - num2
else:
    print("Invalid choice. Please enter either 1 or 2.")
    exit()

print("After swapping:")
print("First number:", num1)
print("Second number:", num2)
