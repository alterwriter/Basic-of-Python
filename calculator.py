def gencalc(num1,num2):
    op = input("enter the operator : ")

    if op == "+":
        print(num1, " + ", num2, " = ", num1 + num2)
    elif op == "-":
        print(num1, " - ", num2, " = ", num1 - num2)
    elif op == "*":
        print(num1, " * ", num2, " = ", num1 * num2)
    elif op == "/":
        print(num1, " / ", num2, " = ", num1 / num2)
    else:
        print("invalid command.\n=====ERROR=====")

num1 = int(input("enter first number : "))
num2 = int(input("enter second number : "))

gencalc(num1,num2)