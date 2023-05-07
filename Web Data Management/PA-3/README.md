
# Form Validation with JavaScript

## Project Description

This assignment is designed to utilize JavaScript for form validation. The purpose of this project is to be completed individually; NO groups are allowed. The task is to validate the form(s) of your web site completed in Assignment 1 and insert the modification to your HTML and CSS files.

* The required fields can be in the same form, or you can have more than one form (login, registration, contact, etc.).
* Add hints when necessary to help the user.
* Write a validation method that can be fired when the form is submitted. The method can validate the fields to ensure that they are not empty or the default value. The method will return a True value, and if it is false, you can fire off your alert and assign classes to highlight the fields that did not pass validation.
* Use Regular Expressions and patterns for validation.

Your form(s) must contain:

### Fields Requirement

1. **First and Last Name** - Only string is allowed.
2. **Address** - Street Name, apt#, City, State, Area Code (zip code)
3. **Phone Number** - The sequence must be in one of these formats:
   * (123)-456-7890
   * 123-456-7890
   * 123456-7890
4. **Email Address** - The following conditions must be met:
   * Uppercase and lowercase letters (A-Z and a-z)
   * Numeric characters (0-9)
   * Special characters - ! # $ % & ' * + - / = ? ^ _ ` { | } ~
   * Period, dot, or full stop (.) with the condition that it cannot be the first or last letter of the email and cannot repeat one after another
   * A valid domain name (for example, com, org, net, in, us, info).
5. **Password** - The following conditions must be met:
   * A password should be alphanumeric.
   * The first letter of the password should be capital.
   * Password must contain a special character (@, $, !, &, etc.).
   * Password length must be greater than 8 characters.
   * The password fields should not be empty.
6. **Date Field** - mm/dd/yyyy or mm-dd-yyyy
7. **Radio Option** - The radio option or Checkbox Option must be linked to Multi-Selection List Option (change the options available within a form based on earlier user entry for radio option or Checkbox) at least once in your form.
8. **Checkbox Option**
9. **Multi-Selection List Option** - Change the options available within a form based on earlier user entry for radio option or Checkbox.
10. **Textarea** - Check the max number of characters, and the text renders in a fixed-width font.
11. **Button** - Submit returns a message of a valid submission or error message.

## Contribution

Contributions are welcome! Feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
