async function getUser(){
  try {
    const response = await fetch('https://reqres.in/api/users/23', {
    headers: {'x-api-key' : 'reqres_c2caf34564d8464abaa2b7f0063bd674'}
    });

    if (!response.ok) {
      throw new Error('User not found');
    }

    const data = await response.json();
    console.log(data);

  } catch (err) {
    console.log(err)
  }
  
}

getUser();