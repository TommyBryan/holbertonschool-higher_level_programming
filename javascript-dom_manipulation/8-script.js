document.addEventListener('DOMContentLoaded', () => {
  // Define the API URL
  const url = 'https://hellosalut.stefanbohacek.dev/?lang=fr';

  // Fetch from the API
  fetch(url)
    .then(response => {
      if (!response.ok) {
        throw new Error(`HTTP error! Status: ${response.status}`);
      }
      return response.json(); // Parse the JSON response
    })
    .then(data => {
      // Set the translated "hello" into the div with id="hello"
      document.getElementById('hello').textContent = data.hello;
    })
    .catch(error => {
      console.error('Fetch error:', error);
    });
});
