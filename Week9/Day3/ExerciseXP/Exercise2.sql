--🌟 Exercise 2 : DVD Rental
--Use UPDATE to change the language of some films. Make sure that you use valid languages.

UPDATE film
SET language_id = 3
WHERE film_id =1; 

SELECT film_id,language_id
FROM film
WHERE film_id =1;

---Which foreign keys (references) are defined for the customer table? How does this affect the way in which we INSERT into the customer table?
--store_id → references store(store_id)
--address_id → references address(address_id)
--use existing store_id and address_id values — otherwise, the insert will fail due to foreign key constraints.


---We created a new table called customer_review. Drop this table. Is this an easy step, or does it need extra checking?

DROP TABLE customer_review;
--To check dependencies
SELECT *
FROM information_schema.constraint_table_usage
WHERE table_name = 'customer_review';


SELECT *
FROM information_schema.constraint_table_usage
WHERE table_name = 'customer_review';


--Find out how many rentals are still outstanding (ie. have not been returned to the store yet)

SELECT COUNT(rental_id)
FROM rental
WHERE return_date IS NULL;

--Find the 30 most expensive movies which are outstanding (ie. have not been returned to the store yet)
SELECT film.title, film.rental_rate, rental.return_date
FROM rental
JOIN inventory  ON rental.inventory_id = inventory.inventory_id
JOIN film  ON inventory.film_id = film.film_id
WHERE rental.return_date IS NULL
ORDER BY film.rental_rate DESC
LIMIT 30;





---The 1st film : The film is about a sumo wrestler, and one of the actors is Penelope Monroe.
SELECT f.title,f.description
FROM film f	
JOIN film_actor
	ON f.film_id = film_actor.film_id
JOIN actor a
	ON film_actor.actor_id = a.actor_id

where a.first_name = 'Penelope' 
	AND a.last_name = 'Monroe' 
	AND f.description ILIKE '%sumo wrestler%';

--The 2nd film : A short documentary (less than 1 hour long), rated “R”.

SELECT title, description,length,rating
FROM film
WHERE length < 60 
	AND rating  = 'R';


--The 3rd film : A film that his friend Matthew Mahan rented. He paid over $4.00 for the rental, and he returned it between the 28th of July and the 1st of August, 2005.

SELECT f.title,f.description
FROM customer c
JOIN payment p
	ON c.customer_id = p.customer_id
JOIN rental r
	ON p.rental_id = r.rental_id
JOIN inventory i
	ON i.inventory_id = r.inventory_id
JOIN film f
	ON f.film_id = i.film_id
WHERE  c.first_name = 'Matthew' 
	AND c.last_name = 'Mahan'
	AND p.amount > 4.00
	AND r.return_date BETWEEN '2005-07-28' AND '2005-08-01';


--The 4th film : His friend Matthew Mahan watched this film, as well. It had the word “boat” in the title or description, and it looked like it was a very expensive DVD to replace.

SELECT f.title,f.description
FROM customer c
JOIN payment p
	ON c.customer_id = p.customer_id
JOIN rental r
	ON p.rental_id = r.rental_id
JOIN inventory i
	ON i.inventory_id = r.inventory_id
JOIN film f
	ON f.film_id = i.film_id
WHERE  c.first_name = 'Matthew' 
	AND c.last_name = 'Mahan'
	AND (f.title ILIKE '%boat%' OR f.description ILIKE '%boat%')
ORDER BY f.replacement_cost DESC
LIMIT 1;




