#!/usr/bin/node
const { argv } = require('node:process');

let currMax;
let value;
let num;

if (argv.length <= 3) {
  console.log(0);
} else {
  currMax = parseInt(argv[2]);
  value = -Infinity;
  let i = 3;
  while (i < argv.length) {
    num = parseInt(argv[i]);
    if (num > currMax || num === +Infinity) {
      value = currMax;
      currMax = num;
    } else if (num > value) {
      value = num;
    }
    i += 1;
  }
  console.log(value);
}
