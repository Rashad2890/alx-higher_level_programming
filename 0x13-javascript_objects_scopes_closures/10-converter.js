#!/usr/bin/node
exports.converter = function (base) {
  return function (poop) {
    return poop.toString(base);
  };
};
