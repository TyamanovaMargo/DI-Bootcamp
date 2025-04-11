--🌟 Exercise 1: DVD Rental
--Get a list of all the languages, from the language table.

SELECT name FROM language

--Get a list of all films joined with their languages – select the following details : film title, description, and language name.
SELECT film.title, film.description, language.name
FROM film
JOIN language ON film.language_id = language.language_id;


--Get all languages, even if there are no films in those languages – select the following details : film title, description, and language name.

SELECT film.title, film.description, TRIM(language.name) AS language_name
FROM language
LEFT JOIN film ON language.language_id = film.language_id;


--Create a new table called new_film
CREATE TABLE new_film (
    id SERIAL PRIMARY KEY,   -- Auto-incrementing primary key
    name VARCHAR(255) NOT NULL  -- Film name, cannot be null
);

INSERT INTO new_film (name) VALUES
('The Matrix'),
('Inception'),
('The Shawshank Redemption'),
('The Dark Knight'),
('Forrest Gump');

---Create a new table called customer_review
CREATE TABLE customer_review (
    review_id SERIAL PRIMARY KEY,                -- Auto-incrementing primary key
    film_id INT NOT NULL,                        -- Film being reviewed (foreign key)
    language_id INT NOT NULL,                    -- Language of the review (foreign key)
    title VARCHAR(255) NOT NULL,                  -- Title of the review
    score INT CHECK (score >= 1 AND score <= 10), -- Rating between 1 and 10
    review_text TEXT,                            -- Review text (no limit on length)
    last_update TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- When the review was last updated
    FOREIGN KEY (film_id) REFERENCES new_film(id)  -- Foreign key for film
        ON DELETE CASCADE,                        -- Automatically delete reviews when film is deleted
    FOREIGN KEY (language_id) REFERENCES language(language_id)  -- Foreign key for language
);

--Add 2 movie reviews. Make sure you link them to valid objects in the other tables.
INSERT INTO customer_review (film_id, language_id, title, score, review_text)
VALUES
(1, 1, 'A Game-Changer', 10, 'The Matrix redefined the science fiction genre. An absolute masterpiece.'),
(2, 1, 'Mind-Bending', 9, 'Inception is a thrilling ride that will leave you questioning reality. Brilliantly executed.');


--Delete a film that has a review from the new_film table, what happens to the customer_review table?
DELETE FROM new_film WHERE id = 1;


---The film "The Matrix" will be deleted from the new_film table.

--All reviews related to "The Matrix" (with film_id = 1) will also be automatically deleted from the customer_review table, due to the ON DELETE CASCADE rule.