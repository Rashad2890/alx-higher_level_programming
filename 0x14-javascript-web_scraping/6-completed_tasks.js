#!/usr/bin/node
const request = require('request');
request(process.argv[2], function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    let data = JSON.parse(body);

    let dict = {};
    for (let i = 0; i < data.length; i++) {
      let user = data[i];

      if (user.completed === true) {
        if (user.userId in dict) {
          dict[user.userId] += 1;
        } else {
          dict[user.userId] = 1;
        }
      }

      /*
if (dict[user.userId] === undefined) {
dict[user.userId] = 0;
}
if (user.completed === true) {
dict[user.userId]++;
}
*/
    }
    console.log(dict);
  }
});
