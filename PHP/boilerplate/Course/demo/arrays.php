<?php 

// ------------------------------------------------------
// Array - variable that hold multiple values
// ------------------------------------------------------

/* There are 3 types: 
   indexed 
   assosative
   multi-dimesional
   */

$cars = array('Ford', 'Kia' ,'Audi'); //generates an array
$id = array(23, 45, 33);
echo $cars;

$people = ['Homer', 'Marge' ,'Bart']; //also generates an array 
$cars[2] = 'Lisa'; // #Arrays start at 0 
$cars[] = 'Maggie';

echo $cars;
echo $id;


echo count($cars); // give the number of variables in an array 

print_r($cars); // shows the whole array 

var_dump($cars); // shows the array and the data type of each object

// ------------------------------------------------------
// Assosative arrays 
// ------------------------------------------------------

// define a key and a value 

$people = array('Homer' => 50, 'Marge' => 49, 'Bart' => 15);

$ids = [50 => 'Homer'];

//shows the age of homer
echo $people['Homer'];

//shows who is 50
echo $ids[50];

//Adding to an assosative array 
$people['Lisa'] = 14;
echo people['Lisa'];

print_r($people);



//Multidimesional Array 
// An array within an array :O

$cars = array(
   array('Honda', 20, 10),
   array('Audi', 10, 30),
   array('Ford', 30, 15)
);

echo $cars[1][2];
// returns 

?>

