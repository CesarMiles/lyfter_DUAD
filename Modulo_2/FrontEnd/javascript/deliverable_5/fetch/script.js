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
  } catch (error) {
    console.log('There was an error', {error});
  }}

getData();

async function getDataById(id) {
  try {
    const fetchData = await fetch(`https://api.restful-api.dev/objects/${id}`);
    if (fetchData.status === 404) {
      throw new Error(`HTTP error. Status: ${fetchData.status}, User not found`);
    };

    const data = await fetchData.json();

    const dataPropieties = Object.keys(data.data)
    console.log(`${data.name} (${dataPropieties.map((key) => {
          return `${key}: ${data.data[key]}`}).join(', ')}`)

  } catch (error) {
    console.error('Error getting user', error)
  }
}

getDataById('ff8081819d150699019d2293768e17b0')
// Valid ID: ff8081819d150699019d2293768e17b0

// async function postUser(name, email, password, address) {
//   try {
//     const userBody = {
//         'name': name,
//         'data': {
//           'email': email,
//           'password': password,
//           'address': address
//         }}
//     const response = await fetch('https://api.restful-api.dev/objects', {
//       method: 'POST',
//       headers: {
//         'Content-Type': 'application/json',
//       },
//       body: JSON.stringify(userBody)
//     });
//     if (!response.ok) {
//       throw new Error(`HTTP error. Status: ${response.status}`);
//     };

//     const data = await response.json();
//     console.log(data);
//   } catch (error) {
//     console.error('Error creating post', error)
//   }
  
// }

// postUser('Cesar M', 'Cesar@test.com', 'pass123', 'CR, Grecia')