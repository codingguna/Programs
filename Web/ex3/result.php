<?php
  
  $fname = $_POST['fname'];
  $lname = $_POST['lname'];
  $email = $_POST['email'];
  $device = $_POST['device'];
  $warranty = $_POST['warranty'];

  echo "Complaint Form Submitted:<br>";
  echo "First Name: $fname<br>";
  echo "Last Name: $lname<br>";
  echo "Email: $email<br>";
  echo "Device: $device<br>";
  echo "Warranty: $warranty<br>";
?>