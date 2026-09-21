const form = document.getElementById('form')
const emailInput = document.getElementById('email-input')
const passwordInput = document.getElementById('password-input')
const errorMessage = document.getElementById('error-message')
const pageTitle = document.title


form.addEventListener('submit', async (e) => {
  e.preventDefault()

  let errors = []

  errors = getFormErrors(emailInput.value, passwordInput.value);
  if (errors.length === 0 ){
    let userData 
    if(pageTitle === 'Login') {
      userData = await login(emailInput.value, passwordInput.value)
    }
    else {
      userData = await createUser(emailInput.value, passwordInput.value)
    }

    if (userData.success == false){
      errors.push(userData.error)
    }
    else {
      window.location.href = "profile.html";
    }
  };

  if (errors.length > 0){
    errorMessage.innerText = errors.join(". ")
  };

})

function getFormErrors(email, password) {
  let errors = []

  if (email === '' || email == null){
    errors.push('Email is required')
    emailInput.parentElement.classList.add('incorrect')
  }

  if (password === '' || password == null){
    errors.push('Password is required')
    passwordInput.parentElement.classList.add('incorrect')
  }
  return errors;
}