#!/usr/bin/node
const { argv } = require('process');
const fs = require('fs');

const path = argv[2];
fs.readFile(path, (err, data) => {
  if (err) throw err;
  console.log(data.toString());
});
