addEventListener("DOMContentLoaded", function () {
    // Get the element with id 'toggle_header' and the <header> element from 3-main.html
    const toggleHeaderElement = this.document.querySelector("#toggle_header");
    const headerElement = document.querySelector("header");

    // Add a click event listener to toggle the class on the <header> element
    toggleHeaderElement.addEventListener("click", function () {
        // Toggle between 'red' and 'green' classes on the <header> element in 3-main.html
        if (headerElement.classList.contains("red")) {
            headerElement.classList.remove("red");
            headerElement.classList.add("green");
        } else {
            headerElement.classList.remove("green");
            headerElement.classList.add("red");
        }
    });
});
