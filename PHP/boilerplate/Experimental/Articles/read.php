<?php 
    include "../includes/header.php";
?>

<body>
   <?php include "../includes/navigation.php" ?>

   <body>
      <div class="content">

      <h1>CRUD Test Site </h1>
      <h2>Read Data</h2>

      <?php
         include "config.php"; // Connect to database script
         include "functions.php";
         showAllData();
      ?>

      

   </div>  
</body>

</html>
