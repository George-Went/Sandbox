<?php

class Car {

   // Properties 
   public $wheels = 4;  // avalible to the whole program
   protected $hood = 1; // only avalible to the class or any subclasses
   private $engine = 1; // only avalible to this class
   var $doors = 4;

   // methods (also called functions)
   function moveWheels() {
      echo "Wheels move";

      // We can use 'this' to refer to the Car class while 'inside' the Car class
      $this->wheels = 10;
   }

   function showPropety(){
      echo $this->hood;
   }
}
// Instansiate new class
$bmw = new Car();

echo $bmw->wheels;

// Depending on the property, varaibles can (or cant) be used by extended classes 
class Semi extends Car {

   function showPropety(){
      echo $this->hood;
   }
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
