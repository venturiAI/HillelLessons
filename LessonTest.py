# ДЗ 3.1. Найпростіший калькулятор
# перша версія для тренування логічних операторів

number_one = int(input("Enter first number: "))
operation = input("Choose operation (+, -, *, /): ")
number_two = int(input("Enter second number: "))

if operation == "+":
    print(number_one + number_two)
elif operation == "-":
    print(number_one - number_two)
elif operation == "*":
    print(number_one * number_two)
elif operation == "/":
    if number_two == 0:
        print("You can't divide by 0!")
    else:
        print(number_one / number_two)
else:
    print("Invalid operation")
###

#match-версія


number_one = float(input("Enter first number: "))
operation = input("Choose operation (+, -, *, /): ")
number_two = float(input("Enter second number: "))

match operation:
    case "+":
        result = number_one + number_two
    case "-":
        result = number_one - number_two
    case "*":
        result = number_one * number_two
    case "/":
        if number_two == 0:
            print("Division by zero!")
            result = None
        else:
            result = number_one / number_two
    case _:
        print("Unknown operation")
        result = None

if result is not None:
    print(f"Result: {result}")
    print(f"Result (float): {float(result)}")


#eval()
user_input = input("Enter expression (e.g. 10 / 0): ")

try:
    result = eval(user_input)
    print(f"Result: {result}")
except ZeroDivisionError:
    print("Нельзя делить на 0!")
except Exception as e:
    print(f"Ошибка ввода: {e}")



