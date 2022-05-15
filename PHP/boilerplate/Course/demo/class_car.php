<?php

class Car {
   function moveWheels() {
      echo "Wheels move";
   }
}

if(class_exists("Car")) {
   echo "Class exists";
} else {
   echo "class does not exist";
}

if(method_exists("Car", "moveWheels")) {
   echo "Method exists";
} else {
   echo "Method does not exist";
}

?>

<!DOCTYPE html>
<html lang="en">
   <head>
      <meta charset="UTF-8">
      <title>Document</title>
   </head>
   <body>


   </body>
</html>


<!-- php -->
<?php 

?>