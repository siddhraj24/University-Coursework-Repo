
import os

# Define a function to evaluate expressions in Reverse Polish Notation (RPN)
def calculate_rpn(expression):
    stack = []  # create an empty stack to hold the operands
    # define a dictionary of operator functions
    operators = {
        "*": lambda x, y: x * y,
        "/": lambda x, y: x / y,
        "+": lambda x, y: x + y,
        "-": lambda x, y: x - y,
    }
    # iterate over the tokens in the expression
    for token in expression:
        if token in operators:  # if the token is an operator
            # check if there are enough operands on the stack to apply the operator
            if len(stack) < 2:
                raise ValueError("Invalid expression: not enough operands for operator")
            # pop the top two operands off the stack
            operand2 = stack.pop()
            operand1 = stack.pop()
            # apply the operator function to the operands
            result = operators[token](operand1, operand2)
            stack.append(result)  # push the result back onto the stack
        else:  # if the token is an operand
            try:
                # convert the token to a float and push it onto the stack
                stack.append(float(token))
            except ValueError:
                raise ValueError("Invalid expression: invalid operand")
    # check if there are any extra values on the stack
    if len(stack) != 1:
        raise ValueError("Invalid expression: too many operands")
    return stack[-1]  # the final result is the only value left on the stack


if __name__ == "__main__":
    # construct the input file path
    input_file = os.path.join(os.getcwd(), "input_RPN.txt")
    try:
        # open the input file
        with open(input_file) as file:
            # iterate over each line in the file
            for line in file:
                # remove whitespace and split into tokens
                expression = line.strip().split()
                try:
                    # evaluate the expression and print the result
                    print(calculate_rpn(expression))
                except ValueError as e:
                    # if an error occurs, print the error message
                    print(e)
    except FileNotFoundError:
        print("Input file not found.")
    except IndexError:
        print("Empty lines found in the input file.")
