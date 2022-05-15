

<!-- php -->
<?php 
   if(isset($_POST['submit'])) {
      echo "yes";
      $_POST['submit'];

      $username = $_POST['username'];
      $password = $_POST['password'];

         // if($username && $password) {
         //    echo Hello . $username;
         //    echo "Your password is" . $password;
         // }
         // else{
         //    echo "Username or password is not set";
         // }

      $connection = mysqli_connect('localhost','root','password','loginapp');
            if($connection) {
               echo "We are connected";
            }
            else{
               die("Database connection failed");
            }
   
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
         <form action="login.php" method="post">
            <div class="form-group">
               <lable for="username">Username</label>
               <input type="text" name="username" class="form-control">
            </div>      
            <div class="form-group">
               <lable for="password">Password</label>
               <input type="text" name="password" class="form-control">
            </div>     
            <input class="btn btn-primary"type="submit" name="submit" value="submit">
         </form>
      </div>

   </body>
</html>


