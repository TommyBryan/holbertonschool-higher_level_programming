// Wait until the DOM is fully loaded
document.addEventListener('DOMContentLoaded', () => {
  // API endpoint
  const apiUrl = 'https://swapi-api.hbtn.io/api/people/5/?format=json';

  // Fetch data from the API
  fetch(apiUrl)
    .then(response => {
      if (!response.ok) {
        throw new Error(`HTTP error! Status: ${response.status}`);
      }
      return response.json(); // Parse JSON from response
    })
    .then(data => {
      // Update the div with id 'character' with the name from the response
      document.getElementById('character').textContent = data.name;
    })
    .catch(error => {
      console.error('Fetch error:', error);
    });
});
