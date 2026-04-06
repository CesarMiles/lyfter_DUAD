async function updateUserAddress (id, newAddres) {
  try {
    const updateBody = {
      'data' : {
        'address': newAddres
      }};

    const response = await fetch(`https://api.restful-api.dev/objects/${id}`, {
      method: 'PATCH',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(updateBody)
    });

    if (response.status === 404) {
      return {success: false, error: 'Error 404. User cant be found'};
    };

    if (!response.ok) {
      return {success: false, error: 'Error updating user'};
    };

    const data = await response.json();
    console.log(data);
    return {success: true, data: data}
  } catch (error){
    console.error('Error creating post', error)
    return {success: false, error: error.message};
  }
}

updateUserAddress('ff8081819d150699019d2293768e17b0', 'Costa Rica')