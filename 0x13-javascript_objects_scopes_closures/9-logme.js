#!/usr/bin/node
let count = 0;
exports.logMe = function (item) {
  console.log(`${count++}: ${item}`);
};
/* exports.logMe = function (item) {
  if (this.count === undefined) {
    this.count = 0;
  }
  function argPrinter () {
    console.log(`${this.count}: ${item}`);
    this.count += 1;
  }
  return argPrinter();
}; */
