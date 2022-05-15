<!DOCTYPE html>
<html lang="en">
<?php
   include 'includes/header.php';

   ob_start();
?>
<body>
<?php if($connection) echo "connection";?>

    <div id="wrapper">

        <!-- Navigation -->
        <?php
            include 'includes/navigation.php';
        ?>
    <div id="page-wrapper">
        <div class="container-fluid">

            <!-- Page Heading -->
            <div class="row">
               <div class="col-lg-12">
                  <h1 class="page-header">
                     Admin Page
                     <small>Author</small>
                  </h1>

                  <div class="col-xs-6">

                  <!-- ADDING CATAGORIES -->
                  <?php
                     create_catagories(); 
                  ?>  
                  <!-- Add Catagory Form -->
                  <form action="" method="post">
                     <div class="form-group">
                        <input type="text" name="cat_title">
                     </div>
                     <div class="form-group">
                        <input  class="btn btn-primary" type="submit" name="submit" value="Add Catagory">
                     </div>
                  </div>


                  <!-- UPDATING EXISTING CATAGORIES -->
                  <form action="" method="post">
                     <div class="form-group">
                        <!-- Display Current Catagory name in the textbox -->
                        <input type="text" name="updated_cat_title" value=" <?php view_update_catagories(); ?> ">
                     </div>
                     <div class="form-group">
                        <input  class="btn btn-primary" type="submit" name="update_catagory" value="Update Catagory">
                     </div>
                  </div>
                  <!-- update catagories function -->
                  <?php
                     update_catagories();
                  ?>
                  

                  <!-- VEIWING EXISTING CATAGORIES (IN A TABLE) -->
                  <div class="col-xs-6">
                     <table class="table table-bordered table-hover">
                        <thread>
                           <tr>
                              <th>Id</th>
                              <th>Catagory Title</th>
                           </tr>
                        </thread>
                        <tbody>
                           <tr>
                           <!-- Generating update and delete options -->
                           <?php
                              // view exising catagories function
                              read_catagories();

                              // delete existing catagories functions
                              delete_catagories();
                           ?>

                           </tr>
                        </tbody>
                     </table>
                  </div>



                  
               </div>
         </div>
         <!-- /.row -->

        </div>
        <!-- /.container-fluid -->

    </div>
    <!-- /#page-wrapper -->

    </div>
    <!-- /#wrapper -->

    <?php 
        include 'includes/footer.php';
    ?>

</body>

</html>
