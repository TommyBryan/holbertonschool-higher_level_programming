// wait for page to load
document.addEventListener('DOMContentLoaded', function () {
  // select the <div> with id='red_header'
  const redHeader = document.getElementById('red_header');

  // Select header element
  const header = document.querySelector('header');

  // Click event listener to redHeader div
  redHeader.addEventListener('click', function () {
    //  Add class 'red' to <header>
    header.classList.add('red');
  });
});
