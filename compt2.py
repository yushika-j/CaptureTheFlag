from itertools import combinations, product

def evaluate_expression(expression):
    try:
        return eval(expression)
    except ZeroDivisionError:
        return float('inf')

def find_expressions(target):
    # Generate all combinations of numbers from 1 to 15
    numbers = list(range(1, 16))
    combinations_list = []
    for r in range(1, len(numbers) + 1):
        combinations_list.extend(combinations(numbers, r))

    # Evaluate expressions for each combination
    valid_expressions = []
    for combination in combinations_list:
        # Generate all possible expressions with mixed operators for each combination
        for operators in product(["+", "-", "*"], repeat=len(combination)-1):
            expression = str(combination[0])
            for num, operator in zip(combination[1:], operators):
                expression += operator + str(num)
            result = evaluate_expression(expression)
            if result == target:
                valid_expressions.append(expression)
    return valid_expressions

# Find expressions that result in 353092
target = 353092
valid_expressions = find_expressions(target)
print("Expressions that result in", target, ":")
for expression in valid_expressions:
    print(expression)