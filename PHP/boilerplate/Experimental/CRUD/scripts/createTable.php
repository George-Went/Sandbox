<?php
$servername = "localhost";
$username = "root";
$password = "password";/* Put your password */
$dbname = "crud";/* Put your database name */

/* Create connection */
$conn = new mysqli($servername, $username, $password, $dbname);
/* Check connection*/
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

/* sql to create table */
$sql = "CREATE TABLE notes
(
	`id` varchar(10) NOT NULL AUTO_INCREMENT,
	`title` varchar(55) NOT NULL,
	`content` varchar(55) NOT NULL,
	`author` varchar(55) NOT NULL
)"; 

// checking if the sql query runs 
if ($conn->query($sql) === TRUE) {
    echo "Table test created successfully";
}
 else {
	 // prints error to page
    echo "Error creating table: " . $conn->error;
}
$conn->close();
?>
