#!/usr/bin/node
const x = process.argv[2];
const change = parseInt(x);
if (isNaN(change)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < x; i++) {
    console.log('X'.repeat(x));
  }
}
