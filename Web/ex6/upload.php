<?php session_start();
if(!isset($_SESSION['user_id'])){
    header('Location: login.php');
    exit();
}
$servername='localhost';
$username='root';
$password='';
$dbname='ir_system';
$conn=new mysqli($servername,$username,$password,$dbname);
if($_SERVER['REQUEST_METHOD']==='POST'){
    $title=$_POST['title'];
    $content=$_POST['content'];
    $sql="insert into documents(title,content) values ('$title','$content')";
    if($conn->query($sql)===TRUE){
        echo 'Document uploaded scussfull.';
    }else{
        echo 'error: '.$sql.'<br>'.$conn->error;
    }
}
$conn->close(); ?>
<form method="post">
    Title: <input type="text" name="title" required><br>
    Content: <textarea name="content" required></textarea><br>
    <input type="submit" value="upload">
</form>