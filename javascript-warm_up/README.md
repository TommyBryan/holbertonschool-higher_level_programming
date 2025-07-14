# JavaScript - Warm up

## Requirements:

* ### Install Node 14

```bash
$ curl -sL https://deb.nodesource.com/setup_14.x | sudo -E bash -
$ sudo apt-get install -y nodejs
```

* ### Install semi-standard
```bash
$ sudo npm install semistandard --global
```

## Using Node.js
```bash
$ node
> console.log("Hello from Node!");
```
## Data Types
```javascript
let greeting = "hello";           // String
let age = 20;                     // Number
let isOnline = true;              // Boolean
let score = null;                 // Null
let result;                       // Undefined
let user = { name: "Tommy" };     // Object
let items = [1, 2, 3];            // Array
```

## Functions
```javascript
functions greet(name) {
    console.log("Hello " + name + "!");
}
greet("Tommy"); // Output: Hello Tommy!
```

## Conditions
```javascript
let age = 20;

if (age >= 18) {
    console.log("You're an adult.");
} else {
    console.log("You're a minor.");
}
```

## Loops
### For Loop
```javascript
for (let i = 0; i < 5; i++) {
    console.log("Number:", i);
}
```
### While Loop
```javascript
let count = 0;
while (count < 3) {
  console.log("Count is", count);
  count++;
}
```

## Arrays
```javascript
let colors = ["red", "green", "blue"];

console.log(colors[0]); // red
colors.push("yellow"); // add to end
colors.pop(); // remove last
```

## Objects
```javascript
let person = {
  name: "Tommy",
  age: 25,
  city: "San Juan"
};

console.log(person.name); // Tommy
```
