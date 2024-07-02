#!/usr/bin/node
const { argv } = require('node:process');
const msg = 'No argument';

if (!argv[2]) {
  console.log(msg);
} else {
  console.log(argv[2]);
}
