
--🌟 Exercise 1: Building a Comprehensive Dataset for Employee Analysis
CREATE TABLE df_employee AS
SELECT 
    e.employee_id || '_' || CAST(e.date AS TEXT) AS id,  -- Use || for concatenation and CAST date to TEXT
    DATE(e.date) AS month_year,                          -- Use DATE() function to cast the timestamp to a DATE format
    e.employee_id,
    e.employee_name,
    e."GEN(M_F)" AS gender,                            
    e.age,                                            
    f.function,                                       
    f.function_group,                     
    s.salary,                                          
    c.company_name,                                    
    c.company_city,                                     
    c.company_state,                                  
    c.company_type,                                     
    c.const_site_category                              
FROM emp_dataset e
LEFT JOIN functions f ON e.function_code = f.function_code 
LEFT JOIN salaries s ON e.employee_id = s.employee_id AND DATE(e.date) = DATE(s.date)  
LEFT JOIN companies c ON e.company_id = c.company_id;  



--🌟 Exercise 2: Cleaning Data for Consistency and Quality
-- run the following SQLite request and observe your new table.
select * from df_employee;

--Remove all unwanted spaces from all text columns using TRIMcompanies
UPDATE df_employee
SET
    id = TRIM(id),  -- Removes any leading or trailing spaces from the `id` column
    employee_name = TRIM(employee_name), 
    gender = CASE 
                WHEN gender IS NULL THEN 'Unknown'  -- Example: if gender is NULL, set to 'Unknown'
                ELSE gender
             END,
    age = CASE 
              WHEN age < 18 THEN 18  -- Ensure age is not below 18, for example
              ELSE age
          END;

--Check for NULL values and empty values.
SELECT *
FROM df_employee
WHERE id IS NULL
   OR month_year IS NULL
   OR employee_id IS NULL
   OR employee_name IS NULL
   OR gender IS NULL
   OR age IS NULL
   OR function IS NULL
   OR function_group IS NULL
   OR salary IS NULL
   OR company_name IS NULL
   OR company_city IS NULL
   OR company_state IS NULL
   OR company_type IS NULL
   OR const_site_category IS NULL;


--Delete rows of the detected missing values.
CREATE TABLE df_employee_no_duplicates AS
SELECT DISTINCT * FROM df_employee;

--or
WITH CTE AS (
    SELECT *, ROW_NUMBER() OVER (PARTITION BY id ORDER BY id) AS rn
    FROM df_employee
)
DELETE FROM df_employee WHERE id IN (SELECT id FROM CTE WHERE rn > 1);


--check again dublicates
SELECT *, COUNT(*)
FROM df_employee
GROUP BY id, month_year, employee_id, employee_name, gender, age, function, function_group, salary, company_name, company_city, company_state, company_type, const_site_category
HAVING COUNT(*) > 1;


---🌟 Exercise 3 : Calculating Current Employee Counts by Company

SELECT month_year from  df_employee;

SELECT company_name, COUNT(employee_id) AS employee_count
FROM df_employee
GROUP BY company_name;

--🌟 Exercise 4 : Analyzing Employee Distribution by City and Over Timecompanies
--What is the total number of employees each city? Add a percentage column

SELECT 
    company_city, 
    COUNT(employee_id) AS total_employees,
    (COUNT(employee_id) * 100.0 / (SELECT COUNT(*) FROM df_employee)) AS percentage
FROM df_employee
GROUP BY company_city;

--What is the total number of employees each month?
SELECT 
    DATE(month_year) AS month,
    COUNT(employee_id) AS total_employees
FROM df_employee
GROUP BY month
ORDER BY month;

--SELECT 
SELECT 
    AVG(monthly_employee_count) AS average_employees_per_month
FROM (
    SELECT 
        DATE(month_year) AS month,
        COUNT(employee_id) AS monthly_employee_count
    FROM df_employee
    GROUP BY month
);


--🌟 Exercise 5 : Analyzing Employment Trends and Salary Metricscompanies
SELECT 
    MIN(monthly_employee_count) AS min_employees,
    MAX(monthly_employee_count) AS max_employees,
    (SELECT month FROM monthly_counts WHERE monthly_employee_count = MIN(monthly_employee_count) LIMIT 1) AS min_month,
    (SELECT month FROM monthly_counts WHERE monthly_employee_count = MAX(monthly_employee_count) LIMIT 1) AS max_month
FROM (
    SELECT 
        DATE(month_year) AS month,
        COUNT(employee_id) AS monthly_employee_count
    FROM df_employee
    GROUP BY month
) AS monthly_counts;

