export default function handleResponseFromAPI(promise) {
  return Promise
    .then(() => ({
      status: 200,
      body: 'success',
    }))
    .then((response) => {
      console.log('Got a response from the API');
      return response;
    })
    .catch(() => new Error());
}
