#!/usr/bin/node
const BaseSquare = require('./5-square');
const process = require('node:process');

class Square extends BaseSquare {
  constructor (size) {
    super(size, size);
  }

  charPrint (c = 'X') {
    let i = 0;
    while (i < this.height) {
      let j = 0;
      while (j < this.width) {
        process.stdout.write(c);
        j += 1;
      }
      process.stdout.write('\n');
      i += 1;
    }
  }
}

module.exports = Square;
