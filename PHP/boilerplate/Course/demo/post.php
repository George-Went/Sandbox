<!-- php -->
<?php 
   echo $_POST['name'];
?>

<!DOCTYPE html>
<html lang="en">
   <head>
      <meta charset="UTF-8">
      <title>Document</title>
   </head>
   <body>
   <form action="post.php" method="post">
      <input name="name" type="text" placeholder="Example Form textbox">
      <br>  
      <input type="submit" name="submit">
   </form>
   </body>
</html>
