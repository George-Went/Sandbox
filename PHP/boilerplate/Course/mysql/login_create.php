

<!-- php -->
<?php 
   include "db.php";
   include "functions.php";

   include "includes/header.php";
   
   createRows();
   
?>




<!DOCTYPE html>
<html lang="en">

   <body>
      <div class="col-sm-3">
         <form action="login_create.php" method="post">
            <div class="form-group">
               <label for="username">Username</label>
               <input type="text" name="username" class="form-control">
            </div>      
            <div class="form-group">
               <label for="password">Password</label>
               <input type="text" name="password" class="form-control">
            </div>     
            <input class="btn btn-primary"type="submit" name="submit" value="submit">
         </form>
      </div>

   </body>
</html>


