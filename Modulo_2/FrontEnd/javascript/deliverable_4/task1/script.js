async function getUser(){
  const response = await fetch('https://reqres.in/api/users/2', {
  headers: {
    'x-api-key' : 'reqres_c2caf34564d8464abaa2b7f0063bd674'}
  });
  const data = await response.json();
  console.log(data);
}

getUser();