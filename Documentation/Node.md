

# Node 
Node is a server-side platform build on javascript (specifically googles javascript V8 engine). 

Node is designed to build fast and scalable applications that run in real time. Node also works with a variety of pre-existing and node specific libraries. 

> Node.js = Runtime environment (engine) + javascript libraries 

**Note:** 
Javascript was designed as an event driven language for mosaic back in 1996 (and became the default standard because -reasons- ). However most web servers still require back end engines which in most cases means people default to using either apache or ngix to run a loop that detects events on the web site. 


## Features of Node.js

**Asynchronous and Event Driven** − All APIs of Node.js library are asynchronous, that is, non-blocking. It essentially means a Node.js based server never waits for an API to return data. The server moves to the next API after calling it and a notification mechanism of Events of Node.js helps the server to get a response from the previous API call.

**Very Fast** − Being built on Google Chrome's V8 JavaScript Engine, Node.js library is very fast in code execution.

**Single Threaded but Highly Scalable** − Node.js uses a single threaded model with event looping. Event mechanism helps the server to respond in a non-blocking way and makes the server highly scalable as opposed to traditional servers which create limited threads to handle requests. Node.js uses a single threaded program and the same program can provide service to a much larger number of requests than traditional servers like Apache HTTP Server.

**No Buffering** − Node.js applications never buffer any data. These applications simply output the data in chunks.

Areas where Node.js is proving itself as a perfect technology partner: 

* I/O bound Applications
* Data Streaming Applications
* Data Intensive Real-time Applications (DIRT)
* JSON APIs based Applications
* Single Page Applications

> As NodeJS is single threaded, it is inadvisable to use the language for CPU intensive applications 

## Installing Node

### On windows
You can download node installation files from http://nodejs.org/download/ and follow the process to install node onto a windows systems

### On Linux
While you can install node manually from node servers, most package managers will have the latest version of node on them
```
curl -sL https://deb.nodesource.com/setup_10.x | sudo -E bash - 
sudo apt-get install -y nodejs
```

You can check that node and npm are working by looking at their version numbers
```
Node -v
Npm -v
```

## Setting up a node application 
First, create the directory that the project will use
```
mkdir application
```
Node applications run on javascript files, so save work as a ```.js``` file




## Node Package Manager (NPM)

NPM is the package manager for Node, in the same way that apt and yum are package managers for linux distributions (ubuntu and rhel respectively) 


###  Using node package manager (npm) 
Navigate to the directory which the project is located in
```
npm init 
```

This creates a ```package.json``` with the applications name, launch point (usually ```index.js``` or ```app.js```), dev scripts and also the developer dependencies. 

### Installing dependencies (add ons)
While creating and using web pages using the pre-existing http api’s in the node language, generally it is much easier to use a framework which does the views and routing protocols for you. For nodes case, the most common web framework used is express.

```
npm install --save <dependancy>
```

>**note**  
The addition of ```--save``` will add whatever we intall as a dependancy in our ```package.json``` file.

when a dependancy is installed it is added to the ```packages.json``` file under ```dependancies```







### Hello World 
The most basic Node program, this just prints out ```Hello World``` to the console.
  
First we can create our main file ```app.js```, this will be used in this project and future projects as the start point of applications - the 'launch pad' if you will. 

```app.js```
```javascript
console.log('Hello World');
```




## Running the Program 
### Executing the script manually
The most basic way to run a node program is to execute the script manually
```
node <script name>
```
For the above ```app.js``` file, we can run ```node app.js``` to run the script.

Usually however this is not standard operating procedure when running a node application.  
In our ```package.json``` file, we can see that there are scritps that we can execute: 

```json
  "scripts": {
    "test": "echo \"Error: no test specified\" && exit 1",
  },
```

We can add our own scripts, which can start the node application

```json
  "scripts": {
    "test": "echo \"Error: no test specified\" && exit 1",
    "start": "node app",
  },
```
We can then run ```npm start``` whcih will run the start script - which itself will run ```node app```.



### Writing a Web application using just Node 
This is a very basic application that demonstrates how node can be used to host web servers and can function as an alternative to using apache or nginx - this application does not use any addons and only uses the libraries that come with node originally. 

```javascript
// Load HTTP module
const http = require("http"); 
// (You can either use constant or variable to denote the modules)

const hostname = "127.0.0.1";
const port = 3000;

// Create HTTP server 
const server = http.createServer((req, res) => {

   // Set the response HTTP header with HTTP status and Content type
   res.writeHead(200, {'Content-Type': 'text/plain'});
   
   // Send the response body "Hello World"
   res.end('Hello World\n');
});

// Prints a log once the server starts listening
server.listen(port, hostname, () => {
   console.log(`Server running at http://${hostname}:${port}/`);
})
```






# Express 

### Hello World 
Express is designed as a web application framework that provides a simple API that allows web server code to go from looking like this:

```javascript
// Load HTTP module
const http = require("http"); 
// (You can either use constant or variable to denote the modules)

const hostname = "127.0.0.1";
const port = 3000;

// Create HTTP server 
const server = http.createServer((req, res) => {

   // Set the response HTTP header with HTTP status and Content type
   res.writeHead(200, {'Content-Type': 'text/plain'});
   
   // Send the response body "Hello World"
   res.end('Hello World\n');
});

// Prints a log once the server starts listening
server.listen(port, hostname, () => {
   console.log(`Server running at http://${hostname}:${port}/`);
})
```
To this:

```javascript
var express = require('express'); // Import Express linbraries
var app = express(); // Declare express as "app" (app.method)

app.get('/', function(req, res){ //GET request for express 
   res.send("Hello world!"); // When a GET request is recived, send text
});

app.listen(3000); // server listens on port 3000
```



# Express - Setting up a simple Server 
To get started with expess, we can set up a simple server that hosts a web page displaying the text "Hello world"

```app.js```
```javascript
var express = require('express'); //app.js requires Express

//Initilise app 
var app = express();

// Home Route 
app.get('/', function(req, res){
  res.send('Hello World');
});
//When a GET function is recived, the application will send the response (in this case "Hello world")


//This will detect any port 3000 traffic and respond with the function defined (in this case, the console prints out the string)
app.listen(3000, function(){
  console.log('server started on port 3000')
});

```

# Templating Engines

One of the main issues with node is that writing HTML and CSS code directly into a javascript ```.get``` function is that it can be hard to tell when the js ends and the HTML begins. 

Templating engines are used to remove HTML code clutter when generating or auto-generating pages, if you have a HTML page that has a generated dev based on the result of a .js file var, congratulations thats technically a templating engine. 

In short, a templating engine can turn this:


```javascript
app.get('/', function(req, res){ //GET request for express 
   res.send("<html><head> <title>Index</title></head><body><h1>Hello World!</h1></body></html>"); // When a GET request is recived, send text
});
```
into this

```index.pug```
```pug
doctype html
html
   head 
      title Index
   body 
      h1 Hello world!
```

> **Note:** Pug was formally known as Jade, some tutorials online still refer to it as such.

**Installing Pug** 
Pug can be installed using the node package manager 
```
npm install --save pug 
```


## Utilising View Engines

### Setting up a views directory 
While we can save our pug code into the root directory of the program at the same level as app.js. This could create problems if we wanted to create a larger program with multiple views, our file structure would be incredebly messy.  
To solve this we can create a ```/views``` directory to store our pug files.

We can use the npm module ```path``` to then allow our app to know where the pug files are. 

```javascript
var path = require('path'); 
```

### Setting the Templating Engine  
To use a templating engine, two functions are needed. 
One to set nodes view engine to the correct templating package
One to show the templating engine where our templates are stored. 


**Adding a template engine**   

```javascript
app.set('view engine', 'pug'); //Sets template engine to pug
app.set('views', path.join(__dirname, 'views'));  //shows template engine where templates are
```

> **Note:**  
>```app.set('views', path.join(__dirname, 'views'))```   
is the same as typing in the directory for views manually i.e.  
  ```app.set('views', '/views')```

The above code allows for pug to use templates that are stored in ```/views```


## Pug Files
Pug uses indentation instead of brackets as a way to organise HTML.
You can either use spaces or tabs, but make sure to be consistant in yoiur usage of either - you cant use both in the same file.

```html
<!DOCTYPE html>
<html>
   <head>
      <title>Library</title>
   </head>
   <body>
      <h1>Books</h1>
   </body>
</html>
```
In pug would be:

```pug
doctype html
html
   head
      title Library
   body
      h1 Books
```

You can also use variables in pug to allow for templated files, for example:

```javascript
// Home Route
app.get('/', function(req, res){
  res.render('index', {
    title: 'Hello' // variable set - titles value is "Hello"
  });
});
```
Your ```views.pug``` file can look like:

```pug
doctype html
html
   head
      title Library
   body
      h1 Books
      h2 #{title}
```

We can also use the code in this pug file to create a completly new route in ```app.js```: 

```javascript
// Add Route
app.get('/book/add', function(req, res){
  res.render('add_book', {
    title:'Add Book'
  })
});
```
add a new pug file called ```add_book.pug```
>**Note**  
Make sure the file name is the same as the name that is called in the ```res.render()``` route - if the files are not called the same value, the server will "fail to lookup view ```filename```"
```pug
doctype html
html
   head
      title Library
   body
      h1 Books
      h2 #{title}
```

### Layouts
One of the main things you may have noticed if you set up two routes with pug files attached is that they have a lot of the same code in the pug file. One of the ways we can organise our designs is through the usage of **layouts**.

We can create a file called ```layout.pug``` to put some of the basic html/pug code that is used in all of our pages.

```layout.pug```
```pug
doctype html
html
   head
      title Library
   body
      block content
      br
      hr
      footer
         p Footer 
```

To use this view file in other .pug files, we can use ```extends.layout```  
The ```block content``` within the layout pug code is an imporant part, as its where we can specify other views to import their code In the ```index.pug``` file we created earlier, we can remove all of the html code except for our titles so that it looks like this:  
```
extends layout

block content
   h2 #{title}
```

### Displaying Variable Data
We can also add control structures such as **if statments** and **loops**. 

While most data from websites come from databases, for the moment, we can replicate this data by just having a static array of data in a route.

```javascript
// Book List Route
app.get('/books', function(req, res){
  let books = [ // We create an array called "books"
    {
      id: 1,
      title: "Book 1",
      author: "Gwent went",
      body: "Star Platinum"
    },
    {
      id: 2,
      title: "Book 2",
      author: "Gwent went",
      body: "Joe mama"
    },
    {
      id: 3,
      title: "Book 3",
      author: "joestar",
      body: "AYAYAYAYA"
    },
  ]
  //Respons with a render of the infomation
  res.render('books', {
    title: 'List of Books',
    books: books // "books" value is the "books" array
  });
});
```

We can use this array as a set of example data that we can display using a pug file:  

```pug
extends layout

block content
   h1 #{title}              
   ul
      each book, i in books 
         li= book.title     
```
The above pug file ```books.pug```   works as such:  
- The ```layout.pug``` file is included, allowing for a header and a footer.    
- The ```block content``` is used, meaning that any indented code within the tag is impoted into the ```layout.pug``` ```content``` block.  
- The Header title is parsed from the response ```render(title: List of Books)```  
- the ```ul`` tag defines an unordered list - meaning instead of numbers, bullet points are used.  
- The each (for) loop means that for each ```book``` in the array ```books```, the page will render the ```book.title``` in a **list** (```li```)  
- The array is parsed into the ```books.pug``` file using ```render(books.books)```, this means that the variable books will render the unorderd list in the ```books.pug``` file.  















































# Basic Express Skeleton Setup 

## Setting up the Environment 
### Node Package Manager (npm)

NPM is the package manager for Node, in the same way that apt and yum are package managers for linux distributions (ubuntu and rhel respectively) 


###  Using node package manager (npm) 
Start by creating the project directory for the application and navigating into it
```
mkdir <application name>
cd <application name> 
```
**Initilising the project**

When a project is created or deployed, a ```package.json``` file has all the details about the project, allowing systems to easily set up and install the required depenadncies for the project, instead of a user having to manually install all of the npm libraries themsleves.

Navigate to the directory which the project is located in
```
npm init 
```
This creates the ```package.json``` with the applications name, launch point (usually index.js or app.js), dev scripts and also the developer dependencies (npm libraries which are only used by the developer)

**Installing packages** 

npm packages can be installed in one of two ways 
* **Globally** - This installs a package onto a system so that it can be used by **any** node project, regardless of whether or not a specific project has it as one of its dependancies, it is normally used for development packages so that they dont have to be installed on every node project  

```
npm install -g <package name>
```

* **Locally** - This installs the package so that it can only be used by the current project, notice that it also adds the dependancy to the ```package.json```, meaning that any other systems that want to run the program know what the necessary dependancies are.

```
npm install <package name>
```

**Enabeling server restart on file changes** 

Any changes made to an express file will not be reflected unless the program is restarted, one of the easiest tools to automate this when file changes are made is ```nodemon``` (it also serves as a nice intro to dev depandencies). Nodemon runs a demon in the background of the program that restarts the service when it detects file changes on the machine hosting the program 

Installing nodemon 
```
npm install --save-dev nodemon
``` 

**Adding scripts to the server** 

normaly to start the service, a user has to specify the file that they want node to run i.e ```node ./bin/www```. With scripts we can simplify this to ```npm start`` when in the directory that the program is stored in. 

Find the scripts section of the ```package.json```. Initially it will only contain the ```"start"``` command, we can update this so that devs can start with the nodemon using ```npm devstart```.

Updating the ```package.json```
```
"scripts": {
    "start": "node ./bin/www",
    "devstart": "nodemon ./bin/www"
  },
```
we can now start the program using nodemon by using:
```
npm run devstart
``` 


# File Structure
The basic file structure of the project is similar to a normal website directory structure, with routing and view templates in seperate directories.

```
/application directory
    app.js
    /bin
        www
    package.json
    package-lock.json
    /node_modules
        [about 6700 subdirectories and files]
    /public
        /images
        /javascripts
        /stylesheets
            style.css
    /routes
        index.js
        users.js
    /views
        error.pug
        index.pug
        layout.pug
```

## www

This is where the program actually starts, and is the first thing a user will (technically) access when they first arrivfor at least an houre to the directory - the first and only thing it does is direct the user to the real access point of the program - the ```app.js``` file and where abouts it is located , you can see this due to the fact that in very basic skeleton application, the only lines are importing the contents of the app.js functions 

```./bin/www``` structure:
```javascript
var app = require('../app'); //imports the app.js 
```
> **Note:** ```require()``` is a global node function that is used to import modules into the current file. Here we specify app.js module using a relative path and omitting the optional (.js) file extension.

## App.js

This is the main ‘starting point’ for the application and is where most of the work happens, by convention its called app, similar to ‘main’ files in other programs. 

### Imports 
The first part of an app.js file is concerned with the node libraries and can be used to import npm packages such as express (needed for express applications suprisingly) among other node libraries such as http-errors, morgan and cookie-parser. 

```javascript
var express = require('express');
var createError = require('http-errors');
var path = require('path');
```

> **Note:** The ```require()``` function in node acts like the import function in other languages such as java or python.

After importing modules, we then need to import our own modules from our application directory, in particular our `routes` (URL paths). This can also be extended to other functions such as database controllers or induvidual functions executed by multiple pages such as permission checking systems. 

```javascript
var indexRouter = require('./routes/index');
var usersRouter = require('./routes/users');
```
> **Note:** At this point we have *imported* the modules, we havent used them or the functions within them at this point.

### Generation 
Once we have imported all of our own libraries and modules we can then generate the application.

```javascript 
var app = express(); // defines the express libraries as app
```

### Middleware 
Adding middleware such as templating and error handeling can be done by utilising the ```app.set``` function to point to a directory, and the ```app.use``` function to use a imported middleware funciton or route.  

### Routes 
Routes are important for a site (i think)

Routes are defined using REST models 
```
/* GET users listing. */
router.get('/', function(req, res, next) {
  res.send('respond with a resource');
});

/* POST users listing. */
router.get('/', function(req, res, next) {
  res.send('respond with a resource');
});
```

Here are some examples of route paths based on strings.
This route path will match requests to the root route, /.
```js
app.get('/', function (req, res) {
  res.send('root')
})
```
This route path will match requests to /about.
```js
app.get('/about', function (req, res) {
  res.send('about')
})
```
This route path will match requests to /random.text.
```js
app.get('/random.text', function (req, res) {
  res.send('random.text')
})
```
Here are some examples of route paths based on string patterns.

This route path will match acd and abcd.
```js
app.get('/ab?cd', function (req, res) {
  res.send('ab?cd')
})
```
This route path will match abcd, abbcd, abbbcd, and so on.
```js
app.get('/ab+cd', function (req, res) {
  res.send('ab+cd')
})
```
This route path will match abcd, abxcd, abRANDOMcd, ab123cd, and so on.
```js
app.get('/ab*cd', function (req, res) {
  res.send('ab*cd')
})
```
This route path will match /abe and /abcde.
```js
app.get('/ab(cd)?e', function (req, res) {
  res.send('ab(cd)?e')
})
```
Examples of route paths based on regular expressions:

This route path will match anything with an “a” in it.
```js
app.get(/a/, function (req, res) {
  res.send('/a/')
})
```
This route path will match butterfly and dragonfly, but not butterflyman, dragonflyman, and so on.
```js
app.get(/.*fly$/, function (req, res) {
  res.send('/.*fly$/')
})
```

### Error Handling 

### Exporting the final product





















# Routing 
Web frameworks provide resources such as HTML pages, scripts, images, etc. at different routes.

While you can set up routes (as well the entire site) within the app.js file (like most helloworld programs in node), it's better practice to use a specific routing directories to organise your sites structure.

In Express routing functions are defined by ```app.method(path,handler)```

The example routing files in the skeleton project above, ```index.js``` and ```example.js``` are examples of 

## Creating a basic routing file
```./routes/example.js```
```javascript
var express = require('express');  //imports express libraries 
var router = express.Router();     //defines express.router as router

/* GET users listing. */
router.get('/', function(req, res, next) {
  res.send('respond with a resource');
});

//export this router to use in our app.js
module.exports = router;
```
> The above code defines a route so that when a user visits ( ```/example``` ) **plus** the defined route in the above file ( ```/``` ). In other words this means that when a user visits ( ```/example/``` ) they will recive the above resource.  


## Changing data based on URL Parameters  
One of the most common ways applications communicate data between backend and frontend systems is by parsing data transmitted through the URL, known as URL encoding.

Another major part of sites is being able to generate route handlers automatically, such as dashboards for induvidual users.

URL parameters can be set up by putting a colon before a router. For example, having a ```router.get('/Library/:Book', function(req,res)```  means that ```:Book``` will be interpreted as data and not as a destination.

An example of how paramaters can work with both node and the pug template structure: 

```/routes/index.js```
```javascript
router.get('/:name/:address', function(req,res) {
   var name = req.params.name;
   var address = req.params.address;
   res.render('index', {title: name, address: address} 
```







# Controllers 

Controllers are part of the MVC ```Model, View, Controller``` methodology and are used to control the backend interactions on the website such as displaying data and matching variables to display elements in views.  


## Creating a basic controller file
An example of a basic controller that just sends a string when a user reqests the route ```hello```. 

```js
// Display Genre create form on GET.
exports.hello = function(req, res) {
    res.send('Hello There!');
};

```

An example of a more complex route that contains middleware functions - as denoted by the ```next``` after the request and the response. The middleware function in this case links to a model called ```Genre``` that then allows us to display genre data from our mongoDB database.  

```js
var Genre = require('../models/genre');

// Display list of all Genre.
exports.genre_list = function(req, res, next) {
    Genre.find()
      .sort([['name', 'ascending']])
      .exec(function (err, list_genres) {

        if (err) { return next(err); }
        //Successful, so render
        res.render('genre_list', { title: 'Genre List', genre_list: list_genres });
      });
};
```









## Controllers and asynchronous requests

Most of the methods used within express are asynchronus by design:  
- specify an operation to peform (```Please add these two variables```)  

- specify a callback (```I will say "done" when i have added the two numbers```)  

- method is called and run (```The answer to 1 + 1 is 2```)
- callback is invoked when requested operation is complete (```operation [add two numbers] is "done"```)

When a controller only needs to take one this works fine, however what if a user wants to take multiple requests - such as collecting multiple sets of data from a database or also dispalying images at the same time.  

You could daisy chain the operators together so that function 1 calls function 2 and when function 2 is complete function 1 runs - with multiple requests this can become very messy an leads to complex nested code, known as ```callback hell```.

>**Note:** Traditionally, code is executed in a linier fashion with one function/method taking place after the other (this is completly oversimplifying it). Due to the high level nature of node if we too this at its word, we would have massive daisy chains of code so that a database + a client and a server (and all the exception checks) - making it unreadable (for me at least)


In order to manage our control flow more effectivly, we can use a popular npm module called ```async``` 

### Async 
There are 3 main methods used by async: 

```async.parallel()```: to execute operations that are peformed in parallel.

```async.series()```: for when operations need to be peformed in series.

```async.waterfall```: for operations that must be run in series, with each operation depending on the results of a previous operation. 








# Templating
One of the main issues with node is that writing HTML and CSS code directly into a javascript ```.get``` function is that it can be hard to tell when the js ends and the HTML begins. 

Templating engines are used to remove HTML code clutter when generating or auto-generating pages, if you have a HTML page that has a generated dev based on the result of a .js file var, congratulations thats technically a templating engine. 

In short, a templating engine can turn this:


```javascript
app.get('/', function(req, res){ //GET request for express 
   res.send("<html><head> <title>Index</title></head><body><h1>Hello World!</h1></body></html>"); // When a GET request is recived, send text
});
```
into this

```index.pug```
```pug
doctype html
html
   head 
      title Index
   body 
      h1 Hello world!
```

One of the most commonly used templating languages is Pug, formally known as Jade. 

> **Note:** Pug was formally known as Jade, some tutorials online still refer to it as such.

**Installing Pug** 
Pug can be installed using the node package manager 
```
npm install --save pug 
```

**Setting the templating engine**
To use a templating engine, two functions are needed. One to set nodes view engine to the correct templating package, and one to show the templating engine where our templates are stored. 

**Adding a template engine** ```app.js```
```javascript
app.set('view engine', 'pug'); //Sets template engine to pug
app.set('views', path.join(__dirname, 'views'));  //shows template engine where templates are
```

> **Note:** 
>```app.set('views', path.join(__dirname, 'views'))``` is the same as typing in the directory for views manually i.e. ```app.set('views', '/views')```

The above code allows for pug to use templates that are stored in ```/views```

As well as specifying the template engine, you also have to make sure that the express "```.app```" can find and then use public files, such as images, javascript and most importantly for our templates, css stylesheets. This can be solved by allowing the app to use files that are stored under ```/public```, in a similar fashion to allowing the app to access third party middleware. 

```javascript

app.use(express.static(path.join(__dirname, './public')));

```
> Note - This code needs to be placed after added routes, otherwise the new files cant access ```/public```
```

```views/index.pug```
```pug 
extends layout

block content
  h1= titleGB

  p Welcome to #{name}
  p Adress: #{address}
```

## Basic Templating Primer    
This was copied from mozilla's template primer: [Template Primer](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Express_Nodejs/Displaying_data/Template_primer)

```html
doctype html
html(lang="en")
  head
    title= title
    script(type='text/javascript').
  body
    h1= title

    p This is a line with #[em some emphasis] and #[strong strong text] markup.
    p This line has un-escaped data: !{'<em> is emphasised</em>'} and escaped data: #{'<em> is not emphasised</em>'}. 
      | This line follows on.
    p= 'Evaluated and <em>escaped expression</em>:' + title

    <!-- You can add HTML comments directly -->
    // You can add single line JavaScript comments and they are generated to HTML comments
    //- Introducing a single line JavaScript comment with "//-" ensures the comment isn't rendered to HTML 
    
    p A line with a link 
      a(href='/catalog/authors') Some link text
      |  and some extra text.
    
    #container.col
      if title
        p A variable named "title" exists.
      else
        p A variable named "title" does not exist.
      p.
        Pug is a terse and simple template language with a
        strong focus on performance and powerful features.
        
    h2 Generate a list
        
    ul
      each val in [1, 2, 3, 4, 5]
        li= val
```



































## Third Party Middleware and Error Handeling 
One of the main advantages of node is that it allows third party libraries to be easily linked into the application.


As an example, common third party packages include: 

* **cookie-parser:** Used to parse the cookie header and populate req.cookies (essentially provides a convenient method for accessing cookie information).
* **debug:** A tiny node debugging utility modeled after node core's debugging technique.
* **morgan:** An HTTP request logger middleware for node.
* **http-errors:** Create HTTP errors where needed (for express error handling).

you can install these packages using 
```
npm install --save cookie-parser morgan debug http-errors
```
> **Note** You can see in ```package.json``` that the packages have been added to the "dependancies". 

> **Note** If your using a pre-built node application, you can install all the relevent dependancies by using ```npm install```.



### Importing the dependacies 
We can import our packages into the ```app.js``` express application in the same way that routes are imported. 

```javascript
app.use(logger('dev'));
app.use(cookieParser());
//Note that this needs to go before adding your own routes 
```

### Error Handeling 
Error handeling is one of the last things to do before exporting the app. 404 pages are one of the most common issues, where a user is directed towards a route or file where a user exists. 

The addition of the http-errors package allows for a easy way to detect different types of errors and execute a function 

```javascript
// 404 catch
app.use(function(req, res, next) {
  next(createError(404));
});
```

You can also add error handling and logging for developers only, specifically when they start on a local system using ```npm devstart``` 

```javascript
// error handler
app.use(function(err, req, res, next) {
  // set locals, only providing error in development
  res.locals.message = err.message;
  res.locals.error = req.app.get('env') === 'development' ? err : {};

  // render the error page
  res.status(err.status || 500);
  res.render('error');
});
```


























# MongoBD

Mongodb is a NoSQL database that stores data in JSON like (Javascript Object Notation).


## Installation of MongoDB  

>**Note:** Most of this guide comes from https://docs.mongodb.com/manual/tutorial/install-mongodb-on-ubuntu/ 

**Adding MongoDB Repositories (Depends on system)**
Depending on the version / distro of linux, MongoDB may not be in the package manger that we are using, if this is the case you will usually get an error stating that "the package is not avalible" or that it "is referanced by another package". 

In this case we can install the official mongodb repository and install the packages from there. 

First we have to import the GPG keys for the mongodb server
```sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv EA312927```

After this we can import the mongodb repository details so ```apt``` will know where the packages can be downloaded from. 

```echo "deb http://repo.mongodb.org/apt/ubuntu xenial/mongodb-org/3.2 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-3.2.list```

after adding the repository details, we can finish off with making sure that all the packages in the repository are up to date.

```sudo apt-get update```

### Installation of the packages  

   
Now we can install the MongoDB Packages   
```sudo apt-get install -y mongodb-org```  
This installes the latest stable version of MongoDB

### Uninstalling Mongodb    

```bash
sudo service mongod stop  
sudo apt-get purge mongodb-org*
```

You also have to remove the data directories
```
sudo rm -r /var/log/mongodb
sudo rm -r /var/lib/mongodb
```


If you get isses stating that mongodb-org dependancies are not met, you first need to remove the mongodb-org packages as well (using the same commands as above).

## Running MongoDB

**Note**  
>Directories  
If you installed via the package manager, the data directory (place where data is stored) **/var/lib/mongodb** and the log directory **/var/log/mongodb** are created during the installation.  
By default, MongoDB runs using the mongodb user account. If you change the user that runs the MongoDB process, you must also modify the permission to the data and log directories to give this user access to these directories.  

### Configuration (confing) Files
The configuration files can be found under **/etc/mongod.conf**

### Starting Mongodb
You can start the process using:   
```sudo service mongod start```  
You can also use:  
```sudo systemctl start mongodb```

>**Mongod** is the daemon that runs mongodb, this runs all the server tasks, including accepting requests, responding to clients and memory management.    
(deamons are programs that run in the background)  

>**Mongo** is a command line shell that can interact with the client - this can be usueful for system administrators and developers, but is not used if a program connects to a database over its api.

You can check that the process is running using:     
```sudo service mongod status```

### Stopping MongoDB
You can stop the mongod daemon using:  
```sudo service mongod stop```  

### Restarting MongoDB
You can restart the service using:  
```sudo service mongod restart```

If the Process is running, you should be able to see: 
```bash 
Output
● mongodb.service - An object/document-oriented database
   Loaded: loaded (/lib/systemd/system/mongodb.service; enabled; vendor preset: enabled)
   Active: active (running) since Sat 2018-05-26 07:48:04 UTC; 2min 17s ago
     Docs: man:mongod(1)
 Main PID: 2312 (mongod)
    Tasks: 23 (limit: 1153)
   CGroup: /system.slice/mongodb.service
           └─2312 /usr/bin/mongod --unixSocketPrefix=/run/mongodb --config /etc/mongodb.conf

```  

You should now have a local mongodb database running on your system.



## Accessing a MongoDB database using Mongo

>**Note:** Most of this guide comes from https://www.freecodecamp.org/news/learn-mongodb-a4ce205e7739/

Now that we have a database set up on a system / our local system, we can now access it to create new databases. 

if we open a new shell / terminal, we can use mongo to access our new mongod service. 

we can open the mongo mediator by using: 
```mongo```

We can find the current database we are in using:
```db```

We can list the current databases using: 
```show databases```


## Accessing a MongoDB database using a GUI 
We can also connect to a mongodb instance using other software.
One of the most commonly used GUI's for accessing mongodb is their own GUI software **MongoDB Compass** 

> You can download MongoDB Compass at https://www.mongodb.com/download-center/compass?jmp=docs

You can connect to the created local instance by selecting ```fill in connection fields induvidually```, Then entering in the following infomation.  

Hostname: ```localhost```  
Port:  ```27017```  
SRV Record: ```off```  
Authenticaion: ```None```  

If working, you should now see a list of the currrent databases within the mongod service. 


### Issues I've run into  

**Failed with result "exit code" / error 100**
```
● mongodb.service - An object/document-oriented database
   Loaded: loaded (/lib/systemd/system/mongodb.service; enabled; vendor preset: enabled)
   Active: failed (Result: exit-code) since Mon 2019-11-25 10:11:32 GMT; 1 day 23h ago  
**Adjusting Firewall Options**
Even Though the MongoDB server has been set up, it will still only be accessable locally and will not be acceable from other systems.

To allow access to the MongoDB database from anywhere on the internet: 
```sudo ufw allow 27017``` 

This is however not usually a good option as it opens up the database to the *entire internet*.   

A much better way to access the database is to allow the server hosting you application access, then have that open to the internet instead:  
```sudo ufw allow from <other server IP>/32 to any port 27012```

You can then verify your new port access with ```sudo status ufw```

You should now be able to see what has access to what ports:
```bash
Status: active

To                         Action      From
--                         ------      ----
OpenSSH                    ALLOW       Anywhere
27017                      ALLOW       Anywhere
OpenSSH (v6)               ALLOW       Anywhere (v6)
27017 (v6)                 ALLOW       Anywhere (v6)

```



## Getting Started with MongoDB 

### Terminology 
**Database:** A physical container for collections, each database gets its own set of files and a directory system. A single MongoDB server typically has multiple databases.

**Collection:** A Collection is similar to a table in RDBMS systems. One major differance is that collections do not enforece a schema (a standardised framwork / order).

**Document:** Documents are a set of key-value pairs (linked) data. They can have ```dynamic schema``` meaning that they do not need to have the same set of fields or structure.  

**Schema:** A schema is a way for data to be mapped to a MogoDB collection and is used as a blueprint to define the format of the documents within a collection


Comparison of Relational Database Management System ```RDBMS``` Terminiology with noSQL Terminology 
```
   RDBMS                 noSQL

   Database              Database
   Table                 Collection
   Tuple / Row           Document
   Column                Field
   Table Join            Embedded Document
   Primary Key           Primary Key (key_id provided by mongodb)

```

## Using Mongo 
we can open the mongo mediator (program to control mongodb) by using: 
```mongo```


### Database Navigation
We can find the current database we are in using:  
```db```

We can list the current databases using:   
```show databases```

We can switch databases using:   
```use <database name>```  
> **Note:** If you navigate to a database that does not exist, it will create a new database. 

We can clear a screen using:  
```cls```  

### Database Population
We can create a database using:  
```use <database name>```

We can show databases using:  
```show databases```

We can create collections using:   
```db.createCollection('articles');```


We can show collections using:   
```show collections```

We can create a document inside the collection using:    
```db.articles.insert({title:"Article One",author:"George Went",body:"This is article one"})```

We can add multiple documents at once using:
```
db.articles.insertMany([
      {title:"Article One",author:"George Went",body:"This is article one"},
      {title:"Article One",author:"George Went",body:"This is article two"}
   ]);
```

We can show all the documents inside a collection using:   
```db.articles.find();```

We can show all the documents inside a collection in a more readable manner using:   
```db.articles.find().pretty();```


### Data Location 
You can find (and change) the location of where you data is stored by going to the configuration files and looking under ```dbPath```    

By default these are located at ```/etc/mongod.conf```
 
> **Note:** The default location that data is stored in is ```/var/lib/mongodb```



# Mongoose 
Mongoose is a client API ```(application programming interface)``` which allows us to modify MongoDB databases within node. Mongooses main purpouse is ```document modelling```, allowing us to process documents before adding them to the database. 

## Installing Mongoose 
We can install the Mongoose npm package using:   
```npm install --save mongoose```

## Getting Started

### Connecting to a MongoDB Database
```js
//Importing Mongoose 
var mongoose = require('mongoose');

db = mongoose.connect('mongodb://localhost/test');
//moongoose.connect(url / location)
//you can assing a varaible to the connected database
```
This code snippet will allow us to use moongoose, then connect to a database at a specified location. 

You can also create a callback to the database being connected, or failing to connect.

```js
//Reports the error to the conosle log screen if it has failed to connect
db.on('error', console.error.bind(console, 'connection error:'));

//Reports that the database has successfully been connected to
db.once('open', function() {
  // we're connected!
  console.log('connected to nodedb')
});
```

### Creating a Schema 
While you can create schemas directly into the app.js file, creating them in a seperate file and then exporting them as modules allows us to reduce the complexity of the code. 
```
 Models
    book.js
 app.js
```
Example of a schema:  
```js
//Import mongoose
let mongoose = require('moongoose');

//Article Schema
let articleSchema = mongoose.Schema({
    title:{
        type: String,      //Variable Type
        required: true     //Is this variable required? (default is false)
    },
    author:{
        type: String,
        required: true
    },
    body:{
        type: String,
        required: true
    }
});

//Export the js file as a module (class) called 'Article'
let  Article = module.exports = mongoose.model('Article', articleSchema)
```
>**Note:** ```mongoose.model('Article', articleSchema)``` is where we specify what collection we want to connect to within the mongoDB database. This is then defined as ```Article``` as an export

#### Schema types (fields)
A schema can have an arbitary number of fields - each one represents a 'field' in the documents:

```js
var schema = new Schema(
{
  name: String,
  binary: Buffer,
  living: Boolean,
  updated: { type: Date, default: Date.now() },
  age: { type: Number, min: 18, max: 65, required: true },
  mixed: Schema.Types.Mixed,
  _someId: Schema.Types.ObjectId,
  array: [],
  ofString: [String], // You can also have an array of each of the other types too.
  nested: { stuff: { type: String, lowercase: true, trim: true } }
})
```
While most follow other database value types, their are 3 exceptions: 
```ObjectID```: Represents specific instances of a model in the database - this will actually contain the unique ID ```(_id)``` that the field has. 

```Mixed```: An 'anything goes' type field

```[]```: An array of items - you can pull javascript operations on these models. 

#### Schema Validation
Mongoose provides built-in custom validation
The build in validators include :
* All schema types have the ```required``` validator. This is used to specify whether the field must be supplied in order to save a document 
* ```Numbers``` have ```min``` and ```max``` values.
* Strings have: 
  * ```enum```: specifies the set of allowed values for the field 
  * ```match```: specifies a regular expression that the string must match.
  *  ```maxlength``` and ```minlength``` for the string.

```js
var breakfastSchema = new Schema({
  eggs: {
    type: Number,
    min: [6, 'Too few eggs'],
    max: 12,
    required: [true, 'Why no eggs?']
  },
  drink: {
    type: String,
    enum: ['Coffee', 'Tea', 'Water',]
  }
});

```
#### Virtual Properties 
Virtual Properties are properties that a person can get and set, but do *not* persist to a MongoDB database.   
```Getters```: Useful for formatting or combining fields.    
```Setters```: Useful for de-composing a single value into multiple values for storage.  




###  Retriveing Documents from the Database
Now that we have a schema to pull data from a collection onto a blueprint, we can now contact the database to ask for data to be sent in the schemas format.

Our first step in the ```app.js``` file is to bring in the modeles (schemas) that we have created and are set up for export. 

```app.js```
```js
// Bring in Models
var Article = require('./models/article');
```

This gives us access to the schema 

```js
// Article List Route
app.get('/articles', function(req, res){

  // Pulling from a Database 
  Article.find({}, function(err, Articles){
    // If it cant find the articles collection - sends error
    if(err){
      console.log(err);  
    }
    //If it can find articles - render infomation from the collection
    else{
      res.render('articles', {        // Renders ./view/articles
        title: 'Article',             // Defines to pug variable 'Title'
        articles: Articles            // Defines pug variable 'Articles'
      });
    } 
  });
});
```
We also need to add a template under the views:  
```articles.pug```  
```
extends layout

block content
   h1 #{title}
   ul                                  // Unorderd (bullet point List)
      each article, i in articles      // for each article (n) in the database
         li= article.title             
         li= article.author           
         li= article.body
```


>**Note:** We dont need to specify the collection we need to connect to, or specify what part of the data we need to get, this is sorted out by the schema we have in ```./models/articles``` 

>**Note:** Remeber that we have exported the schema and called it ```Article``` - this is what we use to referance the schema in ```app.js```, the connection to the database are handeled in ```articles.js```.


### Saving Documents 
We can also use the articles schema to save documents into certian collections that can be used by forms to map data.





























## Forms 
Forms can be used to collect infomation from a user which can then be submitted to the server for recording into a database or for further processing. 

#### The main goals of a form is to: 
1. Dispaly the default form the first time it is requested by the user. This form can contain blank or pre-filled fields.
2. Recive data submitted by the user, usually in a HTTP ```POST``` request.
3. validate and sanitize the data. 
4. If any data is invalid, re-display the form with error messages
5. If all data is valid, peform the required form actions, such as saving data to a database, sending an email or modifying the ented data to produce a result. 
6. Once all actions are complete, redirect a user to another page, or notify the user that the task has been complete. 

>**Note:** When looking at code for a form, the actual function dealing with form submission can be quite small, what makes up the bulk of form submission (and complications that can occur due to form submission) is to do with making sure that the data entered into a form is correct.  

### Creating a Form 

> 1. Dispaly the default form the first time it is requested by the user. This form can contain blank or pre-filled fields.

The first task is to create a html form that clients can access to add new articles to the database.  

```add_articles.pug```
```pug
extends layout

block content
   h2 #{title}  // matches 'title' variable in res.render
   body
      form(action='/articles/add', method='POST')
         div
            label(for='title') Title:
            input(name='title', type='text')
         br
         div
            label(for='author') Author:
            input(name='author', type='text')
         br 
         div
            label(for='body') Body:
            input(name='body', type='text')
         br
         button(type='submit') Add
```
The most important part of the pug file is the ```form(action='/articles/add', method='POST')``` as this dentoes that:   
1. When a ```submit``` element is triggered the form runs ```/articels/add```
2. The method that the form uses, The two most common methods are:
   * ```GET```: This is for changing and viewing something, usually a web page or to pull infomation from a database or another site, you cant change infomation using ```get```.
   * ```POST```: This is used for writing or submitting data to be processed, and can result in the creation of new resoureces, or updating existing resources. 


>**Note:** One of the main things to make sure to check is the indetation on pug files, as elements that are not indented properly (such as form buttons) will not be 'included' in the form.


Now that we have the pug file layout ready, we can create a new route to add the layout to (within ```app.js```):

```js
// Add Articles 
app.get('/articles/add', function(req, res){
  res.render('add_articles', {
    title: "Add Article"     
  });
});
```


### Getting a Response from client to server 

> 2. Recive data submitted by the user, usually in a HTTP ```POST``` request.

Before we can communicate from client to server to database, we can check the our form does actually send data from the client to the server. We can check this just by adding a console log that is run when a client processes a form. 

>**Note:** app.post is our ```form-handler``` which is what is run when a user activates a ```submit``` element (the button).

```app.js```
```js
// Add Article POST Route 
app.post('/articles/add', function(req, res){
  console.log('submitted');  // On a successful POST, retuns a 
  return;                    
  // Stopps the execution of the function after posting the log
});
```
>**Note:** Routes can have both a ```GET``` and a ```POST``` function.

When run you can see that submitting the form will cause the console.log function to run.

### Handling Form Input
Trying to parse (interpret) requested text from a form using normal methods will usually result in a fault/error.

```js
app.post('/articles/add', function(req, res){

  console.log(req.body.title); //Request the HTML element 'title'
  console.log(req.body);       //Requests all HTML elements within 'body'
  return;                    
});
```
While the above code would seem to work, in reality it will only produce an error message

#### Installing Body-Parser
We can retrive submitted form data by using a npm package called ```body-parser``` which allows us to parse form data within a request body.

You can install body parser using:  
```npm install --save body-parser```

Within ```app.js``` we can define bodyparser:
```js
const bodyParser = require('body-parser');
```

We then need to tell the app to use the package, this can be added after initilising express, but before any of the routes are defined:
```js
// Initilise express application  
const app = express();

//Body Parser
  // parse application/x-www-form-urlencoded
app.use(bodyParser.urlencoded({ extended: true }))
  // parse application/json
app.use(bodyParser.json())

//Routes
``` 
>**Note:** The ```{extended: true}``` function allows for the posting and parsing of nested objects/bodys (``` { person: { name: John} } ```). If set to ```false``` then nested objects are not allowed.

### Handling Form Input (For Real)

Now that we have body-parser, we can run the code and our data will move from the clients form to our servers console! 
```js
app.post('/articles/add', function(req, res){

  console.log(req.body.title); //Request the HTML element 'title'
  console.log(req.body);       //Requests all HTML elements within 'body'
  return;                    
});
```
When the above snippet is run, you (should) be able to see the title of the article in your console, while this doesnt seem like much it shows that we can now take data from the client to the server :D.

We now need to get this data into the database.
First we can move the data straight from the form into the model we created to connect to the mongodb database. 

```js
  let article = new ArticleModel();         //Creates a new instance of ArticleModel Collection
  article.title = req.body.articleTitle;    //Links the new instace of ArticleModel to the HTML element articleTitle (in the pug file)
  article.author = req.body.articleAuthor;
  article.body = req.body.articleBody;
```

Now that we have mapped our form to an instance of the ```ArticleModel``` collection, we can now save this data to the mongoDB database. 

MongoDB has the ```.save()``` function, which allows us to save our mapped ```ArticleModel``` to the mongoDB database. 

To just save the model we can use ```db.collection.save()```, which in out case would just be ```article.save()```.

However we also want to check that the data that we are saving is correct - while issues like sql injection can be dealed with later, we should still have some sort of test in place. 

We can add a function to check for issues within the ```save()``` 

```js
article.save(
   function(err){
    if(err){                        
      console.log(err)            //If there is an error, posts the report to the console
      return;
    } else {
      res.redirect('/articles')   //Otherwise returns the client to /articles
    }
  });
```

## Validating and Sanitization

> 3. validate and sanitize the data. 

While we can write our own checks to form validation, we can also use pre-exisitng middleware. ```express-validator``` is a commonly used npm dependancy that provides a number of useful methods form the sanitization and validation of client input.

You can install it using:  
```npm install express-validator --save```

As with other npm dependancies or middleware, to require the functions we need the following code in ```app.js```.
```js
const { body,validationResult } = require('express-validator/check');
const { sanitizeBody } = require('express-validator/filter');
```

### Defining functions within express validator 
```js 
body(fields[,message])
```
This specifies a set of fields that the request ```body``` (a POST parameter) to validate. The ```[message]``` is optional, and can be used to display error messages in the element specified. 

Checks if a name has been entered, if not - display "empty name"
```js
body('name', 'Empty name').isLength({ min: 1 })
``` 
Checks if a date has been entered in the correct manner - the ```optional({ checkFalsy: true })``` allows null and empty strings to *not* fail validation.
```js
body('age', 'Invalid age').optional({ checkFalsy: true }).isISO8601(),
```

You can also daisy chain different validations, with messages that display if the previous validations are true. 

The below example checks for two validators: first it checks that there is a name has been entered, if this is true, it then checks that the name only consists of alphabetical characters.  
```js
body('name').isLength({ min: 1 }).trim().withMessage('Name empty.')
    .isAlpha().withMessage('Name must be alphabet letters.'),
```

#### Sanitisation 
Sanitisation is the process of removing specific characters from form inputs so that issues such as cross site attacks and SQL injection can't occur.  

```js 
sanitizeBody(fields)
```
Commonly used sanitization methods are daisy chained together: 
```.trim()```: used to remove whitespace at the beginning and end of a string.
```.escape()```: used to remove HTML characters (such as < and " ) from a string. 

#### Validation Results
As well as sending messages within the form object / body, express validator also bundles the results of your validations into a ```validationResult ``` object that can be requested and used by other functions.

```js
(req, res, next) => {
    // Extract the validation errors from a request.
    const errors = validationResult(req);

    if (!errors.isEmpty()) {
        // There are errors. Render form again with sanitized values/errors messages.
        // Error messages can be returned in an array using `errors.array()`.
        }
    else {
        // Data from form is valid.
    }
}
```

Once we've dealt with our sanitisation, we can start to deal with the users data (providing its correct)

### Dealing with form data  (errors in submitted forms)









> 4. If any data is invalid, re-display the form with error messages

One of the main issues that people come across with forms is what happens when it goes wrong, thankfully we can use the object ```validationResult``` as a way to check for all of the above checks we made for our form.

Our code for checking errors in the author controller is:

```js
  // assign the requested data from our validation results to the var 'error'
  const errors = validationResult(req);

  if (!errors.isEmpty()) { // (if errors is not empty )
      // There are errors. Render form again with sanitized values/errors messages.
      res.render('author_form', { 
          title: 'Create Author', 
          author: req.body, 
          errors: errors.array()
      });
      return;
  }
```

### Working with the form data 
Now that we have our correct form data, we can start to work with it, whether it just be sitting client side on the users machine, or needing to be sent to a database located on another server. 

> 5. If all data is valid, peform the required form actions, such as saving data to a database, sending an email or modifying the ented data to produce a result. 

For anything that just still runs client side, we can run our operations here


In terms of the authorController class, we need to move this into our noSQL database.
Our first step is to wrap up the form data into a variable that we can use to submit to the database. This is where our model ```author.js``` comes in. 

```author.js``` simplified 
```js
var mongoose = require('mongoose');
var Schema = mongoose.Schema;
var moment = require('moment');

var AuthorSchema = new Schema(
  {
    first_name: {type: String, required: true, max: 100},
    family_name: {type: String, required: true, max: 100},
    date_of_birth: {type: Date},
    date_of_death: {type: Date},
  }
);

//Export model
module.exports = mongoose.model('Author', AuthorSchema);
```

back in our authorController class, we can assign our exported mongoose model ```Author``` to the variable author, allowing us to save data to the model using mongooses ```.save()``` function:

```js
else {
    // Create an Author object with escaped and trimmed data.
    var author = new Author(
        {
            first_name: req.body.first_name,
            family_name: req.body.family_name,
            date_of_birth: req.body.date_of_birth,
            date_of_death: req.body.date_of_death
        });
    // save the form data to the linked database
    author.save(function (err) {
        if (err) { return next(err); }
        // Successful - redirect to new author record.
        res.redirect(author.url);
    });
}
```

6. Once all actions are complete, redirect a user to another page, or notify the user that the task has been complete. 

As you might have seen in the above code, once the function to save our form data to the database completes, the controller sends a response ```res``` to redirect the user back to the author url page - thereby showing the user that the author has been created in the database. 











## Uploading Files

When a user makes a POST Request for a website you have to endcode data that forms the body of the request in some way so that it cant be accessed by outside sources other than the server and the client. 

while in most cases using 





## TODO

1. Find out how to use HTML instead of pug 
2. Work out multipart files formtatting - express streams? 
3. 