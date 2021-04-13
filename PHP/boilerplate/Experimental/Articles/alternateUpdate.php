<?php 
    include "../includes/header.php";
?>

<body>
   <?php include "../includes/navigation.php" ?>

   <body>
      <div class="content">

      <h1>CRUD Test Site </h1>
      <h2>Update Data</h2>

      <?php
         include "config.php"; // Connect to database script
         include "functions.php";
         echo $_GET['id']
      ?>

      <br>

      <div class="form">
         <?php
            global $connection;    // alllows $connection to be used across config.php and functions.php
            if(isset($_GET['id'])) // if the url has "update.php?id=<a number> 
            {
               $id = $_GET['id']; 
               $query = "SELECT * FROM articles WHERE id = $id"; // using the url id to select the correct row of data
            
               $result = mysqli_query($connection, $query);// sends sql query to database and returns the data under an ARRAY called $result 
         
               while($row = mysqli_fetch_assoc($result)){   // $row = fetch assosiative array of $result = query of 'SELECT * FROM users"
                                                            // the array is a row of data - this is looped until the database returns no more rows 
                  echo $row['id'];   
                  echo $row['title'];
                  echo $row['author'];
                  echo $row['content'];
                  echo $row['date_created'];


                  $title = $row['title'];
               }  
            }
         ?>



         <form method="post" action="update.php">
         Title:<br>
         <input type="text" name="title" value=<?php echo $title ?> >
         <br>
         Author:<br>
         <input type="text" name="author" value=<?php echo $row['author'];?>>
         <br>
         Content:<br>
         <textarea type="text" name="content" rows="1" cols="35" value=<?php echo $row['content'];?>>
         </textarea>
         
         <br>
         <br><br>
         <input type="submit" name="save" value="submit">
      </div>
      
   </div>  
</body>

</html>
