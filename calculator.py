num1 = int(input("enetr the frist number:"))
num2 = int(input("enetr the second number:"))
operation = input("enetr the operation you want to perform")
if operation == '+':
    print(num1+num2)
elif operation == '-':
    print(num1-num2)
elif operation == '*':
    print(num1*num2)
elif operation == '/':
    print(num1/num2)
else:
    print("invalid operation")


