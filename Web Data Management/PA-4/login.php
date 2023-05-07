<html>

<head>
    <style>
        .aa {
            text-align: center;
        }

        input {
            text-align: center;
        }
    </style>
</head>

<body>
    <div class="aa">
        <form name="form" action="board.php" method="POST">
            <input type="text" name="username" placeholder="Username" size="20" id="username" required /><br /><br />
            <input type="password" name="password" placeholder="password" size="20" id="password" required><br /><br />
            <button type="submit" class="submit" name="submit" id="submit">Login</button>
        </form>
    </div>
</body>

</html>