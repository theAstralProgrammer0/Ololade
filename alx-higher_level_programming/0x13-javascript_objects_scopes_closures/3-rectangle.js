#!/usr/bin/node
const process = require('node:process');

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    const chr = 'X';
    let i = 0;
    while (i < this.height) {
      let j = 0;
      while (j < this.width) {
        process.stdout.write(chr);
        j += 1;
      }
      process.stdout.write('\n');
      i += 1;
    }
  }
}

module.exports = Rectangle;
