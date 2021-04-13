<?php
$user = 'localhost';

// Put values into the array `db`
$db['db_host'] = "localhost";
$db['db_user'] = "root";
$db['db_pass'] = "password";
$db['db_name'] = "cms";

// define consant (whats happening in the loop)
//  define("DB_HOST", 'localhost');

// loop through array and convert into constant
foreach($db as $key => $value) {
   define(strtoupper($key), $value); // string_to_upper()
}

// mysqli_connect('server url','username','password','database')
$connection = mysqli_connect(DB_HOST, DB_USER, DB_PASS, DB_NAME);

if($connection) {
   echo "we are connected";
}
?>