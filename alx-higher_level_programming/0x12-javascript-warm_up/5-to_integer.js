#!/usr/bin/node
const { argv } = require('node:process');
const msg1 = 'My number:';
const msg2 = 'Not a number';

const num = parseInt(argv[2]);
if (num) {
  console.log(msg1, num);
} else {
  console.log(msg2);
}
