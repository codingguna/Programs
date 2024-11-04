<?php session_start();
if(!isset($_SESSION['user_id'])){
    header("Location: login.php");
    exit();
}
$servername="localhost";
$username="root";
$password="";
$dbname="ir_system";
$conn=new mysqli($servername,$username,$password,$dbname);
if($_SERVER['REQUEST_METHOD']=='POST'){
    $query=$_POST['query'];
    $user_id=$_SESSION['user_id'];
    $sql="insert into search_query(query,user_id) values ('$query','$user_id')";
    $sa=$conn->query($sql);
    $search_sql="select * from documents where title like'%$query%' or content like '%$query%'";
    $result=$conn->query($search_sql);
    if($result->num_rows > 0){
        while($row = $result->fetch_assoc()){
            echo "<h2>Title:" .htmlspecialchars($row['title']). "</h2>";
            echo "<p>Content: " .nl2br(htmlspecialchars($row['content'])) . "</p>";
    }}else{
        echo "No result found.";
    }
}
$conn->close(); ?>
<form  method="post">
    search : <input type="text" name="query" ><br><br>
    <input type="submit" value="Search">
</form>