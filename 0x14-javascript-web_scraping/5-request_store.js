#!/usr/bin/node
// Script that gets the contents of a webpage and stores it in a file

const fS = require('fs');
const request = require('request');
request(process.argv[2]).pipe(fS.createWriteStream(process.argv[3]));
