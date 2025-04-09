document.addEventListener("DOMContentLoaded", function () {
    // Select the <div> element with id="update_header" from the HTML
    const updateHeaderElement = document.querySelector("#update_header");
    // Select the <header> element from the HTML
    const headerElement = document.querySelector("header");

    // Add a click event listener to the <div> element
    updateHeaderElement.addEventListener("click", function () {
        // When the <div> is clicked, update the text content of the <header> element
        headerElement.textContent = "New Header!!!";
    });
});

