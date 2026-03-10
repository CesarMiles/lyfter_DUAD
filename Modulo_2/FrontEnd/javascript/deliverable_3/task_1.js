const isEven = () => {
  console.log("The number is even!");
}

const isOdd = () => {
  console.log("The number is odd!")
}

function numberCheck (number, isEven, isOdd) {
  if (number % 2 === 0 ) {
    isEven()
  }
  else {
    isOdd()
  }
}

numberCheck(3, isEven, isOdd)