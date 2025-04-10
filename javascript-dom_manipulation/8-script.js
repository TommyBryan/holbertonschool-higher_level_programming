document.addEventListener("DOMContentLoaded", function () {
    // Fetch the translation from the API
    fetch("https://hellosalut.stefanbohacek.dev/?lang=fr")
      .then(response => {
        if (!response.ok) {
          throw new Error("Network response was not ok");
        }
        return response.json();
      })
      .then(data => {
        // Display the translated "hello" in the element with id "hello"
        document.querySelector("#hello").textContent = data.hello;
      })
      .catch(error => {
        console.error("Error fetching translation:", error);
      });
  });
