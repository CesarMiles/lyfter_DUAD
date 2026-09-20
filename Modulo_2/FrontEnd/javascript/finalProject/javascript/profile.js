const userEmailProfile =  document.getElementById('user-email')
const logoutButton = document.getElementById('logout-btn')
const userRole = document.getElementById('role')
const changeButton = document.getElementById('change-button')
const userPassword = document.getElementById('password')
let isEditing = false;

if (localStorage.getItem('authToken') === '' || localStorage.getItem('authToken') == null) {
  window.location.href = "login.html";
} else {
  userData() 
}

async function userData() {
  try {
    const response = await getMe()

    if (response.success === true) {
      userEmailProfile.innerHTML = response.data.email;
      userRole.innerHTML = response.data.role;
    } else {
      window.location.href = "login.html";
    };
  } catch (error) {
    alert('There has been an error.')
    window.location.href = "login.html";
  }
}

logoutButton.addEventListener('click', (e) => {
  localStorage.removeItem('authToken');
  window.location.href = "login.html"
})

changeButton.addEventListener('click', async (e) => {
  if (isEditing === false) {
    const newPassInput = document.createElement('input');
    newPassInput.id = 'password-input';
    newPassInput.placeholder = 'Enter new password';
    newPassInput.type = 'password';
  
    userPassword.replaceWith(newPassInput);
  
    changeButton.innerHTML = 'Submit Change';
    isEditing = true;
  } else {
    const newPass = document.getElementById('password-input');
    if (newPass.value.trim() === '') {
      alert('The new password cannot be a blank space')
      return
    }

    const response = await changePassword(newPass.value);
    if (response.success === true) {
      alert('Password updated')
    } else {
      alert('There was an error with the update please try again')
    }
    changeButton.innerHTML = 'Change Password';
    isEditing = false;
    newPass.replaceWith(userPassword)
    
  }
})