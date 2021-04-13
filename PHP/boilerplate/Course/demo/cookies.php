
<!-- php -->

<?php 
   $name = "CookieExample";
   $value = 100;
   $experation = time() + (60 * 60 * 24 * 7 * 52) ; //unix time + use time functions to set cookie to expire in week

   setcookie($name,$value,$experation);
?>

<!DOCTYPE html>
<html lang="en">
   <head>
      <meta charset="UTF-8">
      <title>Document</title>
   </head>
   <body>
      <?php
         // we know that the cookie is a assosative array, so we can find certian values 
         if(isset($_COOKIE["CookieExample"])) {
            $cookieExample = $_COOKIE["CookieExample"]; // pass the cookie data into a variable
            echo $cookieExample;
         } else {
            $cookieExample = "";
            echo "no cookie found";
         }
      ?>
   </body>
</html>


