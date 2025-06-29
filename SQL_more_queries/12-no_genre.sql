-- Lists all shows that do not have any genre linked
-- Displays: tv_shows.title - tv_show_genres.genre_id (NULL)
-- Sorted by tv_shows.title and genre_id

SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
WHERE tv_show_genres.genre_id IS NULL
ORDER BY tv_shows.title, tv_show_genres.genre_id;
