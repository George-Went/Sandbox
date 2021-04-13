<?php
include "db.php";


function showAllData() {
// takes data from a database and displays certian rows based on the 'id' selected
   global $connection; // alllows $connection to be used across db.php and functions.php
   $query = "SELECT * FROM users";

   $result = mysqli_query($connection, $query);// sends sql query to database 

   if(!$result){
      die("query failed" . mysqli_error());
   }

   while($row = mysqli_fetch_assoc($result)){   // $row = fetch assosiative array of $result = query of 'SELECT * FROM users"
      $id = $row['id'];                         // fetch array of the id's in the database 
      echo "<option value='$id'>$id</option>";  // option value display the id's whithin the database
   } 
}


function createRows() {
   global $connection;
   $username = $_POST['username'];
   $password = $_POST['password'];

      $query = "INSERT INTO users(username, password) ";
      $query .= "VALUES ('$username', '$password')"; // .= concatonates (adds on the end) onto existing values (same as += in js)

      echo $query;

      $result = mysqli_query($connection, $query);// sends sql query to database 

      if(!$result){
         die("query failed" . mysqli_error($connection));
      }
}


function readRows() {
   global $connection;
   $query = "SELECT * FROM users";
   $result = mysqli_query($connection, $query);// sends sql query to database 

   if(!$result){
      die("query failed" . mysqli_error());
   }
   
   while($row = mysqli_fetch_assoc($result)){ // loops through mysql rows, echoing the results of each fetch into the preformatted tex div
      print_r($row);
   }
}




function updateTable() {
   global $connection; // alllows $connection to be used across db.php and functions.php

   $username = $_POST['username'];
   $password = $_POST['password'];
   $id = $_POST['id'];

   // building sql query 
   $query = "UPDATE users SET ";
   $query .= "username = '$username', ";
   $query .= "password = '$password' ";
   $query .= "WHERE id = '$id' ";

   echo $query;

   $result = mysqli_query($connection, $query);
   if(!$result) {
      die("Query failed" . mysqli_error($connection));
   }
}





function deleteRows() {
   global $connection; // alllows $connection to be used across db.php and functions.php

   $username = $_POST['username'];
   $password = $_POST['password'];
   $id = $_POST['id'];

   // building sql query 
   $query = "DELETE FROM users  ";
   $query .= "WHERE id = '$id' ";

   echo $query;

   $result = mysqli_query($connection, $query);
   if(!$result) {
      die("Query failed" . mysqli_error($connection));
   }
}


?>