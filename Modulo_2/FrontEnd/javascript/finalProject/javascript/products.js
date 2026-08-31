const productContainer = document.getElementById('product-container')
const productImages = {
  'cat food': 'cat-food.png',
  'dog food': 'dog-food.png',
  'dog leash': 'leash.png',
}
const fallbackImage = 'psyduck.png'

if (localStorage.getItem('authToken') === '' || localStorage.getItem('authToken') == null) {
  window.location.href = "login.html";
} 


// function to get available productos 
async function availableProducts() {
  const response = await getProducts();
  const available = response.data.filter((product) => product.stock > 0 );
  const cards = available.map(product => `<div class="product-card">
        <img src="images/${productImages[product.product_name] || fallbackImage}" alt="${product.product_name}">
        <div class="product-name-price">
          <p>${product.product_name}</p>
          <p>$${product.product_price}</p>
        </div>
        <button data-product-id="${product.product_id}" type="button">Add to cart</button>
      </div>`);
  productContainer.innerHTML = cards.join('');
}

availableProducts()

productContainer.addEventListener('click', (event) => {
  const rawId = event.target.dataset.productId;
  if (!rawId) return;

  const productId = Number(rawId);
  const cart = JSON.parse(localStorage.getItem('cart')) || [];
  
  const item = cart.find((p) => p.product_id === productId);

  if (item) {
    item.quantity++;
  } else {
    cart.push({ product_id: productId, quantity: 1});
  }

  localStorage.setItem('cart', JSON.stringify(cart));
})