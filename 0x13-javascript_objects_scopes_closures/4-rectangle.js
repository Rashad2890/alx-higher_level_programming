#!/usr/bin/node

module.exports = class Rectangle {
  constructor (w, h) {
    if (w <= 0 || h <= 0 || arguments.length < 2 || isNaN(w) || isNaN(h)) {

    } else {
      this.width = w;
      this.height = h;
    }
  }
  print () {
    for (let i = 0; i < this.height; i++) {
      console.log('X'.repeat(this.width));
    }
  }
  rotate () {
    let temp = this.width;
    this.width = this.height;
    this.height = temp;
  }
  double () {
    this.width = this.width * 2;
    this.height = this.height * 2;
  }
};
