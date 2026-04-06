async function postUser(name, email, password, address) {
  try {
    const userBody = {
      'name': name,
      'data': {
        'email': email,
        'password': password,
        'address': address
      }};
      
    const response = await axios.post('https://api.restful-api.dev/objects', userBody);
    console.log(response.data);

    return {success: true, data: response.data};
  } catch (error) {
      if (error.response) {
        console.log('There was an error', error.response.status, error.response.data);
      } else {
        console.log('There was an error', error.message);
      }
      return { success: false, error: error.message };
    }
}

// postUser('Cesar M', 'Cesar@test.com', 'pass123', 'CR, Grecia')
// ID: ff8081819d150699019d362bd3943e3f
