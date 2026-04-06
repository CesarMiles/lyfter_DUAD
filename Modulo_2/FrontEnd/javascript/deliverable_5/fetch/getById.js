async function getDataById(id) {
  try {
    const fetchData = await fetch(`https://api.restful-api.dev/objects/${id}`);
    if (fetchData.status === 404) {
      return {success: false, error: `User not found (status: ${fetchData.status})`};
    };

    const data = await fetchData.json();
    if (!data.data){
      return {success: false, error: 'Response has no data'};
    }

    const dataPropieties = Object.keys(data.data)
    console.log(`${data.name} (${dataPropieties.map((key) => {
          return `${key}: ${data.data[key]}`}).join(', ')}`)
    return {success: true, data: data}

  } catch (error) {
    console.error('Error getting user', error)
    return {success: false, error: error.message};
  }
}

getDataById('ff8081819d150699019d2293768e17b02222')
// Valid ID: ff8081819d150699019d2293768e17b0
