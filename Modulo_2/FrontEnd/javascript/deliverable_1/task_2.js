// Solucion usando For
const numberArray = [1, 2, 3, 4, 5, 6, 7 ,8]
let evenNumber = []
for (const number of numberArray) {
  if (number % 2 === 0) {
    evenNumber.push(number); 
  }
}

console.log(evenNumber);

// Solucion usando Filter

const evenNumberTwo = numberArray.filter((number)=> {if (number % 2 === 0){return number;}});



console.log(evenNumberTwo)