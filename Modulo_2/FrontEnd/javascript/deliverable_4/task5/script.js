const promiseOne = fetch(`https://pokeapi.co/api/v2/pokemon/${Math.floor(Math.random() * 10)+1}`)
const promiseTwo = fetch(`https://pokeapi.co/api/v2/pokemon/${Math.floor(Math.random() * 10)+1}`)
const promiseThree = fetch(`https://pokeapi.co/api/v2/pokemon/${Math.floor(Math.random() * 10)+1}`)


Promise.any([promiseOne, promiseTwo, promiseThree])
  .then(message => {
    return message.json();
  })
  .then((data) => {
    console.log(data.name)
  });
