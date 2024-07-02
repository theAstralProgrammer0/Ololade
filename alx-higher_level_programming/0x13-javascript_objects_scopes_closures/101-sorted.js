#!/usr/bin/node
const { dict } = require('./101-data');

const newDict = Object.entries(dict).reduce((acc, [id, occ]) => {
  if (!acc[occ]) {
    acc[occ] = [];
  }
  acc[occ].push(id);
  return (acc);
}, {});
console.log(newDict);
