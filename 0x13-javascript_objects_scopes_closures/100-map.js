#!/usr/bin/node
const theList = require('./100-data.js').list;
console.log(theList);
const secondList = theList.map((x, index) => x * index);
console.log(secondList);
