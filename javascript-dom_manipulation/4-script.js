document.addEventListener('DOMContentLoaded', function () {
  // Get 'add_item' div and 'my_list' ul
  const item = document.getElementById('add_item');
  const list = document.querySelector('.my_list');

  // click event to 'item'
  item.addEventListener('click', function () {
    const newItem = document.createElement('li');
    newItem.textContent = 'Item';

    // append new item to list
    list.appendChild(newItem);
  });
});
