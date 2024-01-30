#!/usr/bin/node

const request = require('request');
const url = 'http://swapi.co/api/films/' + process.argv[2];
request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    let data = JSON.parse(body).characters;
    // console.log(data);
    let order = [];
    for (let i = 0; i < data.length; i++) {
      order.push(new Promise(function (resolve, reject) {
        request.get(data[i], function (error, response, body) {
          if (error) {
            reject(error);
          }
          resolve(JSON.parse(body).name);
        });
      }));
      // console.log(order[i]);
    }
    Promise.all(order).then(character => {
      for (let j = 0; j < character.length; j++) {
        console.log(character[j]);
      }
      // can shorten above 2 lines into this 1 line below
      // character.forEach(person => console.log(person));
    });
    // console.log(order);
  }
});
