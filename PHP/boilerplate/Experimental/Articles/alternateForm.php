<?php 
    include "../includes/header.php";
?>

<body>
   <?php include "../includes/navigation.php" ?>

   <body>
      <div class="content">

      <h1>CRUD Test Site </h1>
      <h2>Read Data</h2>

      <table style="width:50%">
         <tr>
            <th>ID</th>
            <th>Title</th>
            <th>Author</th>
            <th>Content</th>
            <th>Date Created</th>
         </tr>
      <?php
         include "config.php"; // Connect to database script
         include "functions.php";

         // takes data from a database and displays certian rows based on the 'id' selected
         global $connection; // alllows $connection to be used across config.php and functions.php
         $query = "SELECT * FROM articles";

         $result = mysqli_query($connection, $query);// sends sql query to database 

         if(!$result){
            die("query failed" . mysqli_error($connection));    // If the result fails, stop it (die) and send a error message 
         }

         while($row = mysqli_fetch_assoc($result)){   // $row = fetch assosiative array of $result = query of 'SELECT * FROM users"
                                                      // the array is a row of data - this is looped until the database returns no more rows 
            $id = $row['id'];                         // creates a variable called 'id' that finds data from array with the referance name 'id' (assosative array)
            $title = $row['title'];  
            $author = $row['author'];
            $content = $row['content'];
            $date_created = $row['date_created'];
            
            echo "<tr>";
            echo "<td>" . $id . "</td>";
            echo "<td>" . $title . "</td>";
            echo "<td>" . $author . "</td>";
            echo "<td>" . $content . "</td>";
            echo "<td>" . $date_created . "</td>";
            echo "<td>" . "<a href='alternateUpdate.php?id=" . $id . "'>Update</a>  </td>";
            echo "<td>" . "<a href='alternateDelete/" . $id . ".php'>Delete</a> </td>";
            echo "</tr>";
         }
      ?>
      

         
      </table>
   </div>  
</body>

</html>
