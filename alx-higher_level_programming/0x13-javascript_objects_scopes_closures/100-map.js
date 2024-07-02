#!/usr/bin/node
const { list } = require('./100-data');

const newList = list.map((x, i) => i * x);

console.log(list);
console.log(newList);
