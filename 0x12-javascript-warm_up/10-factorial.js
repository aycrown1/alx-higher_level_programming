#!/usr/bin/node
// computes the factorial of x
function factorial (n) {
  if (n < 0) {
    return (-1);
  }
  if (n <= 1) {
    return (1);
  }
  return (n * factorial(n - 1));
}
const x = parseInt(process.argv[2], 10);
if (isNaN(x)) {
  console.log('1');
} else {
  console.log(factorial(x));
}
