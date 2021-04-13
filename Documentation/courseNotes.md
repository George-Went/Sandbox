
# Course Topics 
## Notes (Basic Functions)

## Export Modules (require xyz)
### validation

## Chalk 

## Global packages and nodemon

## Command Line options and yargs

## Accessing file systems 

## Using Yargs

## ES6 Functions 

## Debugger and inspecting applications 
Debuggin node can be done using the chrome browser
due to the fact that chrom also runs on the V8 engione, google has added the ability to inspect and pause applications to see the variables and values wirthin an application. 

```js
debugger 
// To use a debugger, put 'inspect' before the script name 
// In thsi case it would be 'node inspect app.js --title="" --body=""'
```

To visit the debugger used by chrome, we can visit 
```chrome://inspect```

Remote target 
Port and localhost target (both are the same target)

## Error Messages in V8 
Error Code - This is a referance to what type of error you have 
Stack trace - this will show what functions were executed by the program to get to the code that had the error in. 


## Asynchronous Requests
Most of the functions used within node are asynchronus by design:  

```js
// Asynchronus programming example 
console.log('Starting Application')

setTimeout(( ) => { 
    console.log('2 second timer')
}, 2000 )

setTimeout( () => {
    console.log('0 Second timer') 
    // set time out is a node function provided by C++
}, 0)

console.log('Stopping')
// Stopping prints before the timer, even though it is after
```

When we run this program we can see the order in which they execute: 
1. Starting application 
2. Stopping application 
3. 0 Second Timer 
4. 2 Second Timer 

Even though the 0 second timer should have executed as soon as possible, the stopping timer still executed before it. 

This is due to the way that the **call stack** works - software is functions built ontop of functions, meanging that some functions are subservient to other functions.  

```js
// Call Stack Example
// location is under listlocations and so you get a 'stack' of methods that 
// get executed in the call stack 
const listLocations = (locations) => {
    locations.forEach((location) => {
        console.log(location)       
    });
}

const myLocations = ['London','Manchester','Birmingham']

listLocations(myLocations)
```


When a controller only needs to take one this works fine, however what if a user wants to take multiple requests - such as collecting multiple sets of data from a database or also dispalying images at the same time.  

You could daisy chain the operators together so that function 1 calls function 2 and when function 2 is complete function 1 runs - with multiple requests this can become very messy an leads to complex nested code, known as ```callback hell```.

>**Note:** Traditionally, code is executed in a linier fashion with one function/method taking place after the other (this is completly oversimplifying it). Due to the high level nature of node if we too this at its word, we would have massive daisy chains of code so that a database + a client and a server (and all the exception checks) - making it unreadable (for me at least)


### Callbacks
A very basic view of a callback is that a child method is sent out by its parent to fetch some data, the collection of this data could take some time, so the execution is unknown. When this child method finds the data, it returns back to the parent method with its results.

Example of a callback using ES6: 
```js
const doWorkCallback = (callback) => { 
    setTimeout(() => {
        callback('This is my error', undefined)
    }, 2000)
}

doWorkCallback((error, result) => {
    if (error) {
        return console.log(error)
    }

    console.log(result)
})
```

The same callback using normal syntax 
```js
doWorkCallback = function(callback){
    setTimeout(() => {
        callback('This is my error', undefined)
        // The first callback var is always called if there is an error
        // The second var is called if there is a result 
    }, 1000)
}

doWorkCallback((error, result) => {
    if (error) {
        return console.log(error)
    }

    console.log(result)
})
```

>**Note:** A good analogy is a parent doing a standard shopping trip with a child along a set route, while walking past the vegitable isle, they mention to the child that they need to get some milk. The parent then sends off the child to collect the milk, while they themselves continue with the rest of the shopping and then gets to the checkout and waits for the child. after a while, the child returns with the item and they can pay for the stuff they have ordered. 




### Call Stack 
In a simple synchronous application, the callstack tracks the execution of a program from its inception at a point like `app.js` to its final endpoint. With engines, when the program finishes it repeats again, with events being triggered if the programed conditions are met. This givecs rise to the name `event loop`.  

You can see what a call stack is when you get an error in languages like node or java - the functions that are called that lead up to the error are printed out in the manner they are called - a call stack. 

>**Note:** historically a stack






















## Promises
Promises are simalar to callbacks in that they return a success or failure state for a method in an asychonous environment. However, unlike callbacks, promises allow for execution of code depending on the error, rather than just passing that an error has occured. 

With a correct return, a ```.then``` is used.
With a error return, a ```.catch``` is used

Example of a promise: 
```js
const doWorkPromise = new Promise((resolve,reject) => {
    setTimeout(() => {
       // resolve([7,4,1])
        reject('Things went wrong') // We can only call either a resolve or reject
    }, 2000)
})

// Success - resolve 
doWorkPromise.then((result) => {
    console.log('Success', result)// function goes well - resolve is called
}).catch((error) => {
    console.log('Error', error)   // function failed - reject is called
}) 



```

>**Note:** In the 'supermarket example', a comparison can be made that with a callback, the child method just comes back to the parent with a "i cant find milk" statement. With a promise, the parent can say that if there isnt any milk, then they should get cheese instead. 






















## HTTP Requests



## API Requests
An application programming interface (API) is used to reqest infomation from a Application through a protocol or Program, via the usage of a standardised procedure or (usually) non-graphical Interaface. 

>**Note:** Technically a desktop environment, a Graphical User Interface (GUI) can be considered an Application Programming Interface. 

The examples given below are using the weatherstack api (https://weatherstack.com/). 


With modern day web design, the main protocol for consuming data requested from another site is through a JSON (Javascript Object Notation) GET request. 

```js
// Requesting the entire JSON object and paring it while in the application
request({ url: url},(error, response) => {
    console.log(chalk.red("All JSON Object"))
    console.log(response)                      // Responds with entire JSON string
    const dataJSON = JSON.parse(response.body) // Parsing JSON 
    console.log(dataJSON)                      
})

// Requesting only the current weather JSON data 
// We can use a request function to parse JSON
request({ url:url, json: true }, (error, response) => {
    console.log(chalk.blue("Request current JSON"))
    console.log(response.body.current)         // requesting only the current weather JSON
})


// Parsing and reporting data in a useful manner
request({ url:url, json: true }, (error, response) => {
    const weatherData = (response.body.current)

    console.log(chalk.green("Weather Report "))

    console.log('Temperature: ' + weatherData.temperature)
    console.log('Wind speed: ' + weatherData.wind_speed)
    console.log('Pressure: ' + weatherData.pressure)
    console.log('Humidity: ' + weatherData.humidity)
    console.log('Cloud Cover: ' + weatherData.cloudcover)
})
```

One of the main things to note about the ```response.body.<stuff>``` requests is that ```the response.body``` is the main standard within node (and other web language frameworks)  while anything that comes after this is from the JSON reply itself.  
For example, if a JSON looked like: 
```JSON
{
  "request": {
    "type": "LatLon",
    "query": "Lat 37.83 and Lon -122.42",
    "language": "en",
    "unit": "m"
  },
  "location": {
    "name": "North Beach",
    "country": "United States of America",
    "region": "California",
    "lat": "37.806",
    "lon": "-122.411",
  },
  "current": {                 
    "pressure": 1025,       
    "cloudcover": 100,
    "visibility": 16,
    "is_day": "yes"
  }
}
```
The main way to call a specific value would be to call the nested varibles in the json e.g ```current.pressure```
```js
request({ url:url, json: true }, (error, response) => {
    const weatherData = (response.body.current.pressure)
})
```
whereby ```response.body``` is telling the program to look in the body of the response (an will usually be checked in a IDE), the ```current.pressure``` is part of the JSON (and will not be picked up by an IDE - something that caught me out a lot in the past)

If a response comes with a array rather than a series of nested JSON's, you can also use ```response.body.current[1]``` to referance the array rather than a JSON(Object(Object))   


















## Web Servers


```js
const path = require('path')       // path allows us to access other directories in the server 
const express = require('express')
```
`/`  = absoloute link : From /root  
`./` = relative link  : From the current directory 


```js
console.log(__dirname) // absoloute path to the directory the file is in
console.log(__filename) // absoloute path to the file itself
console.log(path.join(__dirname, '../public')) // path module alows us to modify the file path
// it allows us to access files that are not in the same directory

const app = express() // link app to the express object
const publicDirectoryPath = path.join(__dirname, '../public') 
// assign the location of the public files to a variable

app.use(express.static(publicDirectoryPath)) // sets up the static file location to server static files
``` 
We can link to pages using 
```js
// Root
app.get('', (req, res) => { // (port, function(request, response))
    res.send('<h1>Hello express<h1>')
})
```

We can also link to html pages by linking the pages from root with html
for example ```localhost:3000/index.html```

## Template Engines
Templating engines allow us to create dynamic content rather than static content within node applications

```js
app.set('view engine', 'hbs')  //app.set('value', 'module'

// Root
app.get('', (req, res) => {
    res.render('index')
})
```
You can provide / inject values into .hbs files by using ``{{ }}``
index.hbs
```html
<body>
    <h1> {{title}}</h1>
    <p>{{name}}</p>
</body>

```
app.js
```js
app.get('', (req, res) => {
    res.render('index', {
        title: 'Hello World',
        name: 'George'
    })
})
```


















### Partial Templating 
Partial Templating allows us to template certian parts of the site such as a header or a navigation bar. 

Rendering a partial: 
header.hbs
```hbs
<h1>Static Header.hbs Text</h1>
```

help.hbs
```hbs
<body>
    {{>header}}     <!-- This is the partal file being imported into help.hbs -->
    <h1> {{title}}</h1>
</body>
```
> **Note:** When running the node application with partial templating, we need to use ```app.js -e js,hbs```. This notifies the app that both javascript and handlebars are being used

We can also change our header to referance html page variables from different pages. 

header.hbs
```hbs
<h1>{{title}}</h1>  <!-- This allows us to access title variables from the page variables -->
```

We can also create navigation menus using the template partials: 

```hbs
<h1>{{title}}</h1>  <!-- referances the 'title' variable from the app render variables -->

<div> <!-- division -->
    <a href="/">Weather</a> <!-- anchor -->
    <a href="/about">About</a> <!-- anchor -->
    <a href="/help">Help</a> <!-- anchor -->
</div>
```

## 404 Pages
404 pages can be used when the user goes to a User Resource Interface (URL) that does not match with any url exiting in the application. 
The 404 page has to be at the bottom of the application code so that it is the last executed route.
```js
app.get('*', (req, res) => { // The * (wildcard character) means it matches all urls 
    res.send('404 Page')
})
```

We can also create specific 404 pages by adding the wildcard symbol after a specific directory. 
```js
app.get('/help/*', (req, res) => { // '*' is a wildcard url 
res.render('404', {
    title: 'help',
    errorMessage: '404 - Help article not found',
    name: 'George Went'
    })
})
```
















## Styling applications
We can link css files within the /public directory by letting the express application (in this case, assigned to ```app```) know the location of the /public directory. We then assignt this link to the express static functions, allowing the application to serve static files. 

```js
const publicDirectoryPath = path.join(__dirname, '../public') // assign the location of the public files to a variable
const viewsPath = path.join(__dirname, '../templates/views')        // Assign the location of the views file to a custom directory
const partialsPath = path.join(__dirname, '../templates/partials')

// Set up handlebars  engine and views location 
app.set('view engine', 'hbs')  //app.set('value', 'module')
app.set('views', viewsPath)
hbs.registerPartials(partialsPath)


// sets up the static file location to server static files
app.use(express.static(publicDirectoryPath)) 
```

### Flexboxes
Flexboxes allow for more control over where content appears on a page
You can activate flexbox by changing the diplay mode:   
```css
body {
    /*set the display to allow flexboxes*/
    display: flex;
}
```
The default content will usually appear in a row, to change this you can set the flex-direction to column:  
```css
body{
    flex-direction: column; /*Default value is 'row'- arranges divs in a row*/
    min-height: 100vh; /*sets height 100% of viewport (display) height*/
}
```

We can set a flex-box to fill all avalible space on the body height by using ```flex-grow```
```css
.main-content{
    flex-grow: 1; /*allows a given element to grow to fill all spare space*/
}
```

## Accesing API's from a browser
API's can be used to send back data to a user based on the ```URL``` (User Resource Locator) - you cant pass data between pages client side (usually). The main way that server resources are pased is via ```query strings```, these always start by using the ```?``` symbol, for example a basic query string would look like  
```localhost:3000/products?search=food```
You can also search using multiple datasets using the ```&```
```localhost:3000/products?search=food&drink=water```  
  
API's usually respond with a JSON string that can be parsed to get specific data from a database or server.


### Query Strings 
We can set up a basic JSON response to a api request - this is an express rout handler 
```js
app.get('/products', (req, res) => {
    res.send({
        // Response is a JSON 
        products: []
    })
})
```




### Requests and Response functions
with ```app.get``` functions there are two main function parts to consider, the ```request``` and the ```response```, usually represented by ```req``` and ```res```.  

If we set up a route using a request, we can see that it returns serch terms used in the URL string.
```js
app.get('/products', (req, res) => {
    console.log(req.query.search)
    res.send({
        // JSON 
        products: []
    })
})
```
In a similar fashion to API request from a page, we can dissasemble the url into its component parts, for the code example above using the URL ```localhost:3000/products?search=food```.     
Breaking this down we can see that:  
1. THe client is *req*uesting to go to the ```/products``` page. 
2. The server should prepare for a query due to the ```?``` in the url
3. THe query is that the client wants to search for something
4. The search term is ```food```
5. The server can now *res*pond to the request, it```.send``` back a JSON string showing the produts.
6. In this case the server also sends a console log saying what the search term that was used within the url (```food```).


You can also change the response infomation based on the data send in the request url:

```js
app.get('/weather' ,(req, res) => {

    if (!req.query.address){  // This code only runs when the request fails
        return res.send({
            error: 'You must provide a location search term'
        })
    }

    console.log(req.query.address)

    res.send({
        location: req.query.address, // JSON takes data from the url address term
        temperature: 17,
        wind_speed: 5,
        cloud_coverage: 'Overcast '
    })
```
In the below example, if a user goes to ```localhost:3000/weather?address=[address]``` then the address term in the JSON is the same as the address searched in the url.

### Problems you can run into 
```
Error: cannont set headers after they are sent to the client
```
This is due to the server trying to respond twice to the user, http request have a single request that goes to the server and a single respone that comes out from the server. The above error message is due to the server trying to send back two responses. This can be fixed by either using a ```return``` statment or making sure that all responsed are covered by defensive features such as ```else``` clauses. 


An example of code that sends back two responses base on the url it recieves ```/product?search=[item]```:  
```js
app.get('/products', (req, res) => {
    // This code only runs when the request fails 
    // e.g if there is no '?search' after product 
    if (!req.query.search){  
        res.send({
            error: 'You must provide a search term'
        })
    }

    console.log(req.query.search) // This still sends back even if there is not a search term.
    res.send({
        // JSON 
        products: []
    })
})
```

The same code with a fix:    
```js
app.get('/products', (req, res) => {
    if (!req.query.search){  // This code only runs when the request fails
        return res.send({  // Adding a retrun acts as a break - all code after this function does not run 
            error: 'You must provide a search term'
        })
    }

    console.log(req.query.search)
    res.send({
        // JSON 
        products: []
    })
})
```


















### Adding API Function as a respones to a API request
>**Context:** we have pre-built API utilities (```/utils/forecast.js```) that have been given to us to use in an application.  
How do we utilise these utility functions? 

### Loading in our function
Importing the functions into ```/src/app.js```
We can import the utilitiles like any other npm module:   
```js
const geocode = require('./utils/geocode')
const forecast = require('./utils/forecast')
```

### Using imported API functions
Due to the way that our utility functions work, we can put an address we have gotten from a url query into the function:  

```js
geocode(req.query.address, (error, data) => { // only error OR data will be called
    console.log('Error:', error)     // will return undefined if no error shows up, otherwise prints out error 
    console.log('Data:', data)       // will return data from location as an object 
})
```
we can see from the above code that we can pass in the queried address as a location in the geocode function. When this runs, we can get a printout of the location we have typed in the url back as data: 
```js
Error: undefined    // No errors were detected so no object was passed   
Data: { latitude: 53.46667,
  longitude: -2.23333,
  location: 'Manchester, Greater Manchester, England, United Kingdom' }
```

However, due to the way that the api works, our data is returned as an object, we can get past this by ```destructuring``` the ```data``` variable:

The below code prints out the data varaibles based on the address location

```js
geocode(req.query.address, (error, { latitude, longitude, location}) => { 
    console.log(latitude)
    console.log(longitude)
    console.log(location)

})
```


### Default parameters


### Fetch
Fetch is a *browser* (client side) based function that can be used to collect api's from sites or web pages. Fetch kicks off asynchronous operations that are executed when the data is avalible. 
```js
// Function gets puzzle json object from the url, then prints it into the clientside console.
fetch('http://localhost:3000/weather?address=london').then(response => {
    response.json().then((data) => { //takes the response and assigns it to the var 'data'
        if (data.error) {
            console.log(data.error)
        }
        else {
            console.log(data.address)
            console.log(data.forecast)
            console.log(data.location)
        }
    })
})
```










## Forms in Nodejs 
Creating the HTML front end for a form:
```html
<form>
    <input placeholder="location"> // placeholder can be use for showing example text
    <button>Search</button> This is the 'sumbit button that activates the form
</form>
```

### Client side javascript
While we have a form, nothing happens if we press it, we can use client side js in the ```public/js/app.js```:
```js
let weatherForm = document.querySelector('form')
weatherForm.addEventListener(`submit`, (e) => {
    e.preventDefault() // prevents the whol page from reloading when we click the search button

    console.log('testing')
})
```

>**Note:** The deafault function for form submission is to relaod the html page, this is a relic of a function from a time when efffective scripting to counter bad search results was not avalible.

>**Note:** When decalring variables that are expected to be changed, dont use ```const``` and the variable can sometimes be declared on the loading of the page and is now stuck on the default value. The way around this is to either use ```var``` or ```let```.

### Accessing and using data from forms
We can access data from forms by utilising either the ```document.querySelector``` or ```document.getElementById``` (if your elements have id's). These can then be put into variables and utilised by the client side javascript for various functions

```js
// input value is assigned to the var 'searchElement'
var searchElement = document.querySelector('input')

weatherForm.addEventListener(`submit`, (e) => {
    e.preventDefault()

    // search result is assinged to the var 'location'
    let location = searchElement.value

    console.log('testing')
    console.log(location)
})
```


















### Utilising forms and fetch requets
Both forms and fetch elements can be used together to create search forms that can be used to access data from either your own or other websites. 

THe example below allows us to enter in a location name and get the weather location, by combining a form and a fetch request to another area of the site that calls API requests.
```js
var searchElement = document.querySelector('input') // gets input from search box

weatherForm.addEventListener(`submit`, (e) => {
    e.preventDefault()

    let location = searchElement.value

    console.log('testing')
    console.log('http://localhost:3000/weather?address=' + location)

    fetch('http://localhost:3000/weather?address=' + location).then(response => {
    response.json().then((data) => {
        if (data.error) {
            console.log(data.error)
        }
        else {
            console.log(data.address)
            console.log(data.forecast)
            console.log(data.location)
        }
    })
})
```


#### .querySelector vs .getByElementId
QuerySelector can be used for selecting elements from the DOM by there element type, as long as the element you want is the first type on the HTML page.  

For selecting specific elements on a HTML page, you can select via id by using the ```#``` to specify that you're looking for an id. 
```js
// The HTML element with the id 'message-1' will be assinged to the var 'messageOne'
var messageOne = document.querySelector('#message-1')
messageOne.textContent = 'From Javascript' // On refresh message-1 element will display the text
// You can also input variables into messageOne, not just strings
```



















## MongoDB 

### Running MongoDB

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










## Using Mongdb 
We can interact with our mongodb database by installing the npm packages ```mongodb```. This will allow basic control over the database and will allow us to modify data within it.

### Setting up a connection
We can set up a connection to the mogodb server by using the following node code: 
```js
const Mongodb = require('mongodb')
const MongoClient = Mongodb.MongoClient

const connectionURL = 'mongodb://127.0.0.1:27017'
const databaseName = 'task-manager'

// var.connect(url, {options_object}, (error, client) => {})
MongoClient.connect(connectionURL, { userNewUrlParser: true }, (error, client) => {   
    if(error) {
        return console.log('Unable to connect to a database')
    }

    console.log('Connected')
}) 
```

>**Note:** Using ```mongodb://localhost:27017``` has been known to cause a variety of weird problems with mongodb, so in this case we can use localhost's ip: ```mongodb://127.0.0.1:27017```.

When this code runs the client will be connected to the database for as long as the program is running or until there is a interruption in the connection. 





>**Note:** For all of the example code, we are using a database called ```users```







### Interacting with the database
Our first interaction can be to create both a new ```database``` and a new ```collection```. Mongodb doesnt need a database to be previously created, when a new name is used for a database, a new database is generated with that name. 

We can link to a database by assinging a variable to the database connection. 
```js
const db = client.db(databaseName)
```
This means that when we call ```db```, we are communicating with the database. 

We can also add new ```collections``` to the database by inserting some data. Again, like mongodb databases, collections can be automatically generated if no previous collections exist.
```js
db.collection('users').insertOne({
    name: 'George',
    Age: 24
})
```

Overview of the db connection: 
```js
const Mongodb = require('mongodb')
const MongoClient = Mongodb.MongoClient

const connectionURL = 'mongodb://127.0.0.1:27017'
const databaseName = 'task-manager'

MongoClient.connect(connectionURL, { userNewUrlParser: true }, (error, client) => {   
    if(error) {
        return console.log('Unable to connect to a database')
    }

    const db = client.db(databaseName) 'db'
}) 
```





### Dealing with errors and callbacks 
While we can insert ```documents``` into the database, at the moment our code does not get a reply from the server saying that it was successful. This is where the usage of callbacks can come in.  
With our ```insertOne``` function, we can add a callback after the data is imputted, saying whether the insert worked or not.
```js
db.collection('users').insertOne({
    name: 'George',
    Age: 24
}, (error, result) => { // error OR result triggers based on the success of the operation
    if (error) {
        return console.log('unable to insert user')
    }

    console.log(result.ops) // ops (operations) contains all of the documents inserted
})
```
when run successfully, ```result.ops``` will return and array of all the documents (objects) inserted into the collection. If the program fails, we should get the return string with the 'unable to insert user error'. 

>**Note:** You can access the API documentation for the mongodb drivers at: https://mongodb.github.io/node-mongodb-native/3.6/api/index.html













### Object id's 
In a normal sql database, id's for objects are cumulative, going 1,2,3. In noSQL databases id's are Globaly Unique Identifiers (GUID). This allows mongodb databases to scale easily, without the chance of collisions. Another advantage is that the id's can be generated locally, without having to be on the database in the first place, removing the chance of collision in the first place. 

we can generate object id's locally using the below code:
```js
const id = new ObjectID()               // generates a new id
console.log(id)                         // prints the newly generated id 
console.log(id.getTimestamp())          // prints the time the id was generated
console.log(id.id)                      // prints the binary data
console.log(id.id.length)               // prints the id length
console.log(id.toHexString().lenght)    // prints back the id as a string

```
This will result in an object id - the above code run for the fisrt time gave me: ```5ebeade3d3f6e319478867b3```. The 12 byte object consists of: 
- a 4 byte value representing the seconds since the unix epoch (1/1/1970)
- a 5 byte random value
- a 3 byte counter, starting with a random value

We can use these generated id's as the value for new objects we are putting into collections. 
```js
// Inserting one document into a collection with a pre-defined id
db.collection('users').insertOne({
    _id: id,
    name: 'Harry',
    Age: 22
}, (error, result) => {// error OR result triggers based on the success of the operation
    if (error) {
        return console.log('unable to insert user')
    }

    console.log(result.ops) // ops (operations) contains all of the documents inserted
})
```
>**note:** In most cases we dont need to generate the id - its automatically generated, and we dont need the id to be manually generated in most cases when imputing data into the collection. 









### Querying (Reading) Databases 
We can query a database on values by using the ```findOne``` function:
```js
db.collection('users').findOne({ name: 'michale', age: 27}, (error, user) => {
    if (error) {
        console.log('Unable to fetch')
    }
    console.log(user) // prints out the docuemnt if found
}
```
This will returnt the **first** document that the program finds in the collection. 

We can also search by multiple attriburtes: 
```js
db.collection('users').findOne({ name: 'michale', age: 27}, (error, user) => {'do thing'}
```

If a search result does connect but there is no result with the matching attribute data, instead of an error it will return ```null```.

We can search for multiple documents within a collection using ```find().toArray()```:
```js
// Finding multiple users and inputing results into an array
db.collection('users').find({ name: 'george'}).toArray((error, user) => {
    if (error) {
        console.log('Unable to fetch')
    }
    console.log(user)
})
```

## Updating Documents 
Updating documents is a important part of managing databases as most stuff isnt a constant in real life. 

We can change one document via its id by using the below code.
```js
db.collection('users').updateOne(
    {_id: ObjectID('5ebec6b5b738ab26ff9ab101')}, // creating a new id object with our existing _id value
    {$set: {                                  // changing a documents variables
        name: 'mike',
        age: '25'                               // Changing name variable to 'mike'
    }
}).then((result) => {
    console.log(result)    // return result data (success state)
}).catch((error) => {
    console.log(error)     // return error data (failure state )
})
```
>**Note:** When finding (filtering) via the ```_id``` of a object, we need to referance the fact that it is a object, not a number (being built out of various data) - Overall this means that we need to use the below example instead of just ```_id: <id number>```
```js
_id: ObjectID('5ebec6b5b738ab26ff9ab101')
```

We can aso change multiple documents at once by using the ```updateMany``` - Note that this example uses the ```tasks``` collection.
```js
    db.collection('tasks').updateMany({
        completed: true
    },{
        $set: {
            completed: false
        }
    }).then((result) => {
        console.log(result)    // return result data (success state)
    }).catch((error) => {
        console.log(error)     // return error data (failure state )
    })
```




## Rest API's and Mongoose 

### Mongoose
Mongoose allows us to quickly set up schema based modeling for application data. This allows use to map application objects onto the mongodb database. 

We can connect to a database using mongoose with the following code below:
```js
// Connect to mongoose db
mongoose.connect('mongodb://127.0.0.1:27017/task-manager-api',{
    useNewUrlParser: true,
    useCreateIndex: true
})
```


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

You can see all the options at https://mongoosejs.com/docs/schematypes.html#string-validators


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
### Validation messages 
We can throw error meassages as a callback

We can also create our own validations
```js
const User = mongoose.model('User',{
    name: {
        type: String,
        required: true
    },
    age:{
        type: Number,
        validate(value) {
            if (value < 0) {
                throw new Error('Age must be a positive number')
            }
        }
    }
})
```

### Installing Validation npm Packages 
we can import validator.js which automatically does alot of the validation process for us. 

we can see the 

An example of a validation npm package being helpful is checking emails: 
```js
const User = mongoose.model('User',{
    name: {
        type: String,
        required: true
    },
    age:{
        type: Number,
        validate(value) {
            if (value < 0) {
                throw new Error('Age must be a positive number')
            }
        }
    },
    email: {
        type: String,
        required: true,
        validate(value) {
            if (!validator.isEmail(value)) { // using imported validator email check (note that it is flipped - if the value is NOT an email)
                throw new Error('Email is invalid')
            }
        }
    }
})

const me = new User({
    name: 'George',
    age: 24,
    email: 'Gep@'
})

```
With the above code, if a user does not have a verified email, they will be presednted with an error message. 





#### Virtual Properties 
Virtual Properties are properties that a person can get and set, but do *not* persist to a MongoDB database.   
```Getters```: Useful for formatting or combining fields.    
```Setters```: Useful for de-composing a single value into multiple values for storage.  



### Structuing a REST API (Representational State Transfer)
REST: Representational State Transfer
API: Application Programming Interface 
REST API: 'RESTful Application'

The REST api allow clients such as a web application to access and manipulate resources using a set of predefined operations. 

Resource: User or Task 
Predefined Operation: Ability to create a new task or mark as complete. Upload a file

#### Task Resources

Create : ```POST``` /tasks - Posts new data to server
Read: ```GET``` /tasks - Get existing data from server
Read: ```GET``` /tasks/:id - Get specific id data from server
Update: ```PATCH``` /tasks/:id - Update existing data 
Delete: ```DELETE``` /task/:id - Deleting a task by its id

#### What makes up a HTTP request?
Some text (litterally - no compression)

A Request: 
POST ```/tasks HTTP/1.1```
Accept ```application/json```
Connection: ```Keep-Alive```
Authorization: ```Bearer ubi7oigf8ogsdbo8dfbdsfn```

```{description: "get some food"}```


A Response: 
```HTTP/1.1 201 Created```
Date: ```wed,19 may 2020```
Server: ```Express```
Content-Type: ```application/json ```

{task data}



## Resource Creation Endpoints
While just reading (requesting) data from a database can be useful, API's are used in the creation and deletion of data as well. 

With Express we can easily create POST,PATCH and DELETE requets as well.

### Using Postman 
Postman is an application that allows you to test api endpoints without having to write bash scripts that return a string of json all the time. You can also save multiple types of request in a collection, allowing you to come back to them if you need to test them again.

### Creating a POST request 
POST requests are used by api's for creating data, as the client 'posts' data to a computer - usually in a JSON or XML format. 

With out users database, we have an example of a POST request in the main index file:
```js
app.post('/users', (req, res) => {      // responds to a POST 
    const user = new User(req.body) 
    
    user.save().then(() => {
        res.send(user)
    }).catch((e) => { // catch error (using 'e')
        res.status(400).send(e) // send back a 400 status (Bad Request)
    })
})
```



























