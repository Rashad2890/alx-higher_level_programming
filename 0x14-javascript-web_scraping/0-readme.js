#!/usr/bin/node

// const request = require('request');
const fs = require('fs');
fs.readFile(process.argv[2], 'utf-8', (error, content) => {
  if (error) {
    console.log(error);
  } else {
    console.log(content);
  }
});
// const url = 'http://jsonbin.io/b/591a64459208345676e6a1ed';
/* request (c, function (error, response, body) {
 if (error) {
  console.log(error);
 } else {
  console.log(JSON.parse(body).likes[0]);
 }
});
*/
