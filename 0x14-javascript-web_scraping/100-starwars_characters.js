#!/usr/bin/node
// Script that prints all characters of a Star Wars movie

const req = require('request');
const fm = process.argv[2];
const url = `https://swapi-api.hbtn.io/api/films/${fm}`;
req(url, (err, res, body) => {
  if (!err) {
    const characters = JSON.parse(body).characters;
    characters.forEach((character) => {
      req(character, function (err, res, body) {
        if (!err) {
          console.log(JSON.parse(body).name);
        }
      });
    });
  }
});
