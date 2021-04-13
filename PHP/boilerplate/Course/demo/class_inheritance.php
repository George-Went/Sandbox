<?php

class Car {

   // Properties 
   var $wheels = 4;
   var $hood = 1;
   var $engine = 1;
   var $doors = 4;

   // methods (also called functions)
   function moveWheels() {
      echo "Wheels move";

      // We can use 'this' to refer to the Car class while 'inside' the Car class
      $this->wheels = 10;
   }
}
// Instansiate new class
$bmw = new Car();
$truck = new Car();

// Changing a varaible
$bmw->wheels = 18;

// Displaying a varaible
echo $bmw->wheels . "<br>";
echo $truck->wheel = 10;

// We can inherite properties from the car class
Class Plane extends Car {
   var $engine = 2;
}

$jet = new Plane();

// the plane instance 'jet' inherates the wheels value from the car class;
echo $jet->wheel . "<br>";
echo $jet->engine;

// if(class_exist("Plane")) {
//    echo "it does";
// }

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