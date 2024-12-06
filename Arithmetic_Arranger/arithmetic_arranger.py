def arithmetic_arranger(problems, show_answers=False):
    if len(problems) > 5:
        return "Error: Too many problems."

    first_line = ""
    second_line = ""
    dashes = ""
    answers = ""

    prob_list = [problem.split() for problem in problems]

    for e in prob_list:
        num1 = e[0]
        operator = e[1]
        num2 = e[2]

        if not (num1.isdigit() and num2.isdigit()):
            return "Error: Numbers must only contain digits."
        if operator not in ["+", "-"]:
            return "Error: Operator must be '+' or '-'."
        if len(num1) > 4 or len(num2) > 4:
            return "Error: Numbers cannot be more than four digits."

        width = max(len(num1), len(num2)) + 2  # space for operator and one space
        
        if operator == "+":
            result = str(int(num1) + int(num2))
        elif operator == "-":
            result = str(int(num1) - int(num2))
        # result = str(eval(num1 + operator + num2))

        first_line += num1.rjust(width) + "    "
        second_line += operator + num2.rjust(width - 1) + "    "
        dashes += "-" * width + "    "
        answers += result.rjust(width) + "    "

    if show_answers:
        arranged_problems = f"{first_line.rstrip()}\n{second_line.rstrip()}\n{dashes.rstrip()}\n{answers.rstrip()}"
    else:
        arranged_problems = f"{first_line.rstrip()}\n{second_line.rstrip()}\n{dashes.rstrip()}"

    return arranged_problems

# Example usage:
print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]))
