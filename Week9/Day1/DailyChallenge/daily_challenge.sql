CREATE TABLE actors(
actor_id SERIAL PRIMARY KEY,
first_name VARCHAR(50) NOT NULL,
last_name VARCHAR(100) NOT NULL,
age DATE NOT NULL,
number_oscars SMALLINT NOT NULL

)
-- add data in columns
INSERT INTO actors (first_name, last_name, age, number_oscars) VALUES
('LEONARDO', 'DICAPRIO', '1974-11-11', 1),
('MERYL', 'STREEP', '1949-06-22', 3),
('BRAD', 'PITT', '1963-12-18', 2),
('ANGELINA', 'JOLIE', '1975-06-04', 1),
('TOM', 'HANKS', '1956-07-09', 2),
('NATALIE', 'PORTMAN', '1981-06-09', 1),
('DENZEL', 'WASHINGTON', '1954-12-28', 2),
('SCARLETT', 'JOHANSSON', '1984-11-22', 0),
('ROBERT', 'DOWNEY', '1965-04-04', 0),
('JENNIFER', 'LAWRENCE', '1990-08-15', 1),
('CHRISTIAN', 'BALE', '1974-01-30', 1),
('VIOLA', 'DAVIS', '1965-08-11', 1),
('RYAN', 'GOSLING', '1980-11-12', 0),
('CHARLIZE', 'THERON', '1975-08-07', 1),
('JOAQUIN', 'PHOENIX', '1974-10-28', 1),
('KATE', 'WINSLET', '1975-10-05', 1),
('MORGAN', 'FREEMAN', '1937-06-01', 1),
('EMMA', 'STONE', '1988-11-06', 1),
('SAMUEL', 'JACKSON', '1948-12-21', 0),
('REESE', 'WITHERSPOON', '1976-03-22', 1);


-- see all data
SELECT * FROM actors;

-- Daily Challenge

-- Count how many actors are in the table.
SELECT COUNT (actor_id)
FROM actors;
--20


--Try to add a new actor with some blank fields. What do you think the outcome will be ?

INSERT INTO actors (first_name, last_name, age, number_oscars) VALUES
('PEDRO', 'PASCAL','1988-11-06',0);

---All columns except actor_id are marked as NOT NULL. This means you must provide a non-null value for each of these fields when inserting a new row.
SELECT * FROM actors
WHERE first_name = 'PEDRO';

