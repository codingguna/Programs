<?php session_start();
$servername='localhost';
$username='root';
$password='';
$dbname='ir_system';
$conn=new mysqli($servername,$username,$password,$dbname);
if($_SERVER['REQUEST_METHOD']==='POST'){
    $username=$_POST['username'];
    $password=$_POST['password'];
    $sql="select * from users where username='$username'";
    $result=$conn->query($sql);
    if($result->num_rows>0){
        $user=$result->fetch_assoc();
        if(password_verify($password,$user['password'])){
            $_SESSION['user_id']=$user['id'];
            header('Location: upload.php');
        }else{
            echo 'invalid password.';
        }
    }else{echo 'no user found.';}
}
$conn->close(); ?>
<form method="post">
    username: <input type="text" name="username" required><br>
    password: <input type="password" name="password" required><br>
    <input type="submit" value="login">
</form>
