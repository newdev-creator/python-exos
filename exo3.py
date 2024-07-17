import random

OPERATORS = ["+", "-", "*"]
MIN_OPERAND = 3
MAX_OPERAND = 12


def generate_problem():
    left = random.randint(MIN_OPERAND, MAX_OPERAND)
    right = random.randint(MIN_OPERAND, MAX_OPERAND)
    operator = random.choice(OPERATORS)

    expr = str(left) + " " + operator + " " + str(right)
    computer_answer = eval(expr)

    return expr, computer_answer


expr, answer = generate_problem()
print(expr)
player_answer = int(input("Quel est le résultat de cette opération ?"))

if player_answer == answer:
    print("bravo!")
else:
    print("dommage, la réponse était : ", answer)
