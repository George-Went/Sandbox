<?php
$file = "example.txt";

if($handle = fopen($file, 'w')){
   fwrite($handle, "Hello World");
   fclose($handle);
} 
else {
   echo "The files could not be created";
}

?>

