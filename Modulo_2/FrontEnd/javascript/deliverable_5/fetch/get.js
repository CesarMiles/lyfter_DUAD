async function getData(){
  try {
    const fetchData = await fetch('https://api.restful-api.dev/objects');
    const data =  await fetchData.json();

    data.forEach((object) => {
      if (object.data) {
        const objectPropieties = Object.keys(object.data);
        console.log(`${object.name} (${objectPropieties.map((key) => {
          return `${key}: ${object.data[key]}`
      }).join(', ')})`)
    }});
    return {success: true, data: data}
  } catch (error) {
    console.log('There was an error', {error});
    return {success: false, error: error.message};
  }}

getData();
