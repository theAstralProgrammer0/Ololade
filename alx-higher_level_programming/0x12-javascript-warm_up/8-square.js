#!/usr/bin/node
const process = require('node:process');
const err = 'Missing size';
const size = parseInt(process.argv[2]);
const chr = 'X';

if (size) {
  let i = 0;
  while (i < size) {
    let j = 0;
    while (j < size) {
      process.stdout.write(chr);
      j += 1;
    }
    process.stdout.write('\n');
    i += 1;
  }
} else {
  console.log(err);
}
