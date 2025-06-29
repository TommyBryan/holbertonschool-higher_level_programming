-- Lists all shows that belong to the genre 'Comedy'
-- Displays: tv_shows.title
-- Sorted by title in ascending order

SELECT tv_shows.title
FROM tv_shows
JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
JOIN tv_genres ON tv_genres.id = tv_show_genres.genre_id
WHERE tv_genres.name = 'Comedy'
ORDER BY tv_shows.title;
