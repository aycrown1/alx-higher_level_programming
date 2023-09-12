#!/usr/bin/node
let logme = 0;
exports.logMe = function (item) {
  console.log(logme + ': ' + item);
  logme++;
};
