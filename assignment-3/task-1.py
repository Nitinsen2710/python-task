
def factorial(num):

    if num==1:
        return 1
    else:
        return num*factorial(num-1)

number=int(input("Enter a number:"))
if number<0:
    print("It will not work for negative no.")
else:
    print(f"Factorial of {number} is: {factorial(number)}")




