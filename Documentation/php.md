
# PHP 
Post Hypertext Protocol (made up)
No one really knows what the acronym stands for

- PHP files can contain text, HTML, CSS, JavaScript, and PHP code
- PHP code is executed on the server, and the result is returned to the browser as plain HTML
- PHP files have extension ".php"

## Installing PHP
(Follow the LAMP stack guide)

## Basic PHP syntax 
PHP scripts can be placed anywhere in an exisiting HTML documnet, or can be placed in their own file.

An example of a very basic PHP file, within a html document:
```html
<!DOCTYPE html>
<html>
   <body>

      <h1>My first PHP page</h1>

      <?php
      echo "Hello World!";
      ?>

   </body>
</html> 
```

php has no keyword case sensitivity, this means that:
```
<?php
   ECHO "Hello World!<br>";
   echo "Hello World!<br>";
   EcHo "Hello World!<br>";
?>
```
is legal
However, all variable names are case sensitvie 
 
## Variables in PHP
Variables in php start with the `$` sign
```php
$txt = "george";
echo "Hello " + $txt;
```
Adding numbers:
```php
$x = 1;
$y = 2;
echo $x + $y;
```

php has 8 data types 

**Integers** − are whole numbers, without a decimal point, like 4195.

**Doubles** − are floating-point numbers, like 3.14159 or 49.1.

**Booleans** − have only two possible values either true or false.

**NULL** − is a special type that only has one value: NULL.

**Strings** − are sequences of characters, like 'PHP supports string operations.'

**Arrays** − are named and indexed collections of other values.

**Objects** − are instances of programmer-defined classes, which can package up both other kinds of values and functions that are specific to the class.

**Resources** − are special variables that hold references to resources external to PHP (such as database connections).




## Scope in PHP
PHP has 3 different variable scopes: global, local, static:
**Global**:
Variables used outside of a function will always have a global scope, they can be accessed inside and outside of functions.

**Local**:
Variables that are decelared within a function can only be accessed within the function. 

**Static**:
Once the value is set, the value does not change - however, the values can be accessed outside of the class without referancing the class first.




## Arrays 


## Loops


## Functions


## Conditionals (if statements)







## Forms

### GET 
The GET method sends the encoded user information appended to the page request. The page and the encoded information are separated by the `?` character.

Example URL showing a search funtion within www.bbc.co.uk, you can see the search terms after the `?` within the url
```
https://www.bbc.co.uk/search?q=sport
```

- The GET method produces a long string that appears in your server logs, in the browser's Location: box.
- The GET method is restricted to send upto 1024 characters only.
- Never use GET method if you have password or other sensitive information to be sent to the server.
- GET can't be used to send binary data, like images or word documents, to the server.
- The data sent by GET method can be accessed using QUERY_STRING environment variable.
- The PHP provides $_GET associative array to access all the sent information using GET method.


### POST
The POST method transfers information via HTTP headers (`<head>` parts in HTML). The information is encoded as described in case of GET method and put into a header called QUERY_STRING.

- The POST method does not have any restriction on data size to be sent.
- The POST method can be used to send ASCII as well as binary data.
- The data sent by POST method goes through HTTP header so security depends on HTTP protocol. By using Secure HTTP you can make sure that your information is secure.
- The PHP provides $_POST associative array (post data is sent using an assosiative array)to access all the sent information using POST method.


### Setting up a Form

Example form
```html
<form action="form.php" method="post">
   <input type="text" placeholder="Example Form textbox">
   <br>  
   <input type="text">
   <br>
   <input type="submit" name="submit">
</form>
```

We can check if the form works by running php code above the form: 
```php
// apache/nginx runs this code before rendering the below html
if(isset($_POST['submit'])) {
   echo "it works";
   echo $_POST;
}
```
The $_POST is what is known as a `superglobal`. This means that the variable is avalible in all scopes without the need to define the variable as a global.

### Extracting Infomation from a Form
To extract infomation from the, we can use the POST globalvariable along with referancing the name of the HTML form.

we can start by adding names to the HTML form. 
```HTML
<form action="form.php" method="post">
   <input type="text" name="username" placeholder="Enter Username">
   <br>  
   <input type="password" name="password" placeholder="Enter Password">
   <br>
   <input type="submit" name="submit">
</form>
```
This allows us to referance the form components in the future. 

We can then add the POST referancing in our php: 
```php
if(isset($_POST['submit'])) {
   echo "it works";
   echo $_POST;
   $username = $_POST['username']; // setting an array variable in POST to a variable on its own.
   $password = $_POST['password'];
   echo $username;
   echo $password;
}
?>
```

### Validating Form Data 
We can add simple validation by adding conditional statements. 

in our basic form, we can add some code to check the name length, and also add an array to simulate a database check:  
```php
if(isset($_POST['submit'])) {
   echo "it works";
   
   $minimun = 5;
   $names = array("homer", "marge", "bart", "lisa", "maggie");

   $username = $_POST['username'];
   $password = $_POST['password'];
   echo Hello . $username;
   echo "Your password is" . $password;

   //check if name is more that 5 letters 
   if(strlen($username) < $minimun ){
      echo "username has to be longer than 5 characters";
   }

   if(!in_array($username, $name)){
      echo "you are not allowed here";
   }
   else {
      echo "welcome";
   }
}
```

### External Page Submissions. 
We can send form data to external pages by changing the action of the form, so that it sends the user to a different page:
```html
<form action="form_process.php" method="post">
   <input type="text" name="username" placeholder="Enter Username">
   <br>  
   <input type="password" name="password" placeholder="Enter Password">
   <br>
   <input type="submit" name="submit">
</form>
```

In the new file `form_process.php` we can then modify the POST data that was send over from the `form.php` page. 
We can also move our php code from the form page into the `form_process.php` page 


form_process.php
```php
<?php

// apache/nginx runs this code before rendering the below html
if(isset($_POST['submit'])) {
   echo "it works";
   
   $minimun = 5;
   $names = array("homer", "marge", "bart", "lisa", "maggie");

   $username = $_POST['username'];
   $password = $_POST['password'];
   echo Hello . $username;
   echo "Your password is" . $password;

   //check if name is more that 5 letters 
   if(strlen($username) < $minimun ){
      echo "username has to be longer than 5 characters";
   }

   if(!in_array($username, $name)){
      echo "you are not allowed";
   }
   else {
      echo "welcome";
   }
}
?>
```

# Databases, SQL and PHP

## Installation of PHP and phpmyadmin

`link to LAMP stack documentation` 





## Setting up databases using SQL

## Setting up databases using phpmyadmin
Once phpmyadmin is set up, we can log in using the root account to see the existing databases within the mysql <contatiner/instance/server>? 

On the left hand side of the home page you can see a list of databases in the server, the layout is similar to a file browser, with the tables and colums set up like a collapsable directory. 

>**Note:** At the top of each 'folder' you can find the "new" tab - this allow you to create new databases/tables/columns

Example php myadmin explorer setup:
```
|Database 
---Table 
---|---Columns 
---|---|---|Indvidual Columns
---|---|---|---| Name (varchar)
               | Age (int)
               | Date of Birth (DATE)
               | Address (varchar)
```

## Setting up tables using phpmyadmin
We can set up tables in phpmyadmin by using the create table function - this should bring you to a interface that allows you to set the table name and column names. 
There are a variety of options for the table:  
**Name** - The name of the column  
**Type** - The type of data type (int/varchar etc)   
**Length/values** - The length of the data allowed in the database - if not set, will usually default to 256  
**Defaut** - The deafult value of the data (usefull if you dont want null values)  
**Collation** - The type of char set used by the data (usually set to `utf8mb4_general_ci`)  
**Attributes** - whether to set the data to a binary type or a timestamp     
**Null** - whether the data will allow null values (tick for yes)  
**A_I** - Auto Increment - the number will go up by one for each value, if checked you will not need to enter data in this column
**In_dex** - whether the column is a primary / foreign key  






### A Note on bootstrap
Bootsrtrap is a framwork that you can link to with its CSS and JS functions allowing for the quick development and deployment of front end UI elements for websites.
You can link using `href` functions to either the css or js using: 
```html
<!-- CSS only -->
<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css" integrity="sha384-JcKb8q3iqJ61gNV9KGb8thSsNjpSL0n8PARn9HuZOnIxN0hoP+VmmDGMN5t9UJ0Z" crossorigin="anonymous">

<!-- JS, Popper.js, and jQuery -->
<script src="https://code.jquery.com/jquery-3.5.1.slim.min.js" integrity="sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj" crossorigin="anonymous"></script>
<script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.1/dist/umd/popper.min.js" integrity="sha384-9/reFTGAW83EW2RDu2S0VKaIzap3H66lZH81PoYlFhbGU+6BZp6G7niu735Sk7lN" crossorigin="anonymous"></script>
<script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js" integrity="sha384-B4gt1jrGC7Jh4AgTPSdUtOBvfO8shuf57BaghqFfPlYxofvL8/KUEfYiJOMMV+rV" crossorigin="anonymous"></script>
```

## Setting up the frontend 

## Connecting to a database 
We can connect to an existing database using an inbuit api called `mysqli` 




Example connection script that can be imported/required into existing php scripts: 
```php
$servername='localhost';
$username='root';
$password='password';
$dbname = "crud";
$conn=mysqli_connect($servername,$username,$password,"$dbname");
if(!$conn){
   die('Could not Connect My Sql:' .mysql_error());
}
```
Alternate script to connect to database: 
```php
<?php
$connection = mysqli_connect('localhost','root','password','loginapp'); // parameters (ip/adress , username, password, database name)
   if($connection) {
      echo "We are connected <br>";
   }
   else{
      die("Database connection failed");
}
?>
```

## Creating data within php
We can create data by using the inbuilt `mysqli` functions to allow us to access and edit the database using SQL code which can be built and then sent to the database.
From the moment a user presses enter, a series of event occurs: 
 1. The data entered into the form is put into the `_POST` superglobal array 
 2. The `_POST` array is sent to the server 
 3. The username and password values are parsed out and assigned to induvidual varaibles
 4. The values are inserted into a SQL script 
 5. The sql script is passed to the mysql engine to run, inserting the data into the database. 



```php
<!-- php -->
<?php 
   if(isset($_POST['submit'])) {
      echo "yes";
      $_POST['submit'];

      $username = $_POST['username'];
      $password = $_POST['password'];

         // report back data (igonre security concernes for the moment)
         if($username && $password) {
            echo Hello . $username;
            echo "Your password is" . $password;
         }
         else{
            echo "Username or password is not set";
         }

      $connection = mysqli_connect('localhost','root','password','loginapp'); // parameters (ip/adress , username, password, database name)
            if($connection) {
               echo "We are connected <br>";
            }
            else{
               die("Database connection failed");
            }

            $query = "INSERT INTO users(username,password) ";
            $query .= "VALUES ('$username', '$password')"; // .= concatonates (adds on the end) onto existing values (same as += in js)


            $result = mysqli_query($connection, $query);// sends sql query to database 

            if(!$result){
               die("query failed" . mysqli_error());
            }
   }
?>
```

html
```html
<!DOCTYPE html>
<html lang="en">
   <head>
      <meta charset="UTF-8">
      <title>Document</title>
      <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css" integrity="sha384-JcKb8q3iqJ61gNV9KGb8thSsNjpSL0n8PARn9HuZOnIxN0hoP+VmmDGMN5t9UJ0Z" crossorigin="anonymous">
   </head>
   <body>
      <div class="col-sm-3">
         <form action="login_create.php" method="post">
            <div class="form-group">
               <label for="username">Username</label>
               <input type="text" name="username" class="form-control">
            </div>      
            <div class="form-group">
               <label for="password">Password</label>
               <input type="text" name="password" class="form-control">
            </div>     
            <input class="btn btn-primary"type="submit" name="submit" value="submit">
         </form>
      </div>

   </body>
</html>
```

## Reading Data with php 
We can read data from the database by using the same method as writing data - crafting and sending a SQL script to the server 

php
```php
<!-- php -->
<?php 

   $connection = mysqli_connect('localhost','root','password','loginapp'); // parameters (ip/adress , username, password, database name)
         if($connection) {
            echo "We are connected <br>";
         }
         else{
            die("Database connection failed");
         }

         $query = "SELECT * FROM users";
         


         $result = mysqli_query($connection, $query);// sends sql query to database 

         if(!$result){
            die("query failed" . mysqli_error());
         }

?>
```

html
```html
<!DOCTYPE html>
<html lang="en">
   <head>
      <meta charset="UTF-8">
      <title>Document</title>
      <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css" integrity="sha384-JcKb8q3iqJ61gNV9KGb8thSsNjpSL0n8PARn9HuZOnIxN0hoP+VmmDGMN5t9UJ0Z" crossorigin="anonymous">
   </head>
   <body>
      <div class="col-sm-3">
         
         <pre> <!--  preformatted text -->
         <?php
            while($row = mysqli_fetch_row($result)){
               print_r($row);
            }
         ?>
         </pre>

         <pre>
         <?php
            while($row = mysqli_fetch_assoc($result)){  // associative array
               print_r($row);
            }
         ?>
         </pre>
      
      </div>
   </body>
</html>
```

>**Note: Mysqli Functions**   
From: https://stackoverflow.com/questions/11480129/mysql-fetch-row-vs-mysql-fetch-assoc-vs-mysql-fetch-array  
All of the mentioned functions will return an array, the differences between them is what values that are being used as keys in the returned object.  
   ```mysql_fetch_row```: This function will return a row where the values will come in the order as they are defined in the SQL query, and the keys will span from 0 to one less than the number of columns selected.  
   ```mysql_fetch_assoc```: This function will return a row as an associative array where the column names will be the keys storing corresponding value.  
   ```mysql_fetch_array```: This function will actually return an array with both the contents of mysql_fetch_rowand mysql_fetch_assoc merged into one. It will both have numeric and string keys which will let you access your data in whatever way you'd find easiest.  
   
   It is recommended to use either _assoc or _row though.


## Updating Data 
We can update data by utilsing functions from both the creating and reading data - in the below example, we can select the id of the dataset to read the data based on the id. 

```php
include "db.php";
   $query = "SELECT * FROM users";

   $result = mysqli_query($connection, $query);// sends sql query to database 

   if(!$result){
      die("query failed" . mysqli_error($connection));
   }
```
```html
<?php 
include "db.php";
include "functions.php";

if(isset($_POST['submit'])) {
   $username = $_POST['username'];
   $password = $_POST['password'];
   $id = $_POST['id'];

   // building sql query 
   $query = "UPDATE users SET ";
   $query .= "username = '$username',";
   $query .= "password = '$password',";
   $query .= "WHERE id = '$id";

   echo $query;

   $result = mysqli_query($connection, $query);
   if(!$result) {
      die("Query failed" . mysqli_error($connection));
   }
}
?>

<!DOCTYPE html>
<html lang="en">
   <head>
      <meta charset="UTF-8">
      <title>Document</title>
   </head>
   <body>
      <div class="col-sm-3">
         <form action="" method="post">
            <div class="form-group">
               <label for="username">Username</label>
               <input type="text" name="username" class="form-control">
            </div>      
            <div class="form-group">
               <label for="password">Password</label>
               <input type="text" name="password" class="form-control">
            </div>   
            <div class="form-group">
            <select name="" id="">
               <?php
                  showAllData();
               ?>
            </select>
            </div>

            <input class="btn btn-primary"type="submit" name="submit" value="update">
         </form>
      </div>

   </body>
</html>
```


## Deleting Data
We modify the update rows functionality to just remove the row from the database, this code has already been refactored, so the delete row function is already inside `functions.php`  

functions.php
```php
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
```

login_delete.php
```html
<?php 
include "db.php";
include "functions.php";

if(isset($_POST['submit'])) {
   deleteRows();
}
?>

<!DOCTYPE html>
<html lang="en">
   <head>
      <meta charset="UTF-8">
      
      <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css" integrity="sha384-JcKb8q3iqJ61gNV9KGb8thSsNjpSL0n8PARn9HuZOnIxN0hoP+VmmDGMN5t9UJ0Z" crossorigin="anonymous">
   </head>
   <body>
      <div class="col-sm-3">
         <form action="" method="post">
            <div class="form-group">
               <label for="username">Username</label>
               <input type="text" name="username" class="form-control">
            </div>      
            <div class="form-group">
               <label for="password">Password</label>
               <input type="text" name="password" class="form-control">
            </div>   
            <div class="form-group">
            <select name="id" id="">

               <?php
                  showAllData();
               ?>

               
            </select>
            </div>



            <input class="btn btn-primary"type="submit" name="submit" value="update">
         </form>
      </div>

   </body>
</html>

```





## Notes on refactoring code from a single file into seperate functions
With our current code, we have only been programming in a single file, while this is good for starting projects, this can very quickly spiral out of control.  

### Refactoring php code
With our login_update.php form, we can move the code that selects all the users into its own function.

```php
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
      echo "<option value=''>$id</option>";     // option value display the id's whithin the database
   } 
}
?>
```

within our `login_update` function we can now use the function:
```html
<?php 
include "db.php";
include "functions.php";
?>

<!DOCTYPE html>
<html lang="en">
   <head>
      <meta charset="UTF-8">
      <title>Document</title>
      <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css" integrity="sha384-JcKb8q3iqJ61gNV9KGb8thSsNjpSL0n8PARn9HuZOnIxN0hoP+VmmDGMN5t9UJ0Z" crossorigin="anonymous">
   </head>
   <body>
      <div class="col-sm-3">
         <form action="login_create.php" method="post">
            <div class="form-group">
               <label for="username">Username</label>
               <input type="text" name="username" class="form-control">
            </div>      
            <div class="form-group">
               <label for="password">Password</label>
               <input type="text" name="password" class="form-control">
            </div>   
            <div class="form-group">
            <select name="" id="">
               <?php
                  showAllData(); // uses the function from functions.php
               ?>
            </select>
            </div>



            <input class="btn btn-primary"type="submit" name="submit" value="update">
         </form>
      </div>

   </body>
</html>
```

### Refactoring HTML code
We can also refactor html code using the same php `include` statements, the below code includes a file that contains a header for some php code.

login_create.php
```php
include "includes/header.php";
```

includes/header.php
```html
<head>
   <meta charset="UTF-8">
   <Title>Create</Title>
   <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css" integrity="sha384-JcKb8q3iqJ61gNV9KGb8thSsNjpSL0n8PARn9HuZOnIxN0hoP+VmmDGMN5t9UJ0Z" crossorigin="anonymous">
</head>
```



## PHP Security
### SQL injection 
SQL injection is when someone enters code into an unprotected form by exiting the 'string' within the form. a good example of this is the heartbleed bug.

php has the function `mysqli_read_escape_string` which is a container that ecapsulates the form data. 

In the function `createRows()` it looks like this: 

without injectioon protection
```php
$username = $_POST['username'];
$password = $_POST['password'];
```

with injection protection
```php
$username = $_POST['username'];
$password = $_POST['password'];

$username = mysqli_real_escape_string($connection, $username);
$username = mysqli_real_escape_string($connection, $password);
```

### Password Encryption 
There are different types of encyption that are used, and most are change on a regular basis as new encyption methods are cracked or discovered.

Hashing and Salting


In our funcitons, we can add the encyption features to `createRows` to encypt the password that users give. 

```php
   $username = $_POST['username'];
   $password = $_POST['password'];

   $username = mysqli_real_escape_string($connection, $username);
   $username = mysqli_real_escape_string($connection, $password);

   $hashFormat = "$2y$10$";
   $salt = "iusesomecrazystrings";

   $hash_and_salt = $hashFormat . $salt;
   
   $password = crypt($password, $hash_and_salt);
```


## PHP and the Web

### GET superglobal 
`$_GET` is a superglobal varaible - it is avalible anywhere within a program. 

The GET method sends the encoded user information appended to the page request. The page and the encoded information are separated by the `?` character.

Example URL showing a search funtion within www.bbc.co.uk, you can see the search terms after the `?` within the url
```
https://www.bbc.co.uk/search?q=sport
```

- The GET method produces a long string that appears in your server logs, in the browser's Location: box.
- The GET method is restricted to send upto 1024 characters only.
- Never use GET method if you have password or other sensitive information to be sent to the server.
- GET can't be used to send binary data, like images or word documents, to the server.
- The data sent by GET method can be accessed using QUERY_STRING environment variable.
- The PHP provides $_GET associative array to access all the sent information using GET method.

We can also see this by writing a simple script `get.php`
```php
<?php 
   print_r($_GET) // print_r prints insides of array
?>
```
when we go to `get.php` we can see that it prints out an array 
when we go to `get.php?id=10` we can now see that the array has `id=10` inside of it.

To utilise `$_GET` we can use two methods: 
- Have a user write in the query string 
- send a link with query infomation in the string.

In almost all cases the latter is chosen, with a specific url being crafted to send the user to a custom page with the `$_GET` infomation avalible.

With the below example, we can make a link that sends a user to `get.php` with an id varaible se to 20 withinside the array.  

```html
<!DOCTYPE html>
<html lang="en">
   <head>
      <meta charset="UTF-8">
      <title>Document</title>
   </head>
   <body>
      <a href="get.php?id=20">get</a>

   </body>
</html>
```


### POST
The POST method transfers information via HTTP headers (`<head>` parts in HTML). The information is encoded as described in case of GET method and put into a header called QUERY_STRING.

- The POST method does not have any restriction on data size to be sent.
- The POST method can be used to send ASCII as well as binary data.
- The data sent by POST method goes through HTTP header so security depends on HTTP protocol. By using Secure HTTP you can make sure that your information is secure.
- The PHP provides $_POST associative array (post data is sent using an assosiative array)to access all the sent information using POST method.

With the below example, we can make a link that sends a user to `post.php` that shows how the function works.  

```html
<!-- php -->
<?php 
   echo $_POST['name']; // This code runs before the page html loads.
?>

<!DOCTYPE html>
<html lang="en">
   <head>
      <meta charset="UTF-8">
      <title>Document</title>
   </head>
   <body>
   <form action="post.php" method="post">
      <input name="name" type="text" placeholder="Example Form textbox">
      <br>  
      <input type="submit" name="submit">
   </form>
   </body>
</html>

```

The $_POST is what is known as a `superglobal`. This means that the variable is avalible in all scopes without the need to define the variable as a global.

When the form is submitted with data, the `$_POST` array now has a `name` variable value, which is then printed on the *reloaded* page as the form link is recursive.  

Using inspect element, we can see the http headers used 


## TDLR 
Both `GET` and `POST` are superglobals.  
Both use assosative arrays to send infomation.
`GET` sends infomation via the url. 
`POST` sends infomation via http headers.


## Cookies 
Cookies are a request for a browser to store a small file that can be used for storing and retreiving variables. 

### Setting cookies with php  
An example of a set cookie can be seen below in `cookie.php`:   
```php
   $name = "Homer";
   $value = 100;
   $experation = time() + (60 * 60 * 24 * 7 * 52) ; 
   // (unix time) + (use time functions to set cookie to expire in week)

   setcookie($name,$value,$experation);
```
when the user accesses the page, the cookie will be added to the users computer

### Reading cookies with php
An example of reading a cookie can be seen in `cookie.php`, note the if statment, a browser will continue looking for a cookie unless you tell it to stop.

```php
   // we know that the cookie is a assosative array, so we can find certian values 
   if(isset($_COOKIE["CookieExample"])) {
      $cookieExample = $_COOKIE["CookieExample"]; // pass the cookie data into a variable
      echo $cookieExample;
   } else {
      $cookieExample = "";
      echo "no cookie found";
   }
``` 

`cookie.php`
```html
<?php 
   $name = "CookieExample";
   $value = 100;
   $experation = time() + (60 * 60 * 24 * 7 * 52) ; //unix time + use time functions to set cookie to expire in week

   setcookie($name,$value,$experation);
?>
```
We can see the cookie by using:  
**Firefox:** inspect element > network > cookies  
**Google:** inspect > application > session storage

<!DOCTYPE html>
<html lang="en">
   <head>
      <meta charset="UTF-8">
      <title>Document</title>
   </head>
   <body>
      <?php
         // we know that the cookie is a assosative array, so we can find certian values 
         if(isset($_COOKIE["CookieExample"])) {
            $cookieExample = $_COOKIE["CookieExample"]; // pass the cookie data into a variable
            echo $cookieExample;
         } else {
            $cookieExample = "";
            echo "no cookie found";
         }
      ?>
   </body>
</html>
```

### Sessions 
Session are server-side cookies
Sessions allow users infomation to be saved server side, witout needing the infomation to be passed via a url or a header. This is a great way for a server to remember who is looged in, whats in a shopping cart etc, without needing to spend resources on maintaining a database of current events. 

Session data is stored in an assosative array. 

As sessions take data from 1 page and display it on another, 2 files are needed for an example use: 

In the first file, we can set the value of a session varaible: 
session1.php:  
```php
   session_start(); // This is needed to tell php that you intend to use sessions 
   $_SESSION['greeting'] = "Hello"; // set greeting varaible to be 'hello'
```

In the second file, we can retrive this data: 
session2.php
```php
   session_start(); // This is needed to tell php that you intend to use sessions 
   echo $_SESSION['greeting']; // return the value of the 'greeting' variable
```


## Object Oriented programming in php

Class: A blueprint / Definition / Description of something in a program
Classes define both the properties of an object (varaibles, arrays, data) and the methods used (functions / behaviors)

### Defining classes in php
We can define a class by using: 
```php
class Car {} // note that the class name has to be in all caps
```

### Class methods 
A method is a function, but just inside a class
```php
class Car {

   function moveWheels() {
      echo "Wheels move";
   }
}
```
We can discover if a class or method exists by using:  
```php
if(class_exists("Car")) {
   echo "Class exists";
} else {
   echo "class does not exist";
}

if(method_exists("Car", "moveWheels")) {
   echo "Method exists";
} else {
   echo "Method does not exist";
}
```

### Instansiating Classes 
We can create a new instance of the class by using:
Remeber that creating classes does not generate an instance of a class in the program. 
```php
class Car {

   function moveWheels() {
      echo "Wheels move";
   }
}

// Instansiate class
$ford = new Car();
```

### Properties, Varaibles and Functions.
A class / object can have multiple properties / varaibles assigned to it
A function is a set of instructions within the class that can be executed by first calling the class.  
```php
class Car {

   // Properties 
   var $wheels = 4;
   var $hood = 1;
   var $engine = 1;
   var $doors = 4;

   // methods (also called functions)
   function moveWheels() {
      echo "Wheels move";

      // We can use 'this' to refer to the Car class while 'inside' the Car class
      $this->wheels = 10;
   }
}
// Instansiate new class
$bmw = new Car();
$truck = new Car();

// Changing a varaible
$bmw->wheels = 18;

// Displaying a varaible
echo $bmw->wheels . "<br>";
echo $truck->wheel = 10;
```

### Constructors 
Constructors are functions that are run when a class instance is first created, they can be used to check and test sub classes or class properties.

```php
class Car {

   // Properties 
   var $wheels = 4;
   var $hood = 1;
   var $engine = 1;
   var $doors = 4;

   // this constructor executes every time a new instance of the class is created
   function __construct(){
      echo $this->wheels = 10;
   }
}
// Instansiate new class
$bmw = new Car();
$truck = new Car();
```

### Inheritence 
classes can take on properties (and property values) form other classes. This allow sub-classes  to exist, and allows complex objects that can be built out of multiple other objects.
```php
class Car {

   // Properties 
   var $wheels = 4;
   var $hood = 1;
   var $engine = 1;
   var $doors = 4;

   // methods (also called functions)
   function moveWheels() {
      echo "Wheels move";

      // We can use 'this' to refer to the Car class while 'inside' the Car class
      $this->wheels = 10;
   }
}

// We can inherite properties from the car class
Class Plane extends Car {
   var $engine = 2; // Planes have 2 engines instead of 1
}

// Instansiate new class
$bmw = new Car();
$truck = new Car();

$jet = new Plane();

// the plane instance 'jet' inherates the wheels value from the car class;
echo $jet->wheel . "<br>";
echo $jet->engine;
```

### Class Access 
Classes can have properties that can have different levels of permissions:
**public:** can be modified by the entire program.
**protected:** can be modified by the class or `extended` classes
**private:** can only be modified within the class

```php
class Car {

   // Properties 
   public $wheels = 4;  // avalible to the whole program
   protected $hood = 1; // only avalible to the class or any subclasses
   private $engine = 1; // only avalible to this class
   var $doors = 4;

   // methods (also called functions)
   function moveWheels() {
      echo "Wheels move";

      // We can use 'this' to refer to the Car class while 'inside' the Car class
      $this->wheels = 10;
   }

   function showPropety(){
      echo $this->hood;
   }
}
// Instansiate new class
$bmw = new Car();
echo $bmw->wheels;

// Depending on the property, varaibles can (or cant) be used by extended classes 
class Semi extends Car {
   function showPropety(){
      echo $this->hood;
   }
}
```

### Static Properties
Properties that are within a class that are called static cannot be changed by instaces of the class - only the class itself. This makes them useful when you want to make sure that certian properties cannot be changed by instaces of the class.  
```php
class Car {

   // Properties 
   static $wheels = 4; // The variable is attached to the class - not instaces of the class
   var $hood = 1;
  

   // methods (also called functions)
   function moveWheels() {
      echo "Wheels move";

      // We can use 'this' to refer to the Car class while 'inside' the Car class
      Car::$wheels = 10;
   }
}
// Instansiate new class
$bmw = new Car();
echo $bmw->hood;

echo Car::$wheel // to call any static data or functions, we need to use ::
```

## Files 



















# Setting up a CMS

### A note on php error tracking
It is advised to set the php server to display errors. This can be achived by first checking the `phpinfo.php` page. If it is not avalible you can create it with the following file:   
phpinfo.php  
```php
<?php
   phpinfo();
?>
```

After visting this page, search for `display_errors`, it should say `On`. If not, you need to find the `php.ini` file for your version of php. By defualt its located at `/etc/php/<version>/apache2/php.ini`. Use the editor of your choice to change `display_errors = Off` to `display_errors = On`.

Make sure to restart apache using `systemctl restart apache2.service`

### A note on output buffering
Output buffering is (from https://stackoverflow.com/questions/2832010/what-is-output-buffering)

Without output buffering (the default), your HTML is sent to the browser in pieces as PHP processes through your script. With output buffering, your HTML is stored in a variable and sent to the browser as one piece at the end of your script.

Advantages of output buffering for Web developers:

- Turning on output buffering alone decreases the amount of time it takes to download and render our HTML because it's not being sent to the browser in pieces as PHP processes the HTML.
- All the fancy stuff we can do with PHP strings, we can now do with our whole HTML page as one variable.
- If you've ever encountered the message "Warning: Cannot modify header information - headers already sent by (output)" while setting cookies, you'll be happy to know that output buffering is your answer.

We can change the output_buffer in the `php.ini` file from `off` to `4096`

Make sure to restart apache using `systemctl restart apache2.service`




## 1. Creating Databases for the CMS 
Most of this is from: https://www.elated.com/cms-in-an-afternoon-php-mysql/#step1


### Via Terminal:   
We can run the mysql client from a terminal by entering: 
```
mysql -u <username> -p <password>
```

Create Database
```
create database cms;
```

Afterwards we can exit mysql by using:  
```
exit
```
We now have the first step for the back end of the database

## 2. Create articles table
Due to the simple nature of the database, we have only one table: `articles`.
We can create a `schema` for the table in a file - this means we can run the file multiple times if needed.

`schema`: decribes the type of data a table can hold, as well as infomation about the table itself. 

article_table.sql
```sql
DROP TABLE IF EXISTS articles; 
CREATE TABLE articles
(
  id              smallint unsigned NOT NULL auto_increment,
  publicationDate date NOT NULL,                              # When the article was published
  title           varchar(255) NOT NULL,                      # Full title of the article
  summary         text NOT NULL,                              # A short summary of the article
  content         mediumtext NOT NULL,                        # The HTML content of the article

  PRIMARY KEY     (id)
);
```


## 3. Creating a config file
While this step can be ignore or modified, one of the best ways to organize a sites codebase is by using a config file. Thia allows you to change certian variables by going into the config file, instead of having to edit the codebase itself.

>**Note:** The `define` property is used to create `constants` in php - these cant be edited once set, making them a secure way to store data.
`define("varaible_name", "value")`

cofig.php
```php
<?php
ini_set( "display_errors", true );
date_default_timezone_set( "Europe/London" );  // http://www.php.net/manual/en/timezones.php
define( "DB_DSN", "mysql:host=localhost;dbname=cms" );
define( "DB_USERNAME", "username" ); // mysql username
define( "DB_PASSWORD", "password" ); // mysql password
define( "CLASS_PATH", "classes" );
define( "TEMPLATE_PATH", "templates" );
define( "HOMEPAGE_NUM_ARTICLES", 5 ); // number of articles on homepage
define( "ADMIN_USERNAME", "admin" ); // admin acc username
define( "ADMIN_PASSWORD", "mypass" ); // admin account password
require( CLASS_PATH . "/Article.php" );


// 
function handleException( $exception ) {
  echo "Sorry, a problem occurred. Please try later.";
  error_log( $exception->getMessage() );
}

set_exception_handler( 'handleException' );
?>
```

#### Display errors in the browser
The `ini_set()` line causes error messages to be displayed in the browser. This is good for debugging, but it should be set to false on a live site since it can be a security risk.

#### Set the timezone
As our CMS will use PHP’s `date()` function, we need to tell PHP our server’s timezone (otherwise PHP generates a warning message).

#### Set the database access details
Next we define a constant, `DB_DSN`, that tells PHP where to find our MySQL database. Make sure the dbname parameter matches the name of your CMS database (cms in this case). We also store the MySQL username and password that are used to access the CMS database in the constants `DB_USERNAME` and `DB_PASSWORD`. Set these values to your MySQL username and password.

#### Set the paths
We set 2 path names in our config file: `CLASS_PATH`, which is the path to the class files, and `TEMPLATE_PATH`, which is where our script should look for the HTML template files. Both these paths are relative to our top-level cms folder.

#### Set the number of articles to display on the homepage
`HOMEPAGE_NUM_ARTICLES` controls the maximum number of article headlines to display on the site homepage. We’ve set this to `5` initially, but if you want more or less articles, just change this value.

#### Set the admin username and password
The `ADMIN_USERNAME` and `ADMIN_PASSWORD` constants contain the login details for the CMS admin user. Again, you’ll want to change these to your own values.

#### Include the Article class
Since the Article class file — which we’ll create next — is needed by all scripts in our application, we include it here.

#### Create an exception handler
Finally, we define `handleException()`, a simple function to handle any PHP exceptions that might be raised as our code runs. The function displays a generic error message, and logs the actual exception message to the web server’s error log. 
In particular, this function improves security by handling any PDO (php data objects) exceptions that might otherwise display the database username and password in the page. Once we’ve defined `handleException()`, we set it as the exception handler by calling PHP’s `set_exception_handler()` function. 





## Building the Article class 
We only need one class for the `article.php` class. This handles the storing of articles on the database, as well as retreiving articles from the database. 

Even though we only have one class, its good practice to keep our classes in a seperate directory incase of future development. 

Article.php
```php
<?php

/**
 * Class to handle articles
 */

class Article
{

  // Properties

  /**
  * @var int The article ID from the database
  */
  public $id = null;

  /**
  * @var int When the article was published
  */
  public $publicationDate = null;

  /**
  * @var string Full title of the article
  */
  public $title = null;

  /**
  * @var string A short summary of the article
  */
  public $summary = null;

  /**
  * @var string The HTML content of the article
  */
  public $content = null;


  /**
  * Sets the object's properties using the values in the supplied array
  *
  * @param assoc The property values
  */

  public function __construct( $data=array() ) {
    if ( isset( $data['id'] ) ) $this->id = (int) $data['id'];
    if ( isset( $data['publicationDate'] ) ) $this->publicationDate = (int) $data['publicationDate'];
    if ( isset( $data['title'] ) ) $this->title = preg_replace ( "/[^\.\,\-\_\'\"\@\?\!\:\$ a-zA-Z0-9()]/", "", $data['title'] );
    if ( isset( $data['summary'] ) ) $this->summary = preg_replace ( "/[^\.\,\-\_\'\"\@\?\!\:\$ a-zA-Z0-9()]/", "", $data['summary'] );
    if ( isset( $data['content'] ) ) $this->content = $data['content'];
  }


  /**
  * Sets the object's properties using the edit form post values in the supplied array
  *
  * @param assoc The form post values
  */

  public function storeFormValues ( $params ) {

    // Store all the parameters
    $this->__construct( $params );

    // Parse and store the publication date
    if ( isset($params['publicationDate']) ) {
      $publicationDate = explode ( '-', $params['publicationDate'] );

      if ( count($publicationDate) == 3 ) {
        list ( $y, $m, $d ) = $publicationDate;
        $this->publicationDate = mktime ( 0, 0, 0, $m, $d, $y );
      }
    }
  }


  /**
  * Returns an Article object matching the given article ID
  *
  * @param int The article ID
  * @return Article|false The article object, or false if the record was not found or there was a problem
  */

  public static function getById( $id ) {
    $conn = new PDO( DB_DSN, DB_USERNAME, DB_PASSWORD );
    $sql = "SELECT *, UNIX_TIMESTAMP(publicationDate) AS publicationDate FROM articles WHERE id = :id";
    $st = $conn->prepare( $sql );
    $st->bindValue( ":id", $id, PDO::PARAM_INT );
    $st->execute();
    $row = $st->fetch();
    $conn = null;
    if ( $row ) return new Article( $row );
  }


  /**
  * Returns all (or a range of) Article objects in the DB
  *
  * @param int Optional The number of rows to return (default=all)
  * @return Array|false A two-element array : results => array, a list of Article objects; totalRows => Total number of articles
  */

  public static function getList( $numRows=1000000 ) {
    $conn = new PDO( DB_DSN, DB_USERNAME, DB_PASSWORD );
    $sql = "SELECT SQL_CALC_FOUND_ROWS *, UNIX_TIMESTAMP(publicationDate) AS publicationDate FROM articles
            ORDER BY publicationDate DESC LIMIT :numRows";

    $st = $conn->prepare( $sql );
    $st->bindValue( ":numRows", $numRows, PDO::PARAM_INT );
    $st->execute();
    $list = array();

    while ( $row = $st->fetch() ) {
      $article = new Article( $row );
      $list[] = $article;
    }

    // Now get the total number of articles that matched the criteria
    $sql = "SELECT FOUND_ROWS() AS totalRows";
    $totalRows = $conn->query( $sql )->fetch();
    $conn = null;
    return ( array ( "results" => $list, "totalRows" => $totalRows[0] ) );
  }


  /**
  * Inserts the current Article object into the database, and sets its ID property.
  */

  public function insert() {

    // Does the Article object already have an ID?
    if ( !is_null( $this->id ) ) trigger_error ( "Article::insert(): Attempt to insert an Article object that already has its ID property set (to $this->id).", E_USER_ERROR );

    // Insert the Article
    $conn = new PDO( DB_DSN, DB_USERNAME, DB_PASSWORD );
    $sql = "INSERT INTO articles ( publicationDate, title, summary, content ) VALUES ( FROM_UNIXTIME(:publicationDate), :title, :summary, :content )";
    $st = $conn->prepare ( $sql );
    $st->bindValue( ":publicationDate", $this->publicationDate, PDO::PARAM_INT );
    $st->bindValue( ":title", $this->title, PDO::PARAM_STR );
    $st->bindValue( ":summary", $this->summary, PDO::PARAM_STR );
    $st->bindValue( ":content", $this->content, PDO::PARAM_STR );
    $st->execute();
    $this->id = $conn->lastInsertId();
    $conn = null;
  }


  /**
  * Updates the current Article object in the database.
  */

  public function update() {

    // Does the Article object have an ID?
    if ( is_null( $this->id ) ) trigger_error ( "Article::update(): Attempt to update an Article object that does not have its ID property set.", E_USER_ERROR );
   
    // Update the Article
    $conn = new PDO( DB_DSN, DB_USERNAME, DB_PASSWORD );
    $sql = "UPDATE articles SET publicationDate=FROM_UNIXTIME(:publicationDate), title=:title, summary=:summary, content=:content WHERE id = :id";
    $st = $conn->prepare ( $sql );
    $st->bindValue( ":publicationDate", $this->publicationDate, PDO::PARAM_INT );
    $st->bindValue( ":title", $this->title, PDO::PARAM_STR );
    $st->bindValue( ":summary", $this->summary, PDO::PARAM_STR );
    $st->bindValue( ":content", $this->content, PDO::PARAM_STR );
    $st->bindValue( ":id", $this->id, PDO::PARAM_INT );
    $st->execute();
    $conn = null;
  }


  /**
  * Deletes the current Article object from the database.
  */

  public function delete() {

    // Does the Article object have an ID?
    if ( is_null( $this->id ) ) trigger_error ( "Article::delete(): Attempt to delete an Article object that does not have its ID property set.", E_USER_ERROR );

    // Delete the Article
    $conn = new PDO( DB_DSN, DB_USERNAME, DB_PASSWORD );
    $st = $conn->prepare ( "DELETE FROM articles WHERE id = :id LIMIT 1" );
    $st->bindValue( ":id", $this->id, PDO::PARAM_INT );
    $st->execute();
    $conn = null;
  }

}

?>
```



## Front End index.php

## Back end admin.php

## Front End Templates

## Back End Templates 

## Stylesheets 


## The 

### Procedual 

### Object Oriented

### PDO 

































# Setting up a CMS (course version)

## Creating the database
creating `catagory` table structure:   
```sql
CREATE TABLE `cms`.`catagory` ( `cat_id` INT(3) NOT NULL AUTO_INCREMENT , `cat_title` INT NOT NULL , PRIMARY KEY (`cat_id`)) ENGINE = InnoDB; 
```

## Connecting to the database with php
We need to add a `/includes` directory to our file structure, as `index.php` is open to the public, we want to make sure that our database connection code is secure in a private area only acceable by the server. 

We can do this by putting it in a new secure directory called `includes`
db.php
```php
   $user = 'localhost';

   // Put values into the array `db`
   $db['db_host'] = "localhost";
   $db['db_user'] = "root";
   $db['db_pass'] = "password";
   $db['db_name'] = "cms";

   // define consant (whats happening in the loop)
   define("DB_HOST", 'localhost');

   // loop through array and convert into constant
   foreach($db as $key => $value) {
      define(strtoupper($key), $value);
   }

   // mysqli_connect('server url','username','password','database')
   $connection = mysqli_connect(DB_HOST, DB_USER, DB_PASS, DB_NAME);

   if($connection) {
      echo "we are connected";
   }
```

## Cleaning up the file structure (creating headers and footers)
As well as moving php into the `/includes` folder, we can also move html into the `/includes` folder. We can seperate out the html within `index.php` so that it is both cleaner and reusable (in the sense that you dont have to copy stuff like navbars exactly in each html page).

This can be achived using the `include` function: 
index.php
```php
include "footer.php"
```

footer.php: 
```php
<!-- Footer -->
<footer>
   <div class="row">
         <div class="col-lg-12">
            <p>Copyright &copy; Your Website 2014</p>
         </div>
         <!-- /.col-lg-12 -->
   </div>
   <!-- /.row -->
</footer>
```

The result is that `index.php` will have the footer.php text in the final html page.


## Inserting and displaying data in the catagories file
We have the main page set up, now we can insert some data into the page to display it, starting with the navigation page. Here we can add some catagories directly to the database and add them to the navigation menu. 

As we dont have the ability to upload new catagories yet, we can add them using 
```sql
INSERT INTO `catagories` (`cat_id`, `cat_title`) VALUES (NULL, 'bootstrap'), (NULL, 'javascript');
-- we can use null due to the auto_increment of the 'cat_id' column 
```

We can then output the catagories table into the database by using the following html/php code:
```php
<div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">
      <ul class="nav navbar-nav">
         <?php 

            include "db.php";
            $query = "SELECT * FROM catagories";    // create sql query
            $select_all_catagories_query = mysqli_query($connection,$query); // send query to mysql server

            while($row = mysqli_fetch_assoc($select_all_catagories_query)) {
               $cat_title = $row['cat_title'];

               echo "<li><a href='#'>{$cat_title}</a></li>";
            }
         ?>

         <!-- <li>
            <a href="#">About</a>
         </li>
         <li>
            <a href="#">Services</a>
         </li>
         <li>
            <a href="#">Contact</a>
         </li> -->
      </ul>
</div>
```

## Creating Posts and linking them to catagories 
The site is deigned to host blogging stuff, so we need to add the ability to create posts on the site. As well as this, we need a way to link them to the catagory.

For the table, we can add a variety of attributes for future content 

```sql
CREATE TABLE `posts`. ( 
   `post_id` INT(3) NOT NULL AUTO_INCREMENT ,                 
   `post_catagory_id` INT(3) NOT NULL ,
   `post_title` VARCHAR(255) NOT NULL , 
   `post_author` VARCHAR(255) NOT NULL , 
   `post_date` INT NOT NULL , 
   `post_image` TEXT NOT NULL , 
   `post_content` TEXT NOT NULL , 
   `post_tags` VARCHAR(255) NOT NULL , 
   `post_comment_count` int(11) NOT NULL , 
   `post_status` VARCHAR(255) NOT NULL ,
   `post_view_count` INT(11) NOT NULL ,
 PRIMARY KEY (`post_id`)) ENGINE = InnoDB;
```

We can create an example entry using mysql with the code below:
```sql
INSERT INTO `posts` (`post_id`, `post_catagory_id`, `post_title`, `post_author`, `post_date`, `post_image`, `post_content`, `post_tags`, `post_comment_count`, `post_status`, `post_views_count`) VALUES (NULL, '1', 'Documentation of javascript', 'George', '2020-10-16', 'doge.jpg', 'Some words on documentation', 'Documentation, javascript', '2', '', '2');
```

We now have a database table called `posts` with an example post within it.
We now need to display the data in our table in the `index.php` page.

We can use the below template for the blog posts (remeber that we are using bootstrap for the desing)
```html
   <!-- Blog Post -->
   <h2>
      <a href="#">Blog Post Title</a>
   </h2>
   <p class="lead">
      by <a href="index.php">Start Bootstrap</a>
   </p>
   <p> Posted on August 28, 2013 at 10:00 PM</p>
   <hr>
      <img class="img-responsive" src="http://placehold.it/900x300" alt="">
   <hr>
      <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Dolore, veritatis, tempora, necessitatibus inventore nisi quam quia repellat ut tempore laborum possimus eum dicta id animi corrupti debitis ipsum officiis rerum.</p>
      <a class="btn btn-primary" href="#">Read More</a>

   <hr>
```

We can then add in the php code that will dynamically create the Tile,content,author,etc from the data within the database:

First we need the query that can colled the data - this is run at the start of of the page so that we have the data we need later on, and dont need to contact the database multiple times for small amounts of data.
```php
<?php
   $query = "SELECT * FROM posts";
   $select_all_posts_query = mysqli_query($connection,$query); // send query to mysql server
   
   //this loops through each post and creates a html title tag with the posts name
   while($row = mysqli_fetch_assoc($select_all_posts_query)) { // fetches results and puts them in a assosative array
      $post_title = $row['post_title']; // creates a variable called 'post title with the value of the post_title query
      $post_author = $row['post_author'];
      $post_date = $row['post_date'];
      $post_image = $row['post_image'];
      $post_content = $row['post_content'];
      
   }
?>
```

```html
   <!-- First Blog Post -->
   <h2>
      <a href="#"><?php echo $post_title ?></a>
   </h2>
   <p class="lead">
      by <a href="index.php"><?php echo $post_author ?></a>
   </p>
   <p> Posted on <?php echo $post_date ?></p>
   <hr>
      <img class="img-responsive" src="http://placehold.it/900x300" alt="">
   <hr>
   <p><?php echo $post_content ?></p>
   <a class="btn btn-primary" href="#">Read More</a>

   <hr>
```
Now, instead of having static data, the site can read from existing database data. 

## Inserting Images into the site
The database cant store images in the table itself - but it can have a referance to where the image is located. In our case the `post_image`.
While we cant store the image in the database, we can store the file location on the server. In our case, we can create a folder called `/images`, then we can just store the file name in the database, knowing that it will link to the directory.

Getting all the relivent data for the content - including the image location.
```php
<?php
   $query = "SELECT * FROM posts";
   $select_all_posts_query = mysqli_query($connection,$query); // send query to mysql server
   
   //this loops through each post and creates a html title tag with the posts name
   while($row = mysqli_fetch_assoc($select_all_posts_query)) { // fetches results and puts them in a assosative array
      $post_title = $row['post_title']; // creates a variable called 'post title with the value of the post_title query
      $post_author = $row['post_author'];
      $post_date = $row['post_date'];
      $post_image = $row['post_image'];
      $post_content = $row['post_content'];         
   }
?>
```

We can then just echo the image location along with the `/images` directory to get the image source.

html code to display the stored image
```php
<img class="img-responsive" src="images/<?php echo $post_image;?>" alt="">
```


## Creating a custom search engine.
A search bar is a useful thing for users to find specific content within a website.

We can start off by creating a form that allows users to enter in data. 

```php

   <!-- Blog Search Well -->
   <div class="well">
      <h4>Blog Search</h4>
      <form action="" method="post">
      <div class="input-group">
         <input type="text" class="form-control">
         <span class="input-group-btn">
               <button name="submit"class="btn btn-default" type="submit">
                  <span class="glyphicon glyphicon-search"></span>
         </button>
         </span>
      </div>
      </form>
      <!-- /.input-group -->
   </div>
```
>**Note:** The `<span>` element can be used to create a sort of inline `<div>`. This allows for multiple html elements to be within the same 'line'.

We can check that the form works by 'catching' the data using a 
`$_POST` php command **above** the form. when we refesh the page, the data stored in the header (beacuse its using `$_POST`) will be displayed above the form. 

```php
<?php
echo $_POST['search'];
?>
```
When we enter infomation, we can see that the search value has been stored in `$_POST`.

Now that we have the search data, we can insert it into a query to send to the database. 
```php
if(isset($_POST['submit'])){
   echo $_POST['search'];

   $search = $_POST['search'];

   $query = "SELECT * FROM posts WHERE post_tags LIKE = '%$search%'";
}
```
> **Note:** The `LIKE` operator is used to search for specific patterns in a value. We can use the `%` on either side of the value to say that we want to find any `post_tags` that have the search string value in them. 

> More info can be found at: https://www.w3schools.com/sql/sql_like.asp


We can then add on the code needed to send the query to the database - and the code for error messages if it encounters a problem. We can also move our php script into its own file, and just use `include search_script.php`

```php
if(isset($_POST['submit'])){
   echo $_POST['search'];

   $search = $_POST['search'];

   $query = "SELECT * FROM posts WHERE post_tags LIKE '%$search%' ";

   $search_query = mysqli_query($connection, $query);
   if(!$search_query){
      die("Query Failed" . mysqli_error($connection));
   }

   $count = mysqli_num_rows($search_query);
   if($count == 0){
      echo "<h1>No Result</h1>";
   }
   else {
      echo "Some Result";
   }
}
```


Now that we have a working (if basic) search function, we need to create a page that displayes the results.  

To start off, we can take most of `index.php` and cut it so that only the basics of the page are shown. Then, we can insert our php code into the area where a blog would normally show up, such as the resutls. 

The search function just places the blog post inside a wrapper that means that `$query` is only pulling results from the search SQL function, rather than just pulling every result from the database

index.php SQL function:
```php
$query = "SELECT * FROM posts";
```
search.php SQL function:
```php
$query = "SELECT * FROM posts WHERE post_tags LIKE '%$search%';
```


(`search.php` file in github project link)





## Adding catagories to the sidebar
The catagories setup is very similar to the post content, in that we select specific data from a single table in the database and display it. 

First we get our catagories from the `catagories` table using:
```php
$query = "SELECT * FROM catagories";
$select_catagories_sidebar = mysqli_query($connection,$query);
```

Then, within our blog catagories, we can loop through the database and create a list (`li`) of all the catagories in our database. 

```php
//this loops through each catagory and creates a html title tag with the catagory name
while($row = mysqli_fetch_assoc($select_catagories_sidebar)) 
{ 
   
   $cat_title = $row['cat_title']; //Grabs current row title
   echo "<li><a href = '#'>{$cat_title}</a></li>"; //Creates a list object with that row/cat_title.
}
```





## Working on Admin Features.
The site can also have admin features that allows us to upload articles.


## Catagories Admin Page
We can start off by creating a catagories admin page, allowing for 

### Emmet abbriviation 
You can speed up the generation of html elements in some code editors by using emmet abberviation. 

```table>thread>tr>th*2```  
will be refactored automatically into
```html
<table>
   <thread>
      <tr>         <!-- Thread Row -->
         <th></th> <!-- Thread Header -->
         <th></th>
      </tr>
   </thread>
</table>
```

## Displaying Data in the Catagories Page
We can create our first page in admin with the ability display catagories we have set up in the CMS site. 

Specifically, the page's table can get data from the catagories table 

catagories table div
```html
<div class="col-xs-6">
   <!-- Connecting to the database and selecting all from catagories table-->
   <?php
      $query = "SELECT * FROM catagories";
      $select_catagories_sidebar = mysqli_query($connection,$query); // send query to mysql server to select all catagories
   ?>
   <table class="table table-bordered table-hover">
      <tr>
         <th>Id</th>
         <th>Catagory Title</th>
      </tr>
      <tbody>
         <tr>
         <!-- Inserting catagory data into a html table -->
         <?php 
            //this loops through each post and creates a html title tag with the posts name
            while($row = mysqli_fetch_assoc($select_catagories_sidebar)) 
            { // fetches results and puts them in a assosative array
               $cat_id = $row['cat_id'];
               $cat_title = $row['cat_title']; // creates a variable called 'cat title with the value of the cat_title query 
               
               echo "<tr>";
               echo "<td>{$cat_id}</td>";
               echo "<td>{$cat_title}</td>";
               echo "</tr>";
            }
         ?>
         </tr>
      </tbody>
   </table>
</div>
```

## Adding New Catagories
Now that we have exisitng catagories displayed, we can now add the ability to add new catagories to the site via the admin/catagories page.]

We can first create a form to allow users to enter in a new catagory name:   
```html
<form action="" method="post">
   <div class="form-group">
      <input type="text" name="cat_title">
   </div>
   <div class="form-group">
      <input type="submit" name="submit" value="Add Catagory">
   </div>
   <div class="form-group">
      <input class="btn btn-primary" type="submit" name="submit" value="submit">
</div>
```
Then we can add the php code (above the form) to allow us to create new catagories in the database:  
```php
if(isset($_POST['submit'])){

   $cat_title = $_POST['cat_title']; // varaible 'cat_title is given the value of the form input "cat_title"

   if($cat_title == "" || empty($cat_title)){ // if cat_title is empty, tell the user
      echo "This field should not be empty";
   } 
   else 
   {
      $query = "INSERT INTO catagories($cat_title)";
      $query .= "VALUE('{$cat_title}')";

      $create_catagory_query = mysqli_query($connection, $query); // connects to mysql database and peforms the above query
      
      // If query fails, report error
      if(!$create_catagory_query){
         die('QUERY FAILED' . mysqli_error($connection));
      }
   }
}
```


## Deleting Data
Sometimes we enter in the wrong infomation and we need to delete the data present. We can add a delete button to our catagories table to allow us to remove unwanted data.

The code below adds a delete button to every catagory in the table, with the added link that creates a speciifc url with the id of the catagory e.g. `catagories.php?delete=1` for javascript.  

```php
<?php 

   while($row = mysqli_fetch_assoc($select_catagories_sidebar)) 
   { // fetches results and puts them in a assosative array
      $cat_id = $row['cat_id'];
      $cat_title = $row['cat_title']
      
      echo "<tr>";
      echo "<td>{$cat_id}</td>";
      echo "<td>{$cat_title}</td>";
      // Adds a link that uses the catagory id as part of the url
      echo "<td><a href='catagories.php?delete={$cat_id}'>Delete</a></td>";
      echo "</tr>";
   }
?>
```
We can also add the code that allows us to remove the catagory from the table when we press the delete button:
```php
   if(isset($_GET['delete'])){ 
      $cat_id = $_GET['delete'];
   $query = "DELETE FROM catagories WHERE cat_id = {$cat_id}";
   $delete_query = mysqli_query($connection, $query);
   }
```

## Updating Catagories 
The last part we need to add to out catagories form is being able to update catagories. We can take a lot of the code from both the delete and create options.  
For the UI, we can use a update button in a similar fashion to the delete button, allowing us to create a custome url that will execute a php script when the used accesses it.

## Adding the ability to update catagories
We can first start with adding an update button into the existing generated list:  
catagories.php
```php
//grab all catagories
$query = "SELECT * FROM catagories";  

// send query to mysql server to select all catagories                                       
$select_catagories_sidebar = mysqli_query($connection,$query); 

//this loops through each post and creates a html title tag with the posts name
while($row = mysqli_fetch_assoc($select_catagories_sidebar)) 
{ // fetches results and puts them in a assosative array
$cat_id = $row['cat_id'];
$cat_title = $row['cat_title']; // creates a variable called 'cat_title with the value of the cat_title query 

echo "<tr>";
echo "<td>{$cat_id}</td>";
echo "<td>{$cat_title}</td>";
// Generate custom urls that point towards php scripts to update/delete catagories
echo "<td><a href='catagories.php?update={$cat_id}'>Update</a></td>";
echo "<td><a href='catagories.php?delete={$cat_id}'>Delete</a></td>";
echo "</tr>";
}                 
```
when the user clicks on the update button, a url is generated with the catagory name, instead of just activating a php script to delete the catagory, we can use the `cat_id` from this new url to reload the page with additional features.


## Creating the Form
The main feature is that once we have a url with a cat_id, we can then send a query to the database to retrive the current infomation on 
































# Setting up a PHP + MySQL CRUD

### Requirements 
Web server 
PHP 

### Goals
Create MySQL Records 
Insert new records into the Contacts table.

Read MySQL Records
Reading MySQL records and display them in an HTML table.

Update MySQL Records
Update existing MySQL records in the Contacts table.

Delete MySQL Records  
Confirm and delete records from the Contacts table.

GET and POST Requests 
Send data to our app from an HTML form and URL parameters.

Prepared Statements 
Secure our SQL statements with prepared statements.


## Creating the database and setting up tables
We first need a database table that we can edit, unlike noSQL tables, a SQL table first has to be generated before someone can input data into the table. 

We need an:
- id
- name
- address 
- age

We can execute the following code to create a table named `contacts`: 


### Creating the database via a terminal
Entering mySQL via a terminal: `mysql -u root -p`
This will propmt you with a password, if entering with root 
 
Show all databases:  
`show databases;`

Create new database:  
`create database [database];`  

Select database:   
`use [database];`

Now we have access to the database that we need, we  can enter in the sql code. This can be achived either by:   
- pasting in the code into the command line.
- executing a file with the sql code inside. 

File `createDB.sql`
```sql
CREATE TABLE IF NOT EXISTS `contacts` (
	`id` int(11) NOT NULL AUTO_INCREMENT,
  	`name` varchar(255) NOT NULL,
  	`email` varchar(255) NOT NULL,
  	`phone` varchar(255) NOT NULL,
  	`created` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
	PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
```

we can run the above sql code using 
```sql
source <path_to_sql_file>/file.sql
```

for example: 
```sql
source /home/george/Documents/Programming/Projects/PHP/boilerplate/CRUD/createDB.sql
```

>**Note:** You can also  create the database using alternate methods such as generating it or importing the code into a database admin panel such as phpmyadmin.

### Inserting example data into the database 
We now have the database set up. The below code can add some example  data into our new database table:

```
INSERT INTO `contacts` (`id`, `name`, `email`, `phone`, `created`) VALUES
(1, 'Homer', 'homersimpson@example.com', '2026550143', '2019-05-08 17:32:00'),
(2, 'Marge', 'marge@example.com', '2025550121', '2019-05-08 17:28:44'),
(3, 'Bart', 'bart@example.com', '2004550121', '2019-05-08 17:29:27'),
(4, 'Ned', 'ned@example.com', '2022550178', '2019-05-08 17:29:27')
```

The above code adds 4 rows to the database. 




## Creating the application frontend 
The application can consist of 4 pages (this is an example, we can reformat it later):
- Navigation Page
- Creating Data
- Reading Data
- Updating Data
- Deleting Data

### Navigation Page 
We can use the navigation page to access other pages: 
```html
<!DOCTYPE html>
<html lang="en" dir="ltr">

<head>
   <meta charset="utf-8"> <!-- defienes character types  -->
   <title>Title</title> <!-- Specifices a title for a document-->
   <link rel="stylesheet" href="index.css"> <!-- link to the css stylesheet-->
</head>

<body>
   <div class="content">

      <h1>CRUD Test Site </h1>

      <h2>HTML Forms</h2>

      <li><a href="insert.php"><strong>Create</strong></a> - add a user</li>
      <li><a href="read.php"><strong>Read</strong></a> - find a user</li>
      <li><a href="update.php"><strong>Update</strong></a> - edit a user</li>

      <h2>Database Scripts</h2>
      <li><a href="scripts/createDB.php"><strong>Create Database</strong></a> - create a database</li>
      <li><a href="scripts/createTable.php"><strong>Create Table</strong></a> - create a table</li>
   </div>
</body>

</html>
```

#### Creating a entry
We can use this page to insert new data into the database - this page includes a referance to input.php - a php script in a seperate file. 

insert.html
```html
<!DOCTYPE html>
<html>
  <body>
	<form method="post" action="scripts/insert.php">
		First name:<br>
		<input type="text" name="first_name">
		<br>
		Last name:<br>
		<input type="text" name="last_name">
		<br>
		City name:<br>
		<input type="text" name="city_name">
		<br>
		Email:<br>
		<input type="email" name="email">
		<br><br>
		<input type="submit" name="save" value="submit">
	</form>
  </body>
</html>
```

script.php
```php
<?php

// connections to php code 
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

if(isset($_POST['save']))  // if the submit value 'save' is selected
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
```

### Reading Entries






























### MVC Model View Framework  
```
              --> Browser  --
             |              |
View  -->  Controller  <- Router
             |
           Model   <--/-->  DB
``` 
(Best i can do on md atm)

































# Travisy Media Tutorial Notes 


## File Structure 
```
mvc_program/
├── app       // This is where the MVC strucuter is made 
│   ├── bootstrap.php  // Not twitter bootstrap 
│   ├── controllers
│   ├── helpers                // Small scripts such as redirect functions + sessions
│   ├── libraries
│   │   ├── controller.php     // Load models and views from other classes
│   │   ├── core.php           // analysing URLS for POSTS and grabbing data
│   │   └── database.php       // database links and scripts
│   ├── models
│   └── views
└── public // Where main index.php file goes - everything routes thorugh here
           // Static assests are routed through here    
    ├── css
    │   └── style.css
    ├── img
    ├── index.php
    └── js
        └── main.js
```

In app/ we can add `.htaccess` file that allows us to block clients from accesing the file directories from the website. 

However, this is not needed if you have access to the main server hosting the apache configuration, as you can set the `AllowOveride` to circumnavigate the permissions.  
http://httpd.apache.org/docs/current/howto/htaccess.html#when



## Directing everything through index.php
We can use the `.htaccess` file to allow us to modify how we can request POST data within php code - this is usually enable by defualt on third party apache builders such as xampp or wampp for self hosting testing servers, but for basic apache installs it is needed (sometimes).   

The main thing this file does is that any requested route that does not exist, the client will be returned to the index page. (if you've worked with node / django its like being able to set up a 404 page)

>**Note:** To use `.hcaccess` files, you need to set the `AllowOveride` to `All` instead of none. The default location for the apache config files can be found at `/etc/apache2/apache.conf`  

apache.conf files (found at `/etc/apache2`)
```
<Directory />
	Options FollowSymLinks
	AllowOverride None
	Require all denied
</Directory>

<Directory /usr/share>
	AllowOverride None
	Require all granted
</Directory>

<Directory /var/www/>
	Options Indexes FollowSymLinks
	AllowOverride All
	Require all granted
</Directory>
```

>**Note:** You may also need to allow mod_rewrites if not using xampp or wamp servers. This can be achived by using `sudo a2enmod rewrite`. Make sure to restart apache2 using `sudo systemctl restart apache2`.

mvc_program/public/.htaccess
```
<IfModule mod_rewrite.c>
  Options -Multiviews                    // Remove multiviews ability
  RewriteEngine On                      // Allow rewrite rules 
  RewriteBase /TraversyCourse/public    // Root file to use
  RewriteCond %{REQUEST_FILENAME} !-d   // If file is not found
  RewriteCond %{REQUEST_FILENAME} !-f   // 
  RewriteRule  ^(.+)$ index.php?url=$1 [QSA,L] // GOTO this rewite rule - (which is send user to index.php)
</IfModule>
```
We can also add another .htaccess file in the root of the program that allows us to redirect uses from the root url to the `public/index.php page`.

mvc_program/.htaccess
```
<IfModule mod_rewrite.c>
  RewriteEngine on
  RewriteRule ^$ public/ [L]
  RewriteRule (.*) public/$1 [L]
</IfModule>
```

This allows us to resirect any non-working url back to the index page. For example a user going to `site/post/red` would be redirected to `site/index.php`

Extra infomation on `.htaccess` files can be found at: https://hostadvice.com/how-to/how-to-enable-apache-mod_rewrite-on-an-ubuntu-18-04-vps-or-dedicated-server/

## Bootstrap File and Core Classes 
Calling functions can be done in a php file, however if your constantly using the same classes / functions, it can be easier to group them together into the same class: This is what `bootstrap.php` is for.

bootstrap.php
```php
<!-- This is not the twitter bootstrap, this requires all the helpers / configs  -->
<?php 
// Load libraries
require_once '../app/libraries/Core.php';
require_once '../app/libraries/Controller.php';
require_once '../app/libraries/Database.php';
```

We can then use this conbination of libraries to referance all 3 php files, but we only need to use `require bootstrap.php`.

## Getting a url 
Often in php, we need to grab data from the url, most likey queries, which are denoted by data that appears after a `?` in a url.

```php
<?php
/* Creates URL and loads core controller 
   URL Format 
   Controller / method / parameters (params)
*/


class Core {
   protected $currentController = 'pages';
   protected $currentMethod = 'index';   
   protected $params = []; // No paramaters set 

   // Create a constructor - this allows for the class to be run straight away when a use lands on the page 
   public function __construct(){
      $this->getUrl(); // acceses getURL function from within the class
   }

   // function to get the URL of the page
   public function getUrl(){
      echo $_GET['url']; //global var _GET returns the url
   }
}
?>
```

We can also update the public function `getUrl()` so that it can seperate out diffrent file locations: 

```php
class Core {
   protected $currentController = 'pages';
   protected $currentMethod = 'index';   
   protected $params = []; // No paramaters set 

   // Create a constructor - this allows for the class to be run straight away when a use lands on the page 
   public function __construct(){
      print_r($this->getUrl()); // acceses getURL function from within the class and print array infomation 
   }

   // function to get the URL of the page
   public function getUrl(){
      echo $_GET['url'];                               // global var _GET returns the url
      if (isset($_GET['url'])){                        // if $_GET is "url"
         $url = rtrim($_GET['url'], '/');             // strips whitespce and "/" from the url
         $url = filter_var($url, FILTER_SANITIZE_URL); // Filters our special characters 
         $url = explode('/', $url);                    // splits each word seperated by a "/" into a string, stored in a array 
         return $url;               
      }
   }
}
```

