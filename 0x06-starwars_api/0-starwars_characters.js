#!/usr/bin/node

const request = require('request');
const baseurl = 'https://swapi-api.hbtn.io/api/films/';
const urlMovie = baseurl + process.argv[2];

request(urlMovie, async function (error, response, body) {
  const base = [];

  if (error) {
    console.log(error);
  }
  const film = JSON.parse(body);
  for (let i = 0; i < film.characters.length; i++) {
    base.push(myCharacter(film.characters[i]));
  }

  let actors = await Promise.all(base);

  actors = actors.map((actor) => JSON.parse(actor).name);
  actors.forEach((actor) => console.log(actor));
});

function myCharacter (thisCharacter) {
  return new Promise((resolve, reject) => {
    request(thisCharacter, function (error, response, body) {
      if (error) {
        reject(error);
      }
      resolve(body);
    });
  });
}
