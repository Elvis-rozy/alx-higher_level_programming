#!/usr/bin/node
// Script that computes the number of tasks completed by user id.

const argmts = process.argv;
let requestURL = args[2];
let request = require('request');
request(requestURL, function (error, response, body) {
  if (error) {
    console.log('error:', error);
  } else {
    let todo = JSON.parse(body);
    let dash = {};
    for (let i = 0; i < todo.length; i++) {
      let status = (todo[i]['completed']);
      let key = todo[i]['userId'].toString();
      if (status) {
        if (dash[key]) {
          dash[key]++;
        } else {
          dash[key] = 1;
        }
      }
    }
    console.log(dash);
  }
});
