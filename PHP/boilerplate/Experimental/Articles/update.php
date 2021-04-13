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
         updateRow();
      ?>


      <div class = form>
         <form method=post action=update.php>
         Article: 
         <select name="id" id="id">
            <!-- <option value="id" selected="selected">Select User</option> -->
            <?php
               showId();
            ?>
         </select>
         <input type="submit" name="submit_id" value="view">
      </div>

      <br>
      <div class="form">
         <?php
            $idData = showIdData(); // import id data into variable $idData (this is an array)
            print_r($idData);
            echo $idData[0]['id'] . "</br>";
            echo $idData[0]['author'] . "</br>";
            echo $idData[0]['title'] . "</br>";
            echo $idData[0]['content'] . "</br>";
            echo "<br>";
         ?>
         <form method="post" action="update.php">
         Title:<br>
         <input type="text" name="title" value=<?php echo $idData[0]['title'] ?> >
         <br>
         Author:<br>
         <input type="text" name="author" value=<?php echo $idData[0]['author']?>>
         <br>
         Content:<br>
         <textarea type="text" name="content" rows="1" cols="35" value=<?php echo $idData[0]['content']?>>
         </textarea>
         
         <br>
         <br><br>
         <input type="submit" name="save" value="submit">
      </div>
      
   </div>  
</body>

</html>
