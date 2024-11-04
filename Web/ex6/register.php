<?php $servername = "localhost";
$username = "root";
$password = "";
$dbname = "ir_system";
$conn = new mysqli($servername,$username,$password,$dbname);
if($_SERVER['REQUEST_METHOD'] == 'POST'){
    $username =$_POST['username'];
    $password = password_hash($_POST['password'],PASSWORD_BCRYPT);
    $sql="insert into users(username,password) values ('$username','$password')";
    if ($conn->query($sql)===TRUE){
        echo "registration successfull.";
    }else{
        echo "error:".$sql."<br>".$conn->error;
    }
}
$conn->close();
?>
<form method="post">
    Username:<input type='text' name='username' required><br>
    Password:<input type='password' name='password' required><br>
    <input type="submit" value="Register">
</form>