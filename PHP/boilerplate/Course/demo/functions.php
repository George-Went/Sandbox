<?php 
   // A function is a block of code that can be repeatedly called

   // words on formatting
   /*
      Camel Case- myFunction()
      Lower Case - my_function()
      Pascal Case - MyFunction()
   */

   // --------------------------------------------------------------------
   // BASIC FUNCTIONS
   // --------------------------------------------------------------------

   // Create function
   function simpleFunction(){
      echo 'hello world';
   }

   // Execute function
   simpleFunction();

   // --------------------------------------------------------------------
   // Functions can also contain variables (sometimes called arguments) 
   // --------------------------------------------------------------------
   function sayHello($name = 'World'){
      echo "hello $name <br>";
   }

   sayHello('marge');
   sayHello('Bart');

   // Uncaught errors 
   // Uncaught argument exception - no variable given 
   sayHello();



   // --------------------------------------------------------------------
   // Getting values from functions 
   // --------------------------------------------------------------------
   function addNumbers($num1, $num2){
      echo $num1 + $num2;     // this does not pass a value, it only displays numbers on screen
      return $num1 + $num2;   // this just returns the values, does not echo to screen
   }
   
   addNumbers(20,3);
   echo "<br>";

   // --------------------------------------------------------------------
   // Referancing
   // --------------------------------------------------------------------
   // Referancing allows us to use an alias to call a varable 

   $number = 10;

   function addFive($number){
      return $number += 5; // += is the same as $num = $num + 5
   }

   // We can referance the existing $number by using referancing (kinda like a alias for a person) - not very common
   function addTen(&$number){ 
      return $number += 10;
   }

   addFive($number);
   echo "Value: $number <br>";

   addTen($number);
   echo "Value: $number <br>";

?>