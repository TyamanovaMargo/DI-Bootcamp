--create table items
CREATE TABLE items (
    item_id INT PRIMARY KEY,
   	item_name VARCHAR(100) NOT NULL,
    price INT NOT NULL
);

--creatre table  customer
CREATE TABLE customer (
    customer_id INT PRIMARY KEY,
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL
);


--add items
INSERT INTO items (item_id, item_name, price) VALUES
(1,'Small Desk',100),
(2,'Large desk',300),
(3,'Fan',80);


--all the items
SELECT * FROM items

--add customers
INSERT INTO customer (customer_id, first_name, last_name) VALUES
(1,'Greg','Jones'),
(2,'Sandra','Jones'),
(3,'Scott','Scott'),
(4,'Trevor','Green'),
(5,'Melanie ','Johnson');


--all the customer
SELECT * FROM customer


-- All the items with a price above 80 (80 not included).
SELECT * FROM items
WHERE price > 80;

--All the items with a price below 300. (300 included)
SELECT * FROM items
WHERE price < 300;

---All customers whose last name is ‘Smith’ (What will be your outcome?).
SELECT * FROM customer
WHERE last_name  = "Smith";
---ERROR:  column "Smith" does not exist

--All customers whose last name is ‘Jones’
SELECT * FROM customer
WHERE last_name  = 'Jones';

--All customers whose firstname is not ‘Scott’.
SELECT * FROM customer
WHERE first_name != 'Scott';

