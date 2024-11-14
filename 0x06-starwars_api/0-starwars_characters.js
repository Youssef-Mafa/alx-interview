#!/usr/bin/node

const request = require('request');
const movieID = process.argv[2];

// Function to get characters in the correct order using Promises
const getCharactersInOrder = async () => {
  try {
    const movieResponse = await new Promise((resolve, reject) => {
      request.get(`https://swapi-api.hbtn.io/api/films/${movieID}/`, (err, res, body) => {
        if (err) return reject(err);
        try {
          resolve(JSON.parse(body).characters);
        } catch (parseError) {
          reject(parseError);
        }
      });
    });

    // Sequentially fetch and log each character name
    for (const characterURL of movieResponse) {
      const characterName = await new Promise((resolve, reject) => {
        request.get(characterURL, (err, res, body) => {
          if (err) return reject(err);
          try {
            resolve(JSON.parse(body).name);
          } catch (parseError) {
            reject(parseError);
          }
        });
      });
      console.log(characterName);
    }
  } catch (error) {
    console.error(error);
  }
};

// Call the function to execute the process
getCharactersInOrder();

