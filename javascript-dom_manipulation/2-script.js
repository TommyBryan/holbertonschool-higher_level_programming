document.addEventListener("DOMContentLoaded", function () {
  // Get the element with id 'red_header' from 2-main.html
  const redHeaderElement = document.querySelector("#red_header");

  function elementAddClass() {
    // Add the 'red' class to the <header> element in 2-main.html
    document.querySelector("header").classList.add("red");
  }

  // Add a click event listener to the 'red_header' element in 2-main.html
  redHeaderElement.addEventListener("click", elementAddClass);
});
