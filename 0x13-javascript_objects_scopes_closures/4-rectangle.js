#!/usr/bin/node
module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
      this.print = function () {
        for (let i = 0; i < h; i++) {
          console.log('X'.repeat(w));
        }
      };
      this.rotate = function () {
        const tmp = h;
        h = w;
        w = tmp;
      };
      this.double = function () {
        h *= 2;
        w *= 2;
      };
    }
  }
};
