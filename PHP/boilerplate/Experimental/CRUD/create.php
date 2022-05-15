<?php 
    include "../includes/header.php";
?>

<body>
   <?php include "../includes/navigation.php" ?>

   <body>
      <div class="content">

      <h1>CRUD Test Site </h1>
      <h2>Create Data</h2>

      <?php
         include "config.php"; // Connect to database script
         include "functions.php";
         createRow();
      ?>
      <div class="form">
         <form method="post" action="create.php">
         First name:<br>
         <input type="text" name="first_name">
         <br>
         Last name:<br>
         <input type="text" name="last_name">
         <br>
         City name:<br>
         <input type="text" name="city_name">
         <br>
         Email:<br>
         <input type="email" name="email">
         <br><br>
         <input type="submit" name="save" value="submit">
      </div>
      

   </div>  
</body>

</html>
