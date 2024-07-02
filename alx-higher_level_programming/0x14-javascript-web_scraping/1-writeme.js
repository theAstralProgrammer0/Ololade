#!/usr/bin/node
const fs = require('fs');
const path = process.argv[2];
const content = process.argv[3];

fs.writeFile(path, content, (err) => {
  if (err) throw err;
});
