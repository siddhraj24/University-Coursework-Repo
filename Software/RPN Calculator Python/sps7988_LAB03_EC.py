
import os

# Dictionary to store operator priorities
OPERATOR_PRIORITY = {"+": 1, "-": 1, "*": 2, "/": 2, "%": 2} 
# Evaluates an operation with given operator and operands
def evaluate_operation(operator, operand1, operand2):
    if operator == "+":
        return operand1 + operand2
    elif operator == "-":
        return operand2 - operand1
    elif operator == "*":
        return operand1 * operand2
    elif operator == "/":
        return operand2 / operand1
    elif operator == "%":
        return operand2 % operand1  # Added modulo operator


# Checks if a token is an operator
def is_operator(token):
    return token in OPERATOR_PRIORITY


# Checks if a token is an opening parenthesis
def is_open_parenthesis(token):
    return token == "("


# Checks if a token is a closing parenthesis
def is_close_parenthesis(token):
    return token == ")"


# Determines the priority of an operator
def operator_priority(operator):
    return OPERATOR_PRIORITY[operator]


# Converts algebraic expression to RPN expression
def convert_to_rpn(expression):
    # Split the expression into individual tokens
    tokens = expression.split()
    # Lists to hold the output RPN expression and operators
    output = []
    operator_stack = []
    # Process each token
    for token in tokens:
        # If the token is a number, add it to the output
        if token.isdigit():
            output.append(token)
        # If the token is an operator, pop higher priority operators from the stack and add them to the output
        # until the stack is empty or the top operator has lower priority than the current operator,
        # then add the current operator to the stack
        elif is_operator(token):
            while (
                operator_stack
                and is_operator(operator_stack[-1])
                and operator_priority(operator_stack[-1]) >= operator_priority(token)
            ):
                output.append(operator_stack.pop())
            operator_stack.append(token)
        # If the token is an opening parenthesis, add it to the stack
        elif is_open_parenthesis(token):
            operator_stack.append(token)
        # If the token is a closing parenthesis, pop operators from the stack and add them to the output
        # until an opening parenthesis is encountered, then remove the opening parenthesis from the stack
        elif is_close_parenthesis(token):
            while operator_stack and not is_open_parenthesis(operator_stack[-1]):
                output.append(operator_stack.pop())
            operator_stack.pop()
    # Add any remaining operators on the stack to the output
    while operator_stack:
        output.append(operator_stack.pop())
    # Return the RPN expression
    return output


# Evaluates an RPN expression and returns the result
def evaluate_rpn(expression):
    stack = []
    # Process each token in the RPN expression
    for token in expression:
        """If the token is an operator, pop two operands from the stack,
        evaluate the operation, and push the result back onto the stack"""
        if is_operator(token):
            operand1 = int(stack.pop())
            operand2 = int(stack.pop())
            result = evaluate_operation(token, operand1, operand2)
            stack.append(result)
        # If the token is a number, push it onto the stack
        else:
            stack.append(token)
    # The final result is the only remaining value on the stack
    return int(stack[0])


# Main function that reads from the input file, converts expressions to RPN, and evaluates them
def main():
    try:
        # Open the input file
        input_file = open(os.path.join(os.getcwd(), "input_RPN_EC.txt"))
        # Process each line in the file
        for line in input_file:
            # Convert the algebraic expression to RPN
            rpn_expression = convert_to_rpn(line.strip())
            print("Result of RPN conversion:", rpn_expression)
            # Evaluate the RPN expression and print the result
            result = evaluate_rpn(rpn_expression)
            print("Resulting value:", result)
    except FileNotFoundError:
        print("Could not find the input_RPN_EC.txt file")
    except IndexError:
        print("Empty lines found in the input_RPN_EC.txt file")


if __name__ == "__main__":
    main()
