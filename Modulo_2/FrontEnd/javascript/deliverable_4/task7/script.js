fetch('https://reqres.in/api/users/2', {
  headers: {
    'x-api-key' : 'reqres_c2caf34564d8464abaa2b7f0063bd674'
  }
  }).then(res => {
    if (!res.ok) {
      throw new Error('User not found');
    } else {
      return res.json()
    }
  }).then(data => console.log(data))
  .catch(error => console.log(error.message))


  fetch('https://reqres.in/api/users/23', {
  headers: {
    'x-api-key' : 'reqres_c2caf34564d8464abaa2b7f0063bd674'
  }
  }).then(res => {
    if (!res.ok) {
      throw new Error('User not found');
    } else {
      return res.json()
    }
  }).then(data => console.log(data))
  .catch(error => console.log(error.message))
