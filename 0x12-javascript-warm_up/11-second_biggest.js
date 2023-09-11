#!/usr/bin/node
// finds the second biggest int in a list of args

if (process.argv.length <= 2) {
  console.log('0');
} else {
  let max = 0;
  let pent = 0;

  for (let x = 2; x < process.argv.length; x++) {
    if (process.argv[x] > max) {
      max = process.argv[x];
    }
  }

  for (let x = 2; x < process.argv.length; x++) {
    if (process.argv[x] > pent && process.argv[x] < max) {
      pent = process.argv[x];
    }
  }

  console.log(pent);
}
