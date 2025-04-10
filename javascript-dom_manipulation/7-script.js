document.addEventListener("DOMContentLoaded", function () {
    fetch("https://swapi-api.hbtn.io/api/films/?format=json")
        .then((response) => {
            if (!response.ok) {
                throw new Error("Network response was not ok"); // Check for HTTP errors
            }
            return response.json();
        })
        .then((content) => {
            const movies = content.results;
            const movieList = document.querySelector("#list_movies"); // Select the <ul> element

            for (const movie of movies) {
                const li = document.createElement("li");
                li.innerText = movie.title;
                movieList.appendChild(li);
            } // Loop through each movie and create a <li> element for each one
            // Append the <li> elements to the <ul> element
        })
        .catch(error => {
            console.error("Error fetching movies:", error); // Handle errors
        });
});
