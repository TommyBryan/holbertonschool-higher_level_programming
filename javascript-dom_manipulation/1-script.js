/*
Updates the text color of header to red #FF0000
When user clicks on the tag with the id red_header
*/

// Waits for page to load
document.addEventListener('DOMContentLoaded', function () {
  // Get the button with id red_header
  const button = document.getElementById('red_header');

  // Waits for user to click button to change the color of header text
  button.addEventListener('click', function () {
    document.querySelector('header').style.color = '#FF0000';
  });
});
