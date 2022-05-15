<!DOCTYPE html>
<html lang="en">
<?php
include 'includes/header.php';
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
                        Blank Page
                        <small>Subheading</small>
                    </h1>
                    <ol class="breadcrumb">
                        <li>
                            <i class="fa fa-dashboard"></i>  <a href="index.html">Dashboard</a>
                        </li>
                        <li class="active">
                            <i class="fa fa-file"></i> Blank Page
                        </li>
                    </ol>
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
