# Message Board using PHP and MySQL

This is a project for a message board using PHP and MySQL. The goal of this project is to learn server-side web programming using PHP and a relational database system (MySQL). More specifically, you will create a message board where registered users can post messages.

## Platform
The project is developed on a PC/laptop using XAMPP, and it is tested using the Mozilla Firefox web browser. To set up the project, download the project4.zip file and extract the files inside your web server document root directory. The project contains the file createDB.sql, which has the SQL description of the tables "users" and "posts." The "users" table has columns "username," "password," "fullname," and "email." The "posts" table has columns "id," "replyto," "postedby," "datetime," and "message." The project uses primary keys "users.username" and "posts.id" and foreign keys "posts.postedby->users.username" and "posts.replyto->posts.id." To create the database, start the Apache Web Server and MySQL Database on your PC using the XAMPP manager console. Run phpMyAdmin on your browser, create a new database with the name "board," and execute the SQL code in createDB.sql to create the schema. The URL address for testing the project is http://localhost/project4/board.php.

## Requirements

* Develop the project on your PC/laptop using XAMPP and test it using your Mozilla Firefox web browser.
* Create a message board where registered users can post messages.
* Two PHP scripts must be written: `login.php` and `board.php`.
* `login.php` generates a form that has two text windows for username and password and a "Login" button.
* `board.php` has a "Logout" button, a textarea to write a message, a "New Post" button, and a list of messages.
* The board script prints all the messages in the database as a flat list ordered by date/time (newest first, oldest last).
* Messages should not be organized based on their replyto attributes.
* For each posted message, it prints:
  * The message ID.
  * The username and the fullname of the person who posted the message.
  * The date and time when this message was posted.
  * If this is a reply to a message, the ID of this message.
  * The message text.
  * A button "Reply" to reply to this message.
* If the user enters a wrong username/password and pushes "Login", it should go to the login script again.
* If the user enters a correct username/password and pushes "Login", it should go to the board script.
* If the user pushes "Logout", it should logout and go to the login script.
* The board script must always make sure that only authorized used (users who have logged-in properly) can view and post messages.
* If the user fills out the textarea and pushes the "New Post" button, it will insert the new message in the database (with null replyto attribute) and will go to the board script again.
* If the user fills out the textarea and pushes the "Reply" button, it will insert the message in the database -- but this time you need to set the replyto value, and will go to the board script again.

## Contribution

Contributions are welcome! Feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
