#!/usr/bin/node
const x = process.argv[2];
const change = parseInt(x);
if (isNaN(change)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < x; i++) { console.log('C is fun'); }
}
