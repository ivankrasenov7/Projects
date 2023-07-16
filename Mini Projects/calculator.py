def calculate(num1, num2, operator):
    operations = {
        "+": lambda x, y: x + y,
        "-": lambda x, y: x - y,
        "*": lambda x, y: x * y,
        "/": lambda x, y: x / y if y != 0 else "Error: Division by zero"
    }

    try:
        result = operations[operator](int(num1), int(num2))
        if isinstance(result, str):
            print(result)
            return None
        return result
    except KeyError:
        print(f"Invalid operator. Please use a valid operator: {list(operations.keys())}")
        return None

go_program = True

while go_program:
    try:
        enter_numbers = input("Enter two numbers divided by ','")
        no1, no2 = enter_numbers.split(",")

        if int(no1) == 0 and int(no2) == 0:
            break
        if all(n.strip() == "" for n in (no1, no2)):
            print("Please enter two numbers: ")

        operator = input("Enter operator: ")

        result = calculate(no1, no2, operator)

        if result is not None:
            print(f'{no1.strip()} {operator} {no2.strip()} = {result}')

    except ValueError:
        print("Please enter two valid numbers separated by a comma.")
        continue
