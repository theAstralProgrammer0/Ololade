#!/usr/bin/node
const process = require('node:process');
const fs = require('fs');

const fileA = String(process.argv[2]);
const fileB = String(process.argv[3]);
const fileC = String(process.argv[4]);

fs.readFile(fileA, 'utf8', (err, data) => {
  if (err) {
    console.error('An error occured while reading', err);
    return;
  }
  processDataA(data);
});

function processDataA (dA) {
  fs.writeFile(fileC, dA, (err) => {
    if (err) {
      console.error('An error occured while writing', err);
    }
  });
}

fs.readFile(fileB, 'utf8', (err, data) => {
  if (err) {
    console.error('An error occured while reading', err);
    return;
  }
  processDataB(data);
});

function processDataB (dB) {
  fs.appendFile(fileC, dB, (err) => {
    if (err) {
      console.error('An error occured while writing', err);
    }
  });
}
