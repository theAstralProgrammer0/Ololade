#!/usr/bin/node
const request = require('request');
const id = process.argv[2];

const url = 'https://swapi-api.alx-tools.com/api/films/' + id;

request.get({ url, json:true }, (response, body) => {
    console.log(body.body['title']);
  });
