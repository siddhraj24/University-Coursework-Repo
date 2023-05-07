# RPN (Reverse Polish Notation) Calculator using Python

## Description
This project is a simple calculator that accepts Reverse Polish Notation (RPN) and displays the final answer. It is written in Python and only accepts 4 operators: "+", "-", "*", "/". Input numbers must be single digits, and the input will be in postfix notation. The input will be provided in a text file called `input_RPN.txt`.

The program will read the file and print the result for each RPN expression in a new line. Each digit and symbol will be space delimited. Intermediate steps or results need not be displayed.

Example of RPN: "4 2 +" and your output should be "6". This is a simple expression. More complex algebraic notations will be used to test your program like the one below.

Example algebraic notation: `(4 + 2 * 5) / (1 + 3 * 2)`.

Translated into RPN: "4 2 5 * + 1 3 2 * + /"

Note: Your code should be able to read the input file from the same folder (which has your .py file). Do not hard code the path to the file in your laptop/desktop. Use os to get the path and read the input file. Also, please take special care to process the line-ending character correctly; for example, if you write the program on a Mac it should work correctly when graded using Windows and vice versa.

## Extra credit
For extra credit, I have written a separate program called `sps7988_LAB03.py` that can input an algebraic expression, convert it to RPN, and then evaluate the RPN. It will print the RPN and the result in separate lines.

In addition, I have added an extra operator, and documented it in the code comments. The input file for extra credit will be called `input_RPN_EC.txt`, and it will contain algebraic expressions.

## Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
