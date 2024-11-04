<?php session_start(); ?>

<html>
<head>
  <link rel="stylesheet" type="text/css" href="style.css">
  <script src="valid.js"></script>
</head>
<body>
  <div id="compform">
    <form method="post" action="result.php" name="comp" onsubmit="return compValidate()">
      <h1>Complaint Form</h1>
      <input type="text" name="fname" class="firstname" placeholder="First Name">
      <input type="text" name="lname" class="lastname" placeholder="Last Name"><br>
      <input type="text" name="email" class="email" placeholder="Email"><br>
      <select name="device" class="device">
        <option value="" selected>Select your Device</option>
        <option value="mobile">Mobile Phone</option>
        <option value="tv">Television</option>
        <option value="computer">Computer/Laptop</option>
        <option value="home">Home Electronics</option>
      </select>
      <div class="warranty">
        <p>Is your device under warranty?</p>
        <input type="radio" name="warranty" value="yes"> <label>Yes</label>
        <input type="radio" name="warranty" value="no"> <label>No</label><br>
      </div>
      <button type="submit">Submit</button>
    </form>
  </div>
</body>
</html>