//  wait for page to load
document.addEventListener('DOMContentLoaded', function () {
  //  toggle_header as button
  const toggleHeader = document.getElementById('toggle_header');
  // header element
  const header = document.querySelector('header');

  // Click event listener
  toggleHeader.addEventListener('click', function () {
    // If header has class 'red', switch to 'green'
    if (header.classList.contains('red')) {
      header.classList.remove('red');
      header.classList.add('green');
    } else if (header.classList.contains('green')) {
      header.classList.remove('green');
      header.classList.add('red');
    }
  });
});
