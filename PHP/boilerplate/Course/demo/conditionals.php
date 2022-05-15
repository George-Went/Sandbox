<?php

   // Conditionals 

   /* php operators 
      ==
      ===
      <
      >
      <=
      >=
      !=
      !==
   */


   $num = 5;

   if($num == 5){
      echo 'true';
   }
   elseif($num ==6){
      echo '6 passed';
   }
   else {
      'did not pass';
   }


   // Nesting if staments 

   $num = 7;
   if($num > 5){
      if ($num < 10){
         echo "$num passed";
      }
   }

   /* Logical operators 
      and    &&
      or     ||
      xor
   */
   
   if( $num > 4 and $num < 10){
      echo "$num passed";
   }

   // Switches 
   $colour = 'blue';

   switch($colour){
      case "blue":
         echo "colour is blue";
      case "red":
         echo "colour is red";
      case "green":
         echo "colour is green";

      default: 
         echo "your favorite colour is something else";
   }
   



?>