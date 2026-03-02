const tempCelsius = [36, 37, 37.2]
const tempFarenheit = tempCelsius.map((temp) =>{
  return (temp*1.8) + 32 
})

console.log(tempFarenheit)