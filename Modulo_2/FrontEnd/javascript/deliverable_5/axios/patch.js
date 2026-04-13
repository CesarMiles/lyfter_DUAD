async function updateUserAddress (id, newAddress) {
  try {
    const updateBody = {
      'data' : {
        'address': newAddress
      }};

      const response = await axios.patch(`https://api.restful-api.dev/objects/${id}`, updateBody);
      console.log(response.data);
      return {success: true, data: response.data} 
  } catch (error) {
    if (error.response) {
      console.error('Error updating user', error.response.status, error.response.data)
    } else {
      console.log('There was an error', error.message);
    }
    return {success: false, error: error.message}; 
  }
}

updateUserAddress('ff8081819d150699019d362bd3943e3f', 'Costa Rica')