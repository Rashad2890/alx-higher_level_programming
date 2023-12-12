#!/usr/bin/node

module.exports = class Rectangle {
  constructor (w, h) {
    if (w <= 0 || h <= 0 || arguments.length < 2 || isNaN(w) || isNaN(h)) {

    } else {
      this.width = w;
      this.height = h;
    }
  }
};
