<?php 
    include "../includes/header.php";
?>

<body>
   <?php include "../includes/navigation.php" ?>

   <body>
   <div class="content">

      <h1>CRUD Test Site </h1>

      <h2>HTML Forms</h2>

      <li><a href="CRUD/create.php"><strong>Create</strong></a> - add a user</li>
      <li><a href="CRUD/read.php"><strong>Read</strong></a> - find a user</li>
      <li><a href="CRUD/update.php"><strong>Update</strong></a> - edit a user</li>
      <li><a href="CRUD/delete.php"><strong>Delete</strong></a> - delete a user</li>


      <?php
            include "config.php";    // Connect to database script
            include "functions.php";
      ?>
      
      <h2>Display all Data</h2>
      <?php
         showAllData(); // read all function from functions.php
      ?>

      <h2>Database Scripts</h2>

      <li><a href="scripts/createDB.php"><strong>Create Database</strong></a> - create a database</li>
      <li><a href="scripts/createTable.php"><strong>Create Table</strong></a> - create a table</li>
      <li><a href="scripts/insert.php"><strong>Insert Data</strong></a> - insert data into a table</li>


   </div>
   <?php

      echo $_SERVER['REQUEST_URI'];
   ?>
   
</body>

</html>


<!-- php -->
