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
   $i;
   echo '<br>';
   $i++;
}

// Do while 
// will always run atleast once
// Pramameters: condition 

$i = 0;

do{
   $i;
   echo '<br>';
   $i++;
}

while($i < 10);



// For each
// designed to work with arrays 

$people =['Homer', 'Marge', 'Bart', 'Lisa', 'Maggie'];







?>