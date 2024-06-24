#!/usr/bin/node
const myVar = process.argv[2];
const change = parseInt(myVar);
if (isNaN(change)) {
  console.log('Not a number');
} else {
  console.log(`My number: ${change}`);
}
