print("**********************CALCULATOR************************")
print(" 1. Addition")
print(" 2. Subtraction")
print(" 3. Multiplication")
print(" 4. Division")
more = "y"
while more=="y":
    print("Select the operation:")
    op = input()
    num1 = int(input("Enter 1st no.:"))
    num2 = int(input("Enter 2nd no.:"))
    if op == "1":
        add = num1 + num2
        print("Result:",add)
    elif op == "2":
        sub = num1 - num2
        print("Result:",sub)
    elif op == "3":
        mul = num1 * num2
        print("Result:",mul)
    elif op == "4":
        div = num1/num2
        print("Result:",div)
    else :
        print("Invalid entry")
    print("Want to perform more calculations(y/n):")
    more=input()

