// Wait for the DOM to be ready
document.addEventListener("DOMContentLoaded", function () {
    // Fetch character data from the SWAPI API
    fetch("https://swapi-api.hbtn.io/api/people/5/?format=json")
      .then(response => response.json()) // Parse the response as JSON
      .then(data => {
        // Set the character name in the #character element
        document.querySelector("#character").textContent = data.name;
      })
      .catch(error => {
        console.error("Error fetching character:", error);
      });
  });
  