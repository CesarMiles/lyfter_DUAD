const form = document.getElementById('userForm');
const userInput = document.getElementById('userId');
const resultDiv = document.getElementById('result');

form.addEventListener('submit',  async (event) => {
  event.preventDefault();

  const userId = userInput.value;
  try {
    const response = await fetch(`https://reqres.in/api/users/${userId}`, {
      headers: {'x-api-key': 'reqres_c2caf34564d8464abaa2b7f0063bd674'}
    });

    if (!response.ok) {
      throw new Error('Usuario no encontrado');
    }

    const data = await response.json();
    
    
    resultDiv.innerHTML = `
      <strong>${data.data.first_name} ${data.data.last_name}</strong><br>
      Email: ${data.data.email}
    `;
    resultDiv.className = 'result success';

  } catch (err) {
    resultDiv.innerHTML = err.message; 
    resultDiv.className = 'result error';
  }
});