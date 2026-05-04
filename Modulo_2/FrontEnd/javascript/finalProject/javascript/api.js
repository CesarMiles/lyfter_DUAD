const userInstance = axios.create({
  baseURL: 'http://127.0.0.1:5000',
  timeout: 1000,
});

// Function to register an user using the backend created on BE module 
async function createUser(email, password) {
  try {
    const userBody = {
      'email' : email,
      'password' : password
    };

    const response = await userInstance.post('/register', userBody);
    return {success: true, data: response.data}
  } catch (error) {
    if (error.response) {
        console.log('There was an error', error.response.status, error.response.data);
      } else {
        console.log('There was an error', error.message);
      }
      return { success: false, error: error.message };
    } 
}