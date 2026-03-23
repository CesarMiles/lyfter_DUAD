async function getData(){
  try {
    const fetchData = await fetch('https://api.restful-api.dev/objects');
    const data =  await fetchData.json();
    // console.log(data);
    data.forEach((object) => {
      if (object.data) {
        const objectPropieties = Object.keys(object.data);
        console.log(`${object.name} (${objectPropieties.map((key) => {
          return `${key}: ${object.data[key]}`
      }).join(', ')})`)
    }});
  } catch (error) {
    console.log('There was an error', {error});
  }}


getData();