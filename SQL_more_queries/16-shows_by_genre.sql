-- Lists all shows and their genres (NULL if no genre linked)
-- Displays: tv_shows.title - tv_genres.name
-- Sorted by show title and genre name in ascending order

SELECT tv_shows.title, tv_genres.name
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
LEFT JOIN tv_genres ON tv_genres.id = tv_show_genres.genre_id
ORDER BY tv_shows.title, tv_genres.name;
