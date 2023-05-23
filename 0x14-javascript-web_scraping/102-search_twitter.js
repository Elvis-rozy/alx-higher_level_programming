#!/usr/bin/node

const base_64 = require('base-64');
const req = require('request');
const utf_8 = require('utf8');

function search (bearer) {
  const url = 'https://api.twitter.com/1.1/search/tweets.json';
  req.get({
    url,
    headers: {
      Authorization: `Bearer ${bearer}`
    },
    qs: {
      q: process.argv[4],
      count: '5'
    }
  }, (err, res, body) => {
    if (!err) {
      const tweets = JSON.parse(body).statuses;
      tweets.forEach((tweet) => console.log(`[${tweet.id}] ${tweet.text} by ${tweet.user.name}`));
    }
  });
}

const promise = new Promise((resolve, reject) => {
  const token = utf_8.decode(base_64.encode(`${process.argv[2]}:${process.argv[3]}`));
  const url = 'https://api.twitter.com/oauth2/token';
  req.post({
    url,
    headers: {
      Authorization: `Basic ${token}`,
      'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8'
    },
    form: {
      grant_type: 'client_credentials'
    }
  }, (err, res, body) => {
    if (!err) {
      resolve(JSON.parse(body).access_token);
    }
  });
});
promise.then(
  result => search(result),
  err => console.log(err)
);
