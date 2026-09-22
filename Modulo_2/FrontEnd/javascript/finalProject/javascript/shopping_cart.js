const userEmailProfile =  document.getElementById('user-email')
const logoutButton = document.getElementById('logout-btn')

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
    } else {
      window.location.href = "login.html";
    };
  } catch (error) {
    alert('There has been an error.')
    window.location.href = "login.html";
  }
}
