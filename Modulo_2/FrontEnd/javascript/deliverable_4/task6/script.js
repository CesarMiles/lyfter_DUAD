const wordVery = new Promise((resolve, reject) => {
  setTimeout(() => resolve('very'), 3000)
})

const wordDogs = new Promise((resolve, reject) => {
  resolve('dogs')
})

const wordCute = new Promise((resolve, reject) => {
  setTimeout(() => resolve('cute'), 4000)
})

const wordAre = new Promise((resolve, reject) => {
  setTimeout(() => resolve('are'), 2000)
})

const wordArray = []

const tracked = [wordVery, wordDogs, wordCute, wordAre].map((p) =>
  p.then((word) => wordArray.push(word))
)

Promise.all(tracked).then(() => {
  console.log(wordArray.join(' '))
})
