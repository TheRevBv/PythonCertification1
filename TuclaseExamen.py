class TuclaseExamen():
    def arithmetic_arranger(self, problems, show_answers=False):
        if len(problems) <= 5:
            arranged_problems = []
            i = 0
            for problem in problems:
                if problem.find('+') != -1:
                    operator = '+'
                elif problem.find('-') != -1:
                    operator = '-'
                else:
                    return "Error: Operator must be '+' or '-'."
                numbers = problem.split(operator)
                numbers[0] = numbers[0].strip()
                numbers[1] = numbers[1].strip()
                if len(numbers[0]) > 4 or len(numbers[1]) > 4:
                    return "Error: Numbers cannot be more than four digits."
                if not numbers[0].isdigit() or not numbers[1].isdigit():
                    return "Error: Numbers must only contain digits."
                if len(numbers[0]) > len(numbers[1]):
                    max_length = len(numbers[0])
                else:
                    max_length = len(numbers[1])
                if i == 0:
                    arranged_problems.append("" + numbers[0].rjust(max_length + 2))
                    arranged_problems.append(operator + " " + numbers[1].rjust(max_length))
                    arranged_problems.append("-" * (max_length + 2))
                else:
                    arranged_problems[0] += "    " + numbers[0].rjust(max_length + 2)
                    arranged_problems[1] += "    " + operator + " " + numbers[1].rjust(max_length)
                    arranged_problems[2] += "    " + "-" * (max_length + 2)
                if show_answers:
                    if operator == '+':
                        answer = int(numbers[0]) + int(numbers[1])
                    else:
                        answer = int(numbers[0]) - int(numbers[1])
                    if i == 0:
                        arranged_problems.append("" + str(answer).rjust(max_length + 2))
                    else:
                        arranged_problems[3] += "    " + str(answer).rjust(max_length + 2)

                i += 1

            return "\n".join(arranged_problems)
        else:
            return "Error: Too many problems."
