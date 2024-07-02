#!/usr/bin/node
const { argv } = require('node:process');
const conj = ' is ';

console.log(argv[2] + conj + argv[3]);
