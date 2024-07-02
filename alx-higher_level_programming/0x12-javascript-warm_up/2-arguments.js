#!/usr/bin/node
const { argv } = require('node:process');
const msg1 = 'No argument';
const msg2 = 'Argument found';
const msg3 = 'Arguments found';

const len = argv.length;
if (len === 2) {
  console.log(msg1);
} else if (len === 3) {
  console.log(msg2);
} else if (len > 3) {
  console.log(msg3);
}
