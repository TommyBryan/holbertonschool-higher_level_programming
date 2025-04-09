document.addEventListener("DOMContentLoaded", function () {
  // Get red_header element
  const redHeaderElement = document.querySelector("#red_header");

  function elementAddClass() {
    // Get header element and a class to it
    document.querySelector("header").classList.add("red");
  }

  // Add event listener to red_header element
  redHeaderElement.addEventListener("click", elementAddClass);
});
