document.addEventListener("DOMContentLoaded", function () {
    // Get the element with id 'add_item' and the list with class 'my_list' from 4-main.html
    const addItemElement = document.querySelector("#add_item");
    const myList = document.querySelector(".my_list");
  
    // Add a click event listener to the 'add_item' element
    addItemElement.addEventListener("click", function () {
      // Create a new <li> element
      const newItem = document.createElement("li");
      newItem.textContent = "Item"; // Set the text content to 'Item'
  
      // Append the new item to the list in 4-main.html
      myList.appendChild(newItem);
    });
});
