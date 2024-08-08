number = int(input("Enter a number: "))

action = input("Enter an action (+, -, *, /): ")

number_1 = int(input("Enter another number: "))

if action == "-":
    print(number - number_1)
elif action == "+":
    print(number + number_1)
elif action == "*":
    print(number * number_1)
elif action == "/":
    if number_1 != 0:
        print(number / number_1)
    else:
        print("Error")
else:
    print("Invalid action")