--Daily Challenge 

--Create table

CREATE TABLE employees(
	employee_id INT PRIMARY KEY,
	employee_name VARCHAR(50),
	salary DECIMAL(10,2),
	hire_date VARCHAR(20),
	department VARCHAR(50)
);

INSERT INTO employees (employee_id, employee_name, salary, hire_date, department)
VALUES
(1, 'Amy West', 60000.00, '2021-01-15', 'HR'),
(2, 'Ivy Lee', 75000.50, '2020-05-22', 'Sales'),
(3, 'Joe Smith', 80000.75, '2019-08-10', 'Marketing'),
(4, 'John White', 90000.00, '2020-11-05', 'Finance'),
(5, 'Jane Hill', 85000.25, '2022-02-28', 'IT'),
(6, 'Dave West', 72000.00, '2022-03-03', 'Marketing'),
(7, 'Fanny Lee', 65000.50, '2019-06-15', 'Sales'),
(8, 'Ivy Hill', 87000.25, '2021-11-30', 'Finance'),
(9, 'Ivy Hill', 87000.25, '2021-07-18', 'IT'),
(10, 'Joe White', 78000.00, '2022-04-05', 'Marketing'),
(11, 'John Lee', 69000.00, '2018-12-10', 'HR'),
(12, 'Jane West', 89000.25, '2017-09-15', 'Sales'),
(13, 'Dave Smith', 60000.75, '2022-01-08', NULL),
(14, 'Fanny White', 70000.00, '2019-04-22', 'IT'),
(15, 'Amy Hill', 84000.50, '2020-08-17', 'Marketing'),
(16, 'Ivy West', 92000.25, '2021-02-03', 'Finance'),
(17, 'Joe Lee', 58000.75, '2018-05-28', 'IT'),
(18, 'John Smith', 77000.00, '2019-10-10', 'HR'),
(19, 'Jane Hill', 81000.50, '2022-03-15', 'Sales'),
(20, 'Dave White', 70000.25, '2017-12-20', 'Marketing');

--Identify and handle any missing value.
-- to indentify NULL val
SELECT * FROM employees 
WHERE employee_id IS NULL 
   OR employee_name IS NULL 
   OR salary IS NULL 
   OR hire_date IS NULL 
   OR department IS NULL;


--- to handle missing data
SELECT COALESCE(department, 'Unknow') FROM employees;


--Check for and eliminate any duplicate rows in the dataset.
SELECT employee_id, COUNT(*)
FROM employees
GROUP BY employee_id
HAVING COUNT(*) > 1;

SELECT employee_name, COUNT(*)
FROM employees
GROUP BY employee_name
HAVING COUNT(*) > 1;

SELECT  salary, COUNT(*)
FROM employees
GROUP BY  salary
HAVING COUNT(*) > 1;

SELECT  hire_date, COUNT(*)
FROM employees
GROUP BY  hire_date
HAVING COUNT(*) > 1;

SELECT  department, COUNT(*)
FROM employees
GROUP BY  department
HAVING COUNT(*) > 1;


--Deleting Duplicates
WITH cte AS (
    SELECT ctid,
           ROW_NUMBER() OVER (PARTITION BY employee_name ORDER BY employee_name) AS rn
    FROM employees
)
DELETE FROM employees
USING cte
WHERE employees.ctid = cte.ctid
  AND cte.rn > 1;


 WITH cte AS (
    SELECT ctid,
           ROW_NUMBER() OVER (PARTITION BY department ORDER BY department) AS rn
    FROM employees
)
DELETE FROM employees
USING cte
WHERE employees.ctid = cte.ctid
  AND cte.rn > 1;

--Correct any structural issues, such as inconsistent naming conventions or formatting errors.
-- Convert date formats
SELECT CAST(hire_date AS DATE) FROM employees;


--Ensure all columns have appropriate data types (e.g. the hire_date column).
SELECT column_name, data_type
FROM information_schema.columns
WHERE table_name = 'employees';


--change data type 
ALTER TABLE employees
ALTER COLUMN hire_date TYPE DATE
USING hire_date::DATE;


--check data type
SELECT column_name, data_type, character_maximum_length
FROM information_schema.columns
WHERE table_name = 'employees';

--Standardize and normalize data where applicable to ensure consistency.
UPDATE employees
SET department = 'Sales'
WHERE department IN ('sales', 'SALES');

UPDATE employees
SET department = 'HR'
WHERE department IN ('hr', 'HR');

UPDATE employees
SET department = 'Marketing'
WHERE department IN ('marketing', 'MARKETING');

UPDATE employees
SET department = 'IT'
WHERE department IN ('it', 'IT');

UPDATE employees
SET department = 'Finance'
WHERE department IN ('finance', 'FINANCE');


