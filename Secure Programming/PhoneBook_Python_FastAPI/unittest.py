'''
These test cases verify the inputs using regex for name and phone number and classify accepable inputs and bad inputs.
Student inputs are given for each types(good and bad) .
'''
# Import the re module
import re
# Import the os module
import os

# Get the terminal size
term_size = os.get_terminal_size()

# Get the width of the terminal
term_width = term_size.columns

# Define the regex patterns for name and phone number
name_pattern = r"^([A-Z][a-z]+) ([A-Z][a-z]+)$|^([A-Z][a-z]+), ([A-Z][a-z]+)|^([A-Z][a-z]+), ([A-Z][a-z]+) ([A-Z][a-z]+)$|^[a-zA-Z]+([ \'-][a-zA-Z]+)*,\s[a-zA-Z]+([ \'-][a-zA-Z]+)*\.?$|^[a-zA-Z]+(([ ]{1}[a-zA-Z]+)|([\'][a-zA-Z]+))*([-][a-zA-Z]+)$|^([A-Z][a-z]+)$"
phone_pattern = r"^[1-9]\d{4}$|^\([1-9]\d{2}\)\d{3}\-\d{4}$|^[1-9]\d{2}\-\d{4}$|^\+[1-9]\(\d{3}\)\d{3}-\d{4}$|^\+[1-9]?[0-9]\s\(\d{2}\)\s\d{3}-\d{4}$|^([1-9])\([0-9]{3}\)[.-]?[0-9]{3}[.-]?[0-9]{4}$|^\d{3}\s\d{3}\s\d{3}\s\d{4}$|^\d{5}\.\d{5}$|^\d{3}\s\d{1}\s\d{3}\s\d{3}\s\d{4}$"

# Define a function to validate inputs using regex and print a message
def validate_input(input, pattern):
    # Try to match the input with the pattern
    match = re.match(pattern, input)
    # If there is a match, print the input and a message saying it is valid
    if match:
        return input + ": is a valid input."
    # Otherwise, print the input and a message saying it is invalid
    else:
        return input + ": is an invalid input."

# Test the function with some examples
# Acceptable inputs for name
print("----------Acceptable inputs for name----------".center(term_width))
#sample inputs
validate_input("Bruce Schneier", name_pattern) # Bruce Schneier is a valid input.
validate_input("Schneier, Bruce", name_pattern) # Schneier, Bruce is a valid input.
#student inputs
validate_input("Siddhraj Solanki", name_pattern) # Siddhraj Solanki is a valid input.
print()

# Unacceptable inputs for name
print("----------Unacceptable inputs for name----------".center(term_width))
#sample inputs
validate_input("Ron O’’Henry", name_pattern) # Ron O’’Henry is an invalid input.
validate_input("L33t Hacker", name_pattern) # L33t Hacker is an invalid input.
#student inputs
validate_input("Siddhraj solanki", name_pattern) # Siddhraj solanki is an invalid input.
print()

# Acceptable inputs for phone number
print("-----------Acceptable inputs for phone number----------".center(term_width))
#sample inputs
validate_input("(703)111-2121", phone_pattern) # (703)111-2121 is a valid input.
validate_input("+32 (21) 212-2324", phone_pattern) # +32 (21) 212-2324 is a valid input.
#student inputs
validate_input("+1(682)552-8101", phone_pattern) # +1(682)552-8101 is a valid input.
print()

# Unacceptable inputs for phone number
print("-----------Unacceptable inputs for phone number----------".center(term_width))
#sample inputs
validate_input("1234567890", phone_pattern) # 1234567890 is an invalid input.
validate_input("<script>alert(“XSS”)</script>", phone_pattern) # <script>alert(“XSS”)</script> is an invalid input.
#student inputs
validate_input("SS 102-123-1234", phone_pattern) # SS 102-123-1234 is an invalid input.
print()
