# VUE

## Without vue

```html
<!DOCTYPE html>

<html>
  <head>
    <title></title>
  </head>
  <body>
    <input type="text" id="input" />
  </body>
</html>

<script src="https://unpkg.com/vue@2.1.3/dist/vue.js"></script>
<script>
  // Create an object "data" with the property "message"
  let data = {
    message: "Hello World",
  };

  // Select the element "input" and bind the value of it to the value of data.message
  // input.value will now equal what data.message is
  document.querySelector("#input").value = data.message;
</script>
```

## With Vue

```html
<!DOCTYPE html>

<html>
  <head>
    <title></title>
  </head>
  <body>
    <!-- Vue Binds to objects  -->
    <div id="root">
      <input type="text" id="input" v-model="message" />

      <p>The value of the input is: {{ message }}.</p>
    </div>
  </body>
</html>

<script src="https://unpkg.com/vue@2.1.3/dist/vue.js"></script>

<script>
  new Vue({
    el: "#root", // Vue will work on the 'el' -  element (and child elements) with the id "root" (in this case its div)

    data: {
      message: "Hello World",
    },
  });
</script>
```
