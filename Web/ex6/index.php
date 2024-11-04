<?php session_start(); ?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Information retrival system</title>
</head>
<body>
    <h1>Welcome to Information Retrival System</h1>
    <ul>
        <?php if(isset($_SESSION['user_id'])): ?>
            <li><a href="upload.php">Upload Document</a></li>
            <li><a href="search.php">Search Document</a></li>
            <li><a href="logout.php">Logout</a></li>
        <?php else:?>
            <li><a href="register.php">Register</a></li>
            <li><a href="login.php">Login</a></li>
        <?php endif; ?>
    </ul>
</body>
</html>
