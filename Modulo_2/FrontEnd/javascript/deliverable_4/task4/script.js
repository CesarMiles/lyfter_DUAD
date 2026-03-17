const promiseOne = fetch(`https://pokeapi.co/api/v2/pokemon/${Math.floor(Math.random() * 10)+1}`)
const promiseTwo = fetch(`https://pokeapi.co/api/v2/pokemon/${Math.floor(Math.random() * 10)+1}`)
const promiseThree = fetch(`https://pokeapi.co/api/v2/pokemon/${Math.floor(Math.random() * 10)+1}`)


Promise.all([promiseOne, promiseTwo, promiseThree])
  .then((messages) => {
    return Promise.all(messages.map(res => res.json()));
  })
  .then((data) => {
    data.forEach(pokemon => console.log(pokemon.name))
  });
