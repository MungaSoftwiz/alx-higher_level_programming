#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
const filepath = process.argv[3];
const fs = require('fs');

request(url, function (error, response, body) {
  if (error) {
    console.error(error);
  }

  fs.writeFile(filepath, body, 'utf-8', (error) => {
    if (error) {
      console.error(error);
    }
  });
});
