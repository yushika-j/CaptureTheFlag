from itertools import permutations, product
def find_unique_solutions():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    target_values = set()

    # Generate all possible permutations of numbers
    number_permutations = permutations(numbers)

    # Generate all possible combinations of operations
    operations = ['+', '-', '*']
    op_combinations = product(operations, repeat=len(numbers) - 1)

    # Test each combination of numbers and operations
    for nums in number_permutations:
        for ops in op_combinations:
            print(ops)
            expr = ''.join('{}{}{}'.format(n, op, ' ' if i == len(ops) - 1 else ' ') for i, (n, op) in enumerate(zip(nums, ops)))
            print(expr)
            
            result = eval(expr)  # Added missing import for eval function
            if result > 0 and expr.count('=') == 0:  # Avoid counting expressions with '='
                target_values.add(result)

    # Print the unique target values
    for value in sorted(target_values):
        print(value, end=' ')

find_unique_solutions()