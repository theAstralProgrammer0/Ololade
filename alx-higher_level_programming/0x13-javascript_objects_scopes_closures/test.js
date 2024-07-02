#!/usr/bin/node
const dict = require('./101-data.js').dict;
let uniqueList = new Set(Object.values(dict));

uniqueList = Array.from(uniqueList);
const newDict = {};
for (const element of uniqueList) {
  const valueArray = [];
  for (const key of Object.keys(dict)) {
    if (dict[key] === element) {
      valueArray.push(key);
    }
    newDict[element] = valueArray;
  }
}
console.log(newDict);
*/
