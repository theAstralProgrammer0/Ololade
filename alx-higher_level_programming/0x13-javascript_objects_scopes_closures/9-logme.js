#!/usr/bin/node
let count = 0;

exports.logMe = function (item) {
  function logCounter () {
    console.log(`${count}: ${item}`);
    count += 1;
  }
  return (logCounter());
};
