#!/usr/bin/node
const request = require('request');
const url = process.argv[2];

request(url, function (err, response, body) {
  if (err) {
    console.log(err);
  }
  let count = 0;
  for (const result of JSON.parse(body).results) {
    for (const wedgeUrl of result.characters) {
      if (wedgeUrl.includes(18)) {
        count++;
      }
    }
  }
  console.log(count);
});
