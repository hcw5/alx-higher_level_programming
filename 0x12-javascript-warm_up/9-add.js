#!/usr/bin/node
const a = parseInt(process.argv[2]);
const b = parseInt(process.argv[3]);
function add (a, b) {
  return (a + b);
}

console.log(add(a, b));
/*
const sum = (function add (a, b) {
  return parseInt(a) + parseInt(b);
})(process.argv[2], process.argv[3]);
console.log(sum);
*/
