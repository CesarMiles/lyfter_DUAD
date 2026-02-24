const phrase = "This is a string!";
let phraseArray = [];
let word = [];


for (const letter of phrase) {
  if (letter !== " "){
  word.push(letter);
  } else {
    phraseArray.push(word.join(''));
    word = [];
    }

  if (word.length > 0) {
      phraseArray.push(word.join(''));
  }

}

console.log(word)
console.log(phraseArray)
