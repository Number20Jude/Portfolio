def group_adjacent_numbers(char_list):
    result = []
    current = ''
    for i, char in enumerate(char_list):
        if char.isdigit() or char == '.' or (char in '+-' and (i == 0 or char_list[i - 1] in '()+-*/^|')):
            current += char
        else:
            if current:
                result.append(current)
                current = ''
            if char.strip():
                result.append(char)
    if current:
        result.append(current)
    return result

def evaluate_expression(tokens):
    tokens = tokens.copy()

    def process_operator(ops, operation, name):
        i = 0
        while i < len(tokens):
            if tokens[i] in ops:
                x = float(tokens[i - 1])
                y = float(tokens[i + 1])
                result = operation(tokens[i], x, y)
                old_expr = tokens[i - 1:i + 2]
                tokens[i - 1:i + 2] = [str(result)]
                print(f"Step ({name}): {' '.join(old_expr)} → {result}")
                i = 0  # Restart to re-scan for same-precedence ops
            else:
                i += 1

    def op_power(op, x, y):
        return x ** y if op == "^" else y ** (1 / x)

    def op_mult_div(op, x, y):
        return x * y if op == "*" else x / y

    def op_add_sub(op, x, y):
        return x + y if op == "+" else x - y

    process_operator(["^", "|"], op_power, "exponents/roots")
    process_operator(["*", "/"], op_mult_div, "multiplication/division")
    process_operator(["+", "_"], op_add_sub, "addition/subtraction")

    return tokens

def mathOperation(expr):
    step = 1
    while "(" in expr:
        open_idx = -1
        for i in range(len(expr)):
            if expr[i] == "(":
                open_idx = i
            elif expr[i] == ")":
                if open_idx != -1:
                    close_idx = i
                    inner = expr[open_idx + 1:close_idx]
                    print(f"\nStep {step}: evaluating ({' '.join(inner)})")
                    result = evaluate_expression(inner)
                    expr[open_idx:close_idx + 1] = result
                    print(f"→ Replacing ({' '.join(inner)}) with {result[0]}")
                    print(f"Current expression: {' '.join(expr)}")
                    step += 1
                    break
        else:
            break

    # Final step (no more parentheses)
    print(f"\nFinal Step {step}: evaluating final expression: {' '.join(expr)}")
    return evaluate_expression(expr)


#Start
xs = ''
while xs == '':
    mathProblem = input("Enter a mathematical equation: ")
    char_list = list(mathProblem)
    strVersion = group_adjacent_numbers(char_list)
    result = mathOperation(strVersion)
    print("\nFinal Answer:", result[0])
    xs = input("Enter space to continue, anything else to stop: ")
