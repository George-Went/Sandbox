<?php
// This script connects to the mysql database 
$servername='localhost';
$username='root';
$password='password';
$dbname = "crud";
$connection = mysqli_connect($servername,$username,$password,$dbname);
if(!$connection){
   die('Could not Connect My Sql:' .mysql_error());
}
?>