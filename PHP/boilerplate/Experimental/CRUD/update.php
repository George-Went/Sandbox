<?php 
    include "../includes/header.php";
?>

<body>
   <?php include "../includes/navigation.php" ?>

   <body>
      <div class="content">

      <h1>CRUD Test Site </h1>
      <h2>Update Data</h2>

      <?php
         include "config.php"; // Connect to database script
         include "functions.php";
         updateRow();
      ?>


      <div class = form>
         <form method=post action=update.php>
         User: 
         <select name="id" id="id">
            <!-- <option value="id" selected="selected">Select User</option> -->
            <?php
               showId();
            ?>
         </select>
         <input type="submit" name="submit_id" value="view">
      </div>

      <div class="form">
         <?php
            showIdData();
         ?>
         <form method="post" action="update.php">
         First name:<br>
         <input type="text" name="first_name" value="<?php echo $first_name;?>">
         <br>
         Last name:<br>
         <input type="text" name="last_name" value="">
         <br>
         City name:<br>
         <input type="text" name="city_name" value="">
         <br>
         Email:<br>
         <input type="email" name="email" value=""> 
         <br><br>
         <input type="submit" name="save" value="update">
      </div>
      

   </div>  
</body>

</html>
