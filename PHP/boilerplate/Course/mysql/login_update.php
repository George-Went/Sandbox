<?php 
include "db.php";
include "functions.php";

if(isset($_POST['submit'])) {
  updateTable(); 
}
?>

<!DOCTYPE html>
<html lang="en">
   <head>
      <meta charset="UTF-8">
      
      <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css" integrity="sha384-JcKb8q3iqJ61gNV9KGb8thSsNjpSL0n8PARn9HuZOnIxN0hoP+VmmDGMN5t9UJ0Z" crossorigin="anonymous">
   </head>
   <body>
      <div class="col-sm-3">
         <form action="" method="post">
            <div class="form-group">
               <label for="username">Username</label>
               <input type="text" name="username" class="form-control">
            </div>      
            <div class="form-group">
               <label for="password">Password</label>
               <input type="text" name="password" class="form-control">
            </div>   
            <div class="form-group">
            <select name="id" id="">

               <?php
                  showAllData();
               ?>

               
            </select>
            </div>



            <input class="btn btn-primary"type="submit" name="submit" value="update">
         </form>
      </div>

   </body>
</html>


