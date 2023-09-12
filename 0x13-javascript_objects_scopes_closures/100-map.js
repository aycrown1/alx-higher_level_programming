#!/usr/bin/node
let area = require('./100-data').list;
let newArea = area.map(function (x, idx) {
  return x * idx;
});
console.log(area);
console.log(newArea);
