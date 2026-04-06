async function getDataById(id) {
  try {
    const response = await axios.get(`https://api.restful-api.dev/objects/${id}`);

    if(!response.data.data) {
      return {success: false, error: 'Response has no data'}; 
    }
    
    const dataPropieties = Object.keys(response.data.data);
    console.log(`${response.data.name} (${dataPropieties.map((key) => {
          return `${key}: ${response.data.data[key]}`}).join(', ')}`);
    
    return {success: true, data: response.data}
  } catch (error) {
      if (error.response) {
        if (error.response.status === 404) {
          console.error(`Error ${error.response.status}. ${JSON.stringify(error.response.data)}`);
        } else {
          console.log('There was an error', error.response.status, error.response.data);
        }
      } else {
        console.log('There was an error', error.message);
      }
      return { success: false, error: error.message };
    }
  }


getDataById('ff8081819d150699019d362bd3943e3f')

