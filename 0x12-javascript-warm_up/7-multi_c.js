#!/usr/bin/node

const num = Math.floor(Number(process.argv[2]));
if (isNaN(num)) {
  console.log('Missing number of occurences');
} else {
  for (let index = 0; index < num; index++) {
    console.log('C is fun');
  }
}
