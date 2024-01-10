#!/usr/bin/node
const BaseSquare = require('./5-square.js');

module.exports = class Square extends BaseSquare {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (c === undefined) {
      this.print();
    } else {
      for (let index = 0; index < this.width; index++) {
        console.log(c.repeat(this.height));
      }
    }
  }
};
