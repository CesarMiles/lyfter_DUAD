const userId = localStorage.getItem('userId')
const userName = document.getElementById('name')
const userEmail = document.getElementById('email')
const userPassword = document.getElementById('password')
const userAddress = document.getElementById('address')
const changeButton = document.getElementById('change-button')
const logoutButton = document.getElementById('logout')
let isEditing = false;

// Check if user is logged in
if (userId === '' || userId == null) {
  window.location.href = "login.html";
} else {
  getDataById(userId)
}

async function getDataById(id) {
  try {
    const response = await axios.get(`https://api.restful-api.dev/objects/${id}`)

    userName.innerHTML = response.data.name;
    userEmail.innerHTML = response.data.data['email'];
    userPassword.innerHTML = response.data.data['password'];
    userAddress.innerHTML = response.data.data['address']
  } catch (error) {
    alert(`There has been an error. ${error}`)
  };
};

async function changePassword(id, newPassword) {
  try {
    const updateBody = {
      'data' : {
        'email' : userEmail.innerHTML,
        'password' : newPassword,
        'address' : userAddress.innerHTML
      }};
    
    const response = await axios.patch(`https://api.restful-api.dev/objects/${id}`, updateBody);
    alert('Password has been updated')
  } catch (error) {
    alert(`There has been an error updating the password. ${error}`);
  };
};


changeButton.addEventListener('click', async (e) => {
  if (isEditing == false ) {
    const newPassInput = document.createElement('input');
    newPassInput.id = 'password-input';
    newPassInput.placeholder = 'Enter new password';
    newPassInput.type = 'password';
  
    userPassword.replaceWith(newPassInput);
  
    changeButton.innerHTML = 'Submit Change';
    isEditing = true;
  } else {
    const newPass = document.getElementById('password-input');
    await changePassword(userId, newPass.value);
    changeButton.innerHTML = 'Change Password';
    isEditing = false;
    newPass.replaceWith(userPassword)
    getDataById(userId)
  }

})


logoutButton.addEventListener('click', (e) => {
  localStorage.removeItem('userId')
})