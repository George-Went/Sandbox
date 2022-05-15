<?php
$servername = "localhost";
$username = "root";
$password = "password";/* Put your password */
$dbname = "articlesDB";/* Put your database name */

// Put database name here ----------------------------
$database_name = "articlesDB";
// ----------------------------------------------------


/* Create connection */
$conn = new mysqli($servername, $username, $password, $dbname);
/* Check connection*/
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

/* sql to create table */
$sql = "DROP DATABASE " . $database_name;

// checking if the sql query runs 
if ($conn->query($sql) === TRUE) {
    echo "Table deleted successfully";
}
 else {
	 // prints error to page
    echo "Error creating table: " . $conn->error;
}
$conn->close();
echo "<a href='../articles.php'>Go back</a>";
?>