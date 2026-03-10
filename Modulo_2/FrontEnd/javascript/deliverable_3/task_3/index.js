const text = document.querySelector('.text-container p')
const button = document.querySelector('.change-button')
const colorArray = ["red", "blue", "green", "yellow", "cyan", "pink"]

button.addEventListener('click', () => {
  const randomIndex = Math.floor(Math.random() * colorArray.length);
  const randomColor = colorArray[randomIndex];
  text.style.backgroundColor = randomColor;
})