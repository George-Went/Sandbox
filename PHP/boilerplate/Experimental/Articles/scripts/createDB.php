<?php
$servername = "localhost";
$username = "root";
$password = "password";/* Put your password here */


// Put database name here ----------------------------
$database_name = "articlesDB";
// ----------------------------------------------------


/* Create connection */
$conn = new mysqli($servername, $username, $password);

/* Check connection */
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}


/* sql query to run */
$sql = "CREATE DATABASE IF NOT EXISTS " . $database_name;

/* executing sql query */
if ($conn->query($sql) === TRUE) {
   echo "Database 'articles' created successfully";
}
else
{
   echo "Error creating database: " . $conn->error;
}

$conn->close();
echo "<a href='../articles.php'>Go back</a>";
?>