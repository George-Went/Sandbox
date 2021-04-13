<?php 
    include "../includes/header.php";
?>

<body>
   <?php include "../includes/navigation.php" ?>

   <body>
   <div class="content">

      <h1>Articles Test Site </h1>
      <h3>Aim to add notes etc into database </h3>
      <h2>HTML Forms</h2>

      <li><a href="create.php"><strong>Create</strong></a> - add a user</li>
      <li><a href="read.php"><strong>Read</strong></a> - find a user</li>
      <li><a href="update.php"><strong>Update</strong></a> - edit a user</li>
      <li><a href="delete.php"><strong>Delete</strong></a> - delete a user</li>

      <h3>Alternate form design </h3>
      <li><a href="alternateForm.php"><strong>Alternate Form Design</strong></a> - Another way of managing database data</li>

      


      <h2>Database Scripts</h2>

      <li><a href="scripts/createDB.php"><strong>Create Database</strong></a> - create a database</li>
      <li><a href="scripts/createTable.php"><strong>Create Table</strong></a> - create a table</li>
      <li><a href="scripts/insert.php"><strong>Insert Data</strong></a> - insert data into a table</li>
      <li><a href="scripts/deleteDB.php"><strong>Delete Database</strong></a> - Delete the database</li>
      <li><a href="scripts/deleteTable.php"><strong>Delete Table</strong></a> - Delete the table</li>
      <li><a href="scripts/checkDB.php"><setrong>check</strong></a> - check if the database and table exist</li>
      
      <?php
            include "config.php";    // Connect to database script
            include "functions.php";
      ?>

   </div>
   </br>

   <h2>Display all Data</h2>
      <?php
         showAllData(); // read all function from functions.php
      ?>
   <?php
      
      echo $_SERVER['REQUEST_URI'];
   ?>
   
</body>

</html>


<!-- php -->
