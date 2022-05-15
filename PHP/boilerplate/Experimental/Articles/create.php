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
         Title:<br>
         <input type="text" name="title">
         <br>
         Author:<br>
         <input type="text" name="author">
         <br>
         Content:<br>
         <textarea type="text" name="content" rows="1" cols="35">
         </textarea>
         <br>
         <br><br>
         <input type="submit" name="save" value="submit">
      </div>
   </div>  
</body>

</html>
