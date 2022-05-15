<html>
   <body>

   Welcome <?php echo $_POST["number1"]; ?><br>
   <?php 
      $number1 = $_GET["number1"];
      $number2 = $_POST["number2"];
   
      echo $number1;
      echo $number2;
   ?>


   <a href="/phpExamples/php_examples.php">Go back</a>
   </body>
</html> 