async function postUser(name, email, password, address) {
  try {
    const userBody = {
        'name': name,
        'data': {
          'email': email,
          'password': password,
          'address': address
        }}
    const response = await fetch('https://api.restful-api.dev/objects', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(userBody)
    });
    if (!response.ok) {
      return {success: false, error: 'Failed to post user'};
    };

    const data = await response.json();
    console.log(data);
    return {success: true, data: data}

  } catch (error) {
    console.error('Error creating post', error);
    return {success: false, error: error.message};
  }
  
}

postUser('Cesar M', 'Cesar@test.com', 'pass123', 'CR, Grecia')
