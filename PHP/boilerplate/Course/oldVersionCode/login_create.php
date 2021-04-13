

<!-- php -->
<?php 
   if(isset($_POST['submit'])) {
      echo "yes";
      $_POST['submit'];

      $username = $_POST['username'];
      $password = $_POST['password'];

         if($username && $password) {
            echo Hello . $username;
            echo "Your password is" . $password;
         }
         else{
            echo "Username or password is not set";
         }

         

         $query = "INSERT INTO users(username, password) ";
         $query .= "VALUES ('$username', '$password')"; // .= concatonates (adds on the end) onto existing values (same as += in js)

         echo $query;

         $result = mysqli_query($connection, $query);// sends sql query to database 

         if(!$result){
            die("query failed" . mysqli_error($connection));
         }
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


