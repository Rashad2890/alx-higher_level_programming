#!/usr/bin/node

exports.esrever = function (list) {
  let count = [];
  for (let i = list.length - 1; i >= 0; i--) {
    count.push(list[i]);
  }
  return count;
};
