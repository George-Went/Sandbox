<?php

class Car {

   // Properties 
   static $wheels = 4; // The variable is attached to the class - not instaces of the class
   var $hood = 1;
  

   // methods (also called functions)
   function moveWheels() {
      echo "Wheels move";

      // We can use 'this' to refer to the Car class while 'inside' the Car class
      Car::$wheels = 10;
   }
}
// Instansiate new class
$bmw = new Car();

echo $bmw->hood;

echo Car::$wheel // to call any static data or functions, we need to use ::

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