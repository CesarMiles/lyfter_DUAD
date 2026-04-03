const form = document.getElementById('form')
const nameInput = document.getElementById('name-input')
const emailInput = document.getElementById('email-input')
const passwordInput = document.getElementById('password-input')
const addressInput = document.getElementById('address-input')
const userIdInput = document.getElementById('user-id-input')
const errorMessage = document.getElementById('error-message')

form.addEventListener('submit', async (e) => {
  e.preventDefault()

  let errors = []

  if(nameInput) {
    
    errors = getSignupFormErrors(nameInput.value, emailInput.value, passwordInput.value, addressInput.value);
    if (errors.length === 0) {
      const userId = await postUser(nameInput.value, emailInput.value, passwordInput.value, addressInput.value);
      alert(`Your user Id is: ${userId}`);
      localStorage.setItem('userId', userId)
    }
  }
  else {
    errors = getLoginFormErrors(userIdInput.value, passwordInput.value);
  };

  if (errors.length > 0){
    errorMessage.innerText = errors.join(". ")
  }; 
})

function getSignupFormErrors(name, email, password, address) {
  let errors = []

  if (name === '' || name == null){
    errors.push('Name is required')
    nameInput.parentElement.classList.add('incorrect')
  }
  if (email === '' || email == null){
    errors.push('Email is required')
    emailInput.parentElement.classList.add('incorrect')
  }
  if (password === '' || password == null){
    errors.push('Password is required')
    passwordInput.parentElement.classList.add('incorrect')
  }
  if (address === '' || address == null){
    errors.push('Address is required')
    addressInput.parentElement.classList.add('incorrect')
  }
  return errors;
}

function getLoginFormErrors(userId, password) {
  let errors = []

  if (userId === '' || userId == null){
    errors.push('User Id is required')
    userIdInput.parentElement.classList.add('incorrect')
  }
  if (password === '' || password == null){
    errors.push('Password is required')
    passwordInput.parentElement.classList.add('incorrect')
  }
  return errors;
}


const allInputs = [nameInput, emailInput, passwordInput, addressInput, userIdInput].filter(input => input != null)

allInputs.forEach(input => {
  input.addEventListener('input', () => {
    if(input.parentElement.classList.contains('incorrect')){
      input.parentElement.classList.remove('incorrect');
      errorMessage.innerText = ''
    }
  })
})

async function postUser(name, email, password, address) {
  try {
    const userBody = {
      'name': name,
      'data': {
        'email' : email,
        'password' : password,
        'address' : address
      }
    };

    const response = await axios.post('https://api.restful-api.dev/objects', userBody);
    return response.data.id
  } catch (error) {
    return error.response.data
  }
}
