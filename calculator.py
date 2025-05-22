import re
import operator

# Define supported operations
ops = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
    '%': operator.mod,
    '^': operator.pow,
    '**': operator.pow
}


def calculate(expression):
    # Match: number [optional space] operator [optional space] number
    match = re.fullmatch(r"\s*(-?\d+(?:\.\d+)?)\s*([\+\-\*/\^%]{1,2})\s*(-?\d+(?:\.\d+)?)\s*", expression)
    if not match:
        return "❌ Invalid format. Use format like: 2 + 2 or 3^2"

    num1, op, num2 = match.groups()
    num1, num2 = float(num1), float(num2)

    try:
        if op in ops:
            return f"Result: {ops[op](num1, num2)}"
        else:
            return f"❌ Unsupported operator: {op}"
    except ZeroDivisionError:
        return "❌ Division by zero is not allowed."


# Main loop
while True:
    user_input = input("Enter calculation (e.g., 2 + 2 or 5^3), or type 'exit' to quit:\n>> ")
    if user_input.lower() == 'exit':
        print("👋 Goodbye!")
        break
    result = calculate(user_input)
    print(result)
