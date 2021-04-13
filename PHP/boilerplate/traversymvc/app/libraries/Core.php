<?php
// /* Creates URL and loads core controller 
//    URL Format 
//    Controller / method / parameters (params)
//    The aim of this class is to allow different URL's to direct uses to different controlllers 
// */


// class Core {
//    protected $currentController = 'Pages';
//    protected $currentMethod = 'index';   
//    protected $params = []; // No paramaters set 

//    // Create a constructor - this allows for the class to be run straight away when a use lands on the page 
//    public function __construct(){
//       print_r($this->getUrl()); // acceses getURL function from within the class and print array infomation 
      
//       $url = $this->getUrl();  // Assing the url to a variable

//       // Look in controllers for first value 
//       if(file_exists('../app/controllers/' . ucwords($url[0]) . '.php')){ // if the first url var in the array exists in controllers folder
//          $this->currentController = ucwords($url[0]);                    // capitilsie the first letter in the url[0] variable
//          unset($url[0]);                                                 // remove empty spaces from $url
//       }

//       // Require controller based on word in the url
//       echo '../app/controllers/'. $this->currentController . '.php';
//       require_once '../app/controllers/'. $this->currentController . '.php';
      
//       //Instantite controller class
//       $this->currentController = new $this->currentController;

//       //Overall,what this class does is that it works out 
      
//    }

//    // function to get the URL that the user has 
//    public function getUrl(){
//      // echo $_GET['url'];                               // global var _GET returns the url
//       if (isset($_GET['url'])){                        // if $_GET is "url"
//          $url = rtrim($_GET['url'], '/');             // strips whitespce and "/" from the url
//          $url = filter_var($url, FILTER_SANITIZE_URL); // Filters our special characters 
//          $url = explode('/', $url);                    // splits each word seperated by a "/" into a string, stored in a array 
//          return $url;               
//       }
//    }
// }
?>





<?php
  /*
   * App Core Class
   * Creates URL & loads core controller
   * URL FORMAT - /controller/method/params
   */
  class Core {
    protected $currentController = 'Pages';
    protected $currentMethod = 'index';
    protected $params = [];

    public function __construct(){
      //print_r($this->getUrl());

      $url = $this->getUrl();

      // Look in controllers for first value
      if(isset($url[0]) && file_exists('../app/controllers/' . ucwords($url[0]). '.php')){
        // If exists, set as controller
        $this->currentController = ucwords($url[0]);
        // Unset 0 Index
        unset($url[0]);
      }

      // Require the controller

      echo '../app/controllers/'. $this->currentController . '.php';
      require_once '../app/controllers/'. $this->currentController . '.php';

      // Instantiate controller class

      $controllerpath = '../app/controllers/'. $this->currentController . '.php';
      echo $controllerpath;
      $controllername = 'Pages';
      require $controllerpath;
      $this->currentController = new Pages;
     

    }

    public function getUrl(){
      if(isset($_GET['url'])){
        $url = rtrim($_GET['url'], '/');
        $url = filter_var($url, FILTER_SANITIZE_URL);
        $url = explode('/', $url);
        return $url;
      }
    }
  } 
  
  