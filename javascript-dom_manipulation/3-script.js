addEventListener("DOMContentLoaded", function () {
    // Get the toggle_header element and the header element
    const toggleHeaderElement = this.document.querySelector("#toggle_header");
    const headerElement = document.querySelector("header");

    // Event listener to toggle the class on click
    toggleHeaderElement.addEventListener("click", function () {
        // Check the current class and toggle it betwen red and green
        if (headerElement.classList.contains("red")) {
            headerElement.classList.remove("red");
            headerElement.classList.add("green");
        } else {
            headerElement.classList.remove("green");
            headerElement.classList.add("red");
        }
    });
});
