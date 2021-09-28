// Example Ternary
var age = 26;
var beverage = (age >= 21) ? "Beer" : "Juice";
console.log(beverage); // "Beer"


// Example Array
status = ['created','restarting','stopped','paused','exited','dead'];
console.log(status);

//Example Objects
container0 = {status: 'created'}
container1 = {status: 'stopped'}
container2 = {status: 'restarting'}

console.log(container1.status) 

// Loop Through Containers
for (let i = 0; i < 3; i++) {
    console.log("container" + i);
}
// v2
for (let i = 0; i < 3; i++) {
    console.log("container" + i);
}

function containerCheck(container) {
    if (container.status == "created") { return 'success'; }
    else if (container.status == "stopped") { return 'danger'; }
    else if (container.status == "restarting") { return 'warning'; }
    else { return 'none'; }
}

//v3
// containers = [
//     {name: "container_0", status: 'created'},
//     {name: "container_1", status: 'stopped'},
//     {name: "container_2", status: 'restarting'}
//   ]

//   for (let i = 0; i < containers.length; i++) {
//       console.log("Name " + containers[i].name)
// }

// //v4
// containers = [
//     {name: "container_0", status: 'created'},
//     {name: "container_1", status: 'stopped'},
//     {name: "container_2", status: 'restarting'}
//   ]


// function containerCheck(container) {
//     if (container == "created") { return 'success'; }
//     else if (container == "stopped") { return 'danger'; }
//     else if (container == "restarting") { return 'warning'; }
//     else { return 'none'; }
// }

// for (let i = 0; i < containers.length; i++) {
//     console.log("Name: " + containers[i].name)
//     console.log("Result: " + containerCheck(containers[i].status))
// }

// v5 --------------------------
// always always always use const or let. Otherwise you are poluting the global scope.
const containers = [
    {name: "container_0", status: 'created'},
    {name: "container_1", status: 'stopped'},
    {name: "container_2", status: 'restarting'},
    {name: "container_3", status: 'blah'}
]

// You're checking a status, not a container. Changing the name to this makes more sense
function containerStatusCheck(status) {
  // a switch makes more sense here
  switch(status) {
    case 'created': return 'success';
    case 'stopped': return 'danger';
    case 'restarting': return 'warning';
    default: return 'none';
  }
}

// as you don't required the index, a for..of loop is more suitable here
for (const container of containers) {
    console.log("Name: " + container.name)
    console.log("Result: " + containerStatusCheck(container.status))
}

// _________________________________________________________________________________________________________
// attempeted as a ternary (v1)
console.log("ATTEMPT 5")

function containerStatusCheck(status){
    return status == "created" ? 'success'
        : status == "stopped" ? 'danger'
        : status == "restarting" ? 'warning'
        : 'none';
}
for (const container of containers) {
    console.log("Name: " + container.name)
    console.log("Result: " + containerStatusCheck(container.status))
}

