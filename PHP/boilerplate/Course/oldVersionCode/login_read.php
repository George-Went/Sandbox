

<!-- php -->
<?php 
   include "db.php";
   include "functions.php";

   $query = "SELECT * FROM users";
   $result = mysqli_query($connection, $query);// sends sql query to database 

   if(!$result){
      die("query failed" . mysqli_error());
   }
?>




<!DOCTYPE html>
<html lang="en">
   <head>
      <meta charset="UTF-8">
      <title>Document</title>
      <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css" integrity="sha384-JcKb8q3iqJ61gNV9KGb8thSsNjpSL0n8PARn9HuZOnIxN0hoP+VmmDGMN5t9UJ0Z" crossorigin="anonymous">
   </head>
   <body>
      <div class="col-sm-3">
         
         <pre> <!--  preformatted text -->
         <?php
            while($row = mysqli_fetch_row($result)){ // loops through mysql rows, echoing the results of each fetch into the preformatted tex div
               print_r($row);
            }
         ?>
         </pre>

         <pre>
         <?php
            while($row = mysqli_fetch_assoc($result)){ // associative array
               print_r($row);
            }
         ?>
         </pre>
      
      </div>
   </body>
</html>


