<?php
$file = "example.txt";

if($handle = fopen($file, 'r')){

   // you read a file by selecting how many bites you want to read
   echo $content = fread($handle, 10); // Each bit is a character 
   
   // We can also read the entire file by using 'filesize'
   echo $content = fread($handle, filesize($file));

   fclose($handle);
} 
else {
   echo "The files could not be created";
}



?>

