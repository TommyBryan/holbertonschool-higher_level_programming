document.addEventListener('DOMContentLoaded', () => {
  // Select the element with id 'update_header'
  const updateHeader = document.getElementById('update_header');

  // Select the <header> element
  const headerElement = document.querySelector('header');

  // Add click event listener
  updateHeader.addEventListener('click', () => {
    // Change the header text
    headerElement.textContent = 'New Header!!!';
  });
});
