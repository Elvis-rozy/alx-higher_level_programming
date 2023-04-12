#!/usr/bin/node
/*100-map.js*/
const theList = require('./100-data.js').list;
console.log(list);
const secondList = list.map((x, index) => x * index);
console.log(secondList);
