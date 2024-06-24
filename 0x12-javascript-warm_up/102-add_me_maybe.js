#!/usr/bin/node
const addMeMaybe = function (number, theFunction) {
  theFunction(++number);
};
exports.addMeMaybe = addMeMaybe;
