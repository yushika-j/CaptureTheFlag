from itertools import product

# Fonction pour calculer le résultat d'une équation donnée
def calculate(expression):
    return eval(expression)

# Fonction pour générer toutes les combinaisons d'opérations possibles
def generate_operations():
    operations = ['+', '-', '*']
    return product(operations, repeat=8)

# Fonction pour générer toutes les équations possibles
def generate_equations():
    numbers = [str(i) for i in range(1, 10)]
    equations = []
    for ops in generate_operations():
        equation = ''
        for i in range(8):
            equation += numbers[i] + ops[i]
        equation += numbers[-1]
        equations.append(equation)
    return equations

# Fonction pour trouver les valeurs de X ayant une unique solution
def find_unique_solutions():
    unique_solutions = []
    for X in range(1, 1000):
        equation_found = False
        for equation in generate_equations():
            if calculate(equation) == X:
                if not equation_found:
                    unique_solutions.append(X)
                    equation_found = True
                else:
                    equation_found = False
                    break
    return unique_solutions


# Affichage du résultat au format demandé
unique_solutions = find_unique_solutions()
flag = 'JFFI{' + '_'.join(map(str, unique_solutions)) + '}'
print(unique_solutions)
