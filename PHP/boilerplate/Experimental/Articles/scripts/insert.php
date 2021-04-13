<?php

// not used at the moment
$servername='localhost';
$username='root';
$password='password';
$dbname = "crud";
$conn=mysqli_connect($servername,$username,$password,"$dbname");
if(!$conn){
   die('Could not Connect My Sql:' .mysql_error());
}

//include_once 'config.php'; // connect to database
//require_once 'config.php'; // 

if(isset($_POST['save']))  // if the submit value 'save' is selected (is submit button pressed)
{	 
   // select the variable from the form to post
   $first_name = $_POST['first_name']; // _POST is a superglobal array that contains avalible data 
   $last_name = $_POST['last_name'];
   $city_name = $_POST['city_name'];
   $email = $_POST['email'];

   echo $first_name . "<br>", $last_name . "<br>", $city_name . "<br>", $email . "<br>"; // (checking data for debug )

   // sql code to insert the form data
   $sql = "INSERT INTO Contacts (first_name, last_name, city_name, email) 
           VALUES ('$first_name','$last_name','$city_name','$email')";        // sql code to insert user data 



   // if (mysql (connects, run above sql code))
   if (mysqli_query($conn, $sql)) {
   echo "New record created successfully !";
   } 
   else {
      echo "Error: " . $sql . " " . mysqli_error($conn);
   }

   // Close connection
   mysqli_close($conn);
   
}
?>