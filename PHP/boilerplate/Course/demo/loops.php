<?php

// Loops execute code a set number of times 

// For Loop 
// When a varaible = something, run code
// Parameters: initlisation, condition, increment 


for($i = 0; $i < 10; $i++){
   echo $i;
   echo '<br>'; // line break
}

// While loop
// Run code, check if varible still = somehting
// Parameters: condition 

$i = 0; 
while($i <10){
   echo $i;
   echo '<br>';
   $i++;
}

// Do while 
// will always run atleast once
// Pramameters: condition 

$i = 0;

do{
   echo $i;
   echo '<br>';
   $i++;
}

while($i < 10);



// For each
// designed to work with arrays 
// will execture a script for each item in an array

$people =['Homer', 'Marge', 'Bart', 'Lisa', 'Maggie'];
echo $people;

$numbers = array(234,23,4234,24,24,2);

foreach($numbers as $number){
   echo $number . '<br>';

}

// Switch statements
// more than two options availible 
// test a condition against multiple values 

$person = "homer";

switch($person){
   case "homer":                         
      echo "hey homer";
   break;  // a break stament stops the loop from running the options below it if the case has run successfully. 
   
   case "bart":
      echo "bart stop prank calling";

   case "marge":
      echo "hey midge";

   default: // default is the option if none of the other options are found
      echo "...";
   break;
}

?>

