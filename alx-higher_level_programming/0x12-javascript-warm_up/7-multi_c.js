#!/usr/bin/node
const { argv } = require('node:process');
const err = 'Missing number of occurrences';
const msg = 'C is fun';
const num = argv[2];

if (parseInt(num)) {
  let i = 0;
  while (i < num) {
    console.log(msg);
    i += 1;
  }
} else {
  console.log(err);
}
