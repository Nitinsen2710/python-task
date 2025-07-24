<!-- git status
git add .
git commit -m "---"
git pull origin master
git push origin master -->





It includes the following two Python programs:
- ✅ Task 1: Basic Mathematical Operations
- ✅ Task 2: Personalized Greeting

---

## ✅ Task 1: Perform Basic Mathematical Operations

### 🔹 Description:
This Python program takes **two numbers** as input from the user and performs the following operations:
- Addition
- Subtraction
- Multiplication
- Division

### 🧾 Code:
# task1.py

input1 = float(input("Enter the first number: "))
input2 = float(input("Enter the second number: "))

print("Addition:", input1 + input2)
print("Substraction:", input1 - input2)
print("Multiplication:", input1 * input2)
print("Division:", input1 / input2)

#Input
Enter the first number: 10
Enter the second number: 5

#Output
Addition: 15.0
Substraction: 5.0
Multiplication: 50.0
Division: 2.0

# task2.py

input1 = input("Enter your first name: ")
input2 = input("Enter your last name: ")

print(f"Hello, {input1} {input2}! Welcome to the Python program.")

Enter your first name: John
Enter your last name: Doe

#Output
Hello, John Doe! Welcome to the Python program.


#Assignment 2

#task-1.py
The user is prompted to enter a number.
The program converts the input into an integer.
It uses the modulus operator (%) to check if the number is divisible by 2.
If the remainder is 0, the number is even.
Otherwise, the number is odd.
It prints the result accordingly.

#task-2.py
A variable num1 is initialized to 1 (starting number).
A variable sum is initialized to 0 (to store the running total).
The program enters a while loop that runs as long as num1 is less than or equal to 50.
In each iteration:
The current value of num1 is added to sum.
num1 is incremented by 1.
After the loop completes, it prints the total sum.
