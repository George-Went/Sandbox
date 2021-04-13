<?php
$servername = "localhost";
$username = "root";
$password = "password";/* Put your password */
$dbname = "articlesDB";/* Put your database name */

// Put table name here ----------------------------
$table_name = "articles";
// ----------------------------------------------------


/* Create connection */
$conn = new mysqli($servername, $username, $password, $dbname);
/* Check connection*/
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

/* sql to create table */
$sql = "CREATE TABLE IF NOT EXISTS $table_name (
	`id` int(11) NOT NULL AUTO_INCREMENT,
  	`title` varchar(255) NOT NULL,
  	`author` varchar(255) NOT NULL,
  	`content` varchar(255) NOT NULL,
  	`date_created` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
	PRIMARY KEY (`id`)
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

// Link to go back
echo "<a href='../articles.php'>Go back</a>";
?>
