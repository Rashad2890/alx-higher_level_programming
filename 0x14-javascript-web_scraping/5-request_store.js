#!/usr/bin/node

const request = require('request');
const fs = require('fs');
const url = process.argv[2];
request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    let data = body;
    fs.writeFile(process.argv[3], data, 'utf-8');
  }
});
