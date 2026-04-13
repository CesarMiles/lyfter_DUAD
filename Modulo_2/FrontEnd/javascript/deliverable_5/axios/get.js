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
    return {success: true, data: response.data}
  } catch (error) {
    if (error.response) {
      console.log('There was an error', error.response.status, error.response.data);
    } else {
      console.log('There was an error', error.message);
    }
    return {success: false, error: error.message}; 
  }
}
