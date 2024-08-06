number = int(input("Enter a number: "))

action = input("Enter a action: ")

number_1 = int(input("Enter a number: "))

if action == "-":
    print(number - number_1)
elif action == "+":
    print(number + number_1)
elif action == "*":
    print(number * number_1)
elif action == "/":
    print(number / number_1)
