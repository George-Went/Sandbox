<?php

class Car {

   // Properties 
   var $wheels = 4;
   var $hood = 1;
   var $engine = 1;
   var $doors = 4;

   // this constructor executes every time a new instance of the class is created
   function __construct(){
      echo $this->wheels = 10;
   }
}
// Instansiate new class
$bmw = new Car();
$truck = new Car();

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