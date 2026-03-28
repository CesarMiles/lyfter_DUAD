async function getData() {
  try {
    const response = await axios.get('https://api.restful-api.dev/objects');

    response.data.forEach((object) => {
      if (object.data) {
        const objectPropieties = Object.keys(object.data);
        console.log(`${object.name} (${objectPropieties.map((key) => {
          return `${key}: ${object.data[key]}`
        }).join(', ')})`)
      }
    });
  } catch (error) {
    console.log('There was an error', error.response.status, error.response.data);
  }
}

getData();

async function getDataById(id) {
  try {
    const response = await axios.get(`https://api.restful-api.dev/objects/${id}`);
    
    const dataPropieties = Object.keys(response.data.data);
    console.log(`${response.data.name} (${dataPropieties.map((key) => {
          return `${key}: ${response.data.data[key]}`}).join(', ')}`);
  } catch (error) {
    if (error.response.status === 404) {
      console.error(`Error ${error.response.status}.  ${JSON.stringify(error.response.data)}`)
    } else {
      console.error('Error completing the action', error.response.status, error.response.data)
    }
  }
}

getDataById('ff8081819d150699019d362bd3943e3f')

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
  } catch (error) {
    console.error('Error posting user', error.response.status, error.response.data)
  }
}

// postUser('Cesar M', 'Cesar@test.com', 'pass123', 'CR, Grecia')
// ID: ff8081819d150699019d362bd3943e3f

async function updateUserAddress (id, newAddress) {
  try {
    const updateBody = {
      'data' : {
        'address': newAddress
      }};

      const response = await axios.patch(`https://api.restful-api.dev/objects/${id}`, updateBody);
      console.log(response.data);
  } catch (error) {
    console.error('Error updating user', error.response.status, error.response.data)
  }
}

updateUserAddress('ff8081819d150699019d362bd3943e3f', 'Costa Rica')