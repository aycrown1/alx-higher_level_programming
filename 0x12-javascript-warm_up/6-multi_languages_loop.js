#!/usr/bin/node
// prints 'lang  is desc'
const langs = ['C', 'Python', 'Javascript'];
const desc = ['fun', 'cool', 'amazing'];
let i;
for (i in langs) {
  console.log(langs[i] + ' is ' + desc[i]);
}
