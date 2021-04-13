<?php



// DISPLAYING EXISTING CATAGORIES
function read_catagories(){

    // This allows us to us the $connection variable (instansiated at CMS/includes/db.php) 
    // anywhere within the function
   global $connection;

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
}




// INSERTING (CREATING) CATAGORIES
function create_catagories() {
   global $connection;

   if(isset($_POST['submit'])){
      $cat_title = $_POST['cat_title'];
      if($cat_title == "" || empty($cat_title)){
         echo "This field should not be empty";
      } else {
         $query = "INSERT INTO catagories(cat_title)";
         $query .= "VALUE('{$cat_title}')";

         $create_catagory_query = mysqli_query($connection, $query);
         
         if(!$create_catagory_query){
            echo $query;
            die('QUERY FAILED' . mysqli_error($connection));
         }
      }
   }
}






// DELETING CATAGORIES 
function delete_catagories() {
   global $connection;

   if(isset($_GET['delete'])){ 
      $cat_id = $_GET['delete'];
      $query = "DELETE FROM catagories WHERE cat_id = {$cat_id}";
      $delete_query = mysqli_query($connection, $query);
   }
}





// DISPLAYING CATAGORIES TO UPDATE
function view_update_catagories(){
   global $connection;

   // if the update variable has been set (url with ?update=cat_id at the end)
   if(isset($_GET['update'])){ 
   
      //get the variable from the generated url
      $cat_id = $_GET['update']; 
      // echo "yes: " . $cat_id;

      // create query to find the catagory with the correct id
      $query = "SELECT * FROM catagories WHERE cat_id = $cat_id";
      
      // send query to run in mysql database - returning data is put into varaible
      $select_catagories_id = mysqli_query($connection,$query);

      // Go through array and assing varaible names to array data
      while($row = mysqli_fetch_assoc($select_catagories_id)){
         $cat_id = $row['cat_id']; 
         $cat_title = $row['cat_title'];
         echo $cat_title;
      }
   }
}


// UPDATING CATAGORIES
function update_catagories() {
   global $connection;

   // if a user select 'Update Catagory'
   if(isset($_POST['update_catagory'])){

      // cat_title is set to the new value
      $cat_title = $_POST['updated_cat_title'];

      // is field empty 
      if($cat_title == "" || empty($cat_title)){
         echo "This field should not be empty";
      } 
      else {
         // update catagory title with new one (cat id is still set from the 'display catagories' script)
         $query = "UPDATE catagories SET cat_title = '{$cat_title}' WHERE cat_id = ${cat_id}";

         $update_catagory_query = mysqli_query($connection, $query);
         echo $query;
         // if the query fails
         if(!$update_catagory_query){
            die('QUERY FAILED' . mysqli_error($connection));
         }
      }
   }
}



?>