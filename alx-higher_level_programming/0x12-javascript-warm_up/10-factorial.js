#!/usr/bin/node
const process = require('node:process');

function fact (n) {
  if (!n) {
    return (1);
  }
  return (n * fact(n - 1));
}

console.log(fact(parseInt(process.argv[2])));
