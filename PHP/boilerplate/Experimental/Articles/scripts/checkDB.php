<?php
$servername = "localhost";
$username = "root";
$password = "password";/* Put your password here */


/* Create connection */
$conn = new mysqli($servername, $username, $password);

/* Check connection */
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
    echo "Connection";
}
/* Create database */
$sql = "SELECT SCHEMA_NAME FROM INFORMATION_SCHEMA.SCHEMATA WHERE SCHEMA_NAME = 'articlesDB'";
   
if ($conn->query($sql) === TRUE) {
      echo "Database Exists";
}
else
{
   echo "No database found with name: articlesDB";
   echo "<br>";
   echo "Error: " . $conn->error;
}
$sql = "SHOW DATABASES LIKE 'articlesDB'";
   

if ($conn->query($sql) === TRUE) {
    echo "Database Existv2";
}

$conn->close();
echo "</br>";
echo "<a href='../articles.php'>Go back</a>";
?>