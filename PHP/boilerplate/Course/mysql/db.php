<?php
$connection = mysqli_connect('localhost','root','password','loginapp'); 
// parameters (ip/adress , username, password, database name)
   if(!$connection) {
      die("Database connection failed");
   }
?>