<?php 
    include "../includes/header.php";
?>

<body>
   <?php include "../includes/navigation.php" ?>

   <div class="content">

      <h1>Example PHP Code</h1>

      <!-- Hello world PHP -->
      <h2>hello world script</h2>
      <?php
         // Simple greeting message
         echo "Hello, world!";
      ?>

      <h2>Embedded PHP</h2>
      <h1><?php echo "Hello, world!"; ?></h1>


      <!-- Variables -->
      <h2>PHP variables</h2>
      <?php
         $txt = "Hello World!";
         $number = 10;

         // Display variables value
         echo $txt;
         echo "<br>";
         echo $number;
      ?>

      <!-- PHP If statments -->
      <h2>If Statements</h2>
      <?php
         $d = date("D");
         if($d == "Fri"){
            echo "Have a nice weekend!";
         }
         else{
            echo "Its still the Week (Its " . $d . ")";
         }
      ?>
      <input type="button" value="Click me" onclick="msg()"> 


      <!-- Forms -->
      <h2> Forms </h2>
      <form action="script.php" method="get">
         Name: <input type="text" name="name">
         <input type="submit"> 
      </form>
     
      <!-- Add numbers together -->
      <h2> Forms </h2>
      <form action="add.php" method="post">
         Number 1: <input type="text" name="number1">
         Number 2: <input type="text" name="number2">
         <input type="submit"> 
      </form>

      <!-- Sending Data (back to the same page) -->
      <!-- GET -->
      <h2> POST </h2>
      <form action="php_examples.php" method="post">
         Name: <input type="text" name="name">
         <input type="submit" name="post"> 
      </form>
      <?php 
      function GetExample()
      {
            if(isset($_GET['name']))
            {
               $name = $_GET['name'];
               echo "Hello " . $name;
            }
         }
      ?> 
      

      <?php
      function PostExample(){
         if(isset($_POST['post']))
         {
            $name = $_POST['name'];
            echo "Hello " . $name;
         }
      }
      ?>


      <!-- POST -->
      <h2> POST </h2>
      <form action="php_examples.php" method="post">
         Name: <input type="text" name="name">
         <input type="submit" name="post"> 
      </form>
      <?php PostExample()?> 
      

      <?php
      function PostExample(){
         if(isset($_POST['post']))
         {
            $name = $_POST['name'];
            echo "Hello " . $name;
         }
      }
      ?>




   </div>
</body>

</html>

