const productContainer = document.getElementById('product-container')

if (localStorage.getItem('authToken') === '' || localStorage.getItem('authToken') == null) {
  window.location.href = "login.html";
} 
