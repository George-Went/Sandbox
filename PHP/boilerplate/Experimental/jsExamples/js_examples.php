
<?php 
    include "../includes/header.php";
?>

<body>
   <?php include "../includes/navigation.php" ?>

   <div class="content">

      <div class="card">
         <!-- <img src="img_avatar.png" alt="Avatar" style="width:100%"> -->

         <div class="container">
            <h3>Card I</h3>
            <h4><b>John Doe</b></h4>
            <p>Architect & Engineer</p>
         </div>
      </div>

      <div class="card">
         <!-- <img src="img_avatar.png" alt="Avatar" style="width:100%"> -->
         <h3>Display Time</h3>
         <button type="button" class="button" onclick="getTime()">
            Click me to display Date and Time.
         </button>
         <p id="timeDemo">test</p>
      </div>



      <div class="card">
         <h3>Getting HTML Content</h3>
         <div id="example" class="example">
            <p>Hello</p>
         </div>
         <button type="button" class="button" onclick="getHTMLelements()">get elements
         </button>
         <div id="answer"></div>
      </div>

      <!-- <div class="card">
               <h3>Forms</h3>
               <form action=>
                  First Number:<br>
                  <input type="text" id="no1"><br>
                  Seconds Number:<br>
                  <input type="text" id="no2">
                  <input type="submit" value="Add">
               </form> 
               <h3 id=addAnswer>Answer: </h3>
            </div>   -->

      <div class="card">
         <h3>JS Forms</h3>

         First Number:<br>
         <input type="text" id="no1"><br>
         Seconds Number:<br>
         <input type="text" id="no2">
         <button class="button" id="calculate" onclick="addNumbers()">Add</button>

         <h3 id=addAnswer>Answer: </h3>
      </div>
   </div>
</body>

</html>



<!-- Below are the js scripts for each of the above cards -->

<script>
   /* Toggle between adding and removing the "responsive" class to topnav when the user clicks on the icon */
   function navbarFunction() {
      var x = document.getElementById("myTopnav");
      if (x.className === "topnav") {
         x.className += " responsive";
      } else {
         x.className = "topnav";
      }
   }

</script>
<script>
   function getTime() {
      document.getElementById("timeDemo").innerHTML = Date();
   }

</script>
<script>
   function getHTMLelements() {
      var get_id = document.getElementById("example");
      var get_tag = get_id.getElementsByTagName("p");
      var get_class = document.getElementsByClassName("example");
      var get_css = document.querySelectorAll(".example");

      all = "ID: " + get_id.innerHTML +
         " Tag: " + get_tag[0].innerHTML +
         " Class: " + get_class[0].innerHTML +
         " CSS: " + get_css[0].innerHTML;

      //gets the first paragraph in the document

      document.getElementById("answer").innerHTML = all;
   }

</script>
<script>
   function addNumbers() {
      var no1, no2;
      var no1 = Number(document.getElementById("no1").value);
      var no2 = Number(document.getElementById("no2").value);
      var answer = no1 + no2;

      console.log(no1 + "  " + no2);
      console.log(answer);

      document.getElementById("addAnswer").innerHTML = answer;
   }

</script>