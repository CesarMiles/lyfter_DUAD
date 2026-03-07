const fs = require('fs');


fs.readFile(__dirname + '/text1.txt', 'utf8', (err, data) => {
  if (err) {
    console.log("Error leyendo text1.txt:", err.message);
    return;
  }

  const textOneData = data.split('\n').map(word => word.trim());

  fs.readFile(__dirname + '/text2.txt', 'utf8', (err, data) =>{
    if (err) {
      console.log("Error leyendo text2.txt:", err.message);
      return;
    }

    const textTwoData = data.split('\n').map(word => word.trim());
    const hiddenMessage = textOneData.filter(word => {
      return textTwoData.includes(word);
    });
    console.log("Hidden Message:", hiddenMessage.join(' '));
    })
  })

