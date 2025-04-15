
--Exercise1
-- Task 1
-- Creation of a temporary table to store competitors and their medals by season
CREATE TEMPORARY TABLE temp_medalists AS
SELECT gc.person_id, 
       g.season, 
       COUNT(ce.medal_id) AS total_medals
FROM games_competitor gc
JOIN competitor_event ce ON gc.id = ce.competitor_id
JOIN games g ON gc.games_id = g.id
WHERE ce.medal_id IS NOT NULL
GROUP BY gc.person_id, g.season;

-- Selection of competitors who won medals in both seasons
SELECT person_id 
FROM temp_medalists
GROUP BY person_id
HAVING COUNT(DISTINCT season) = 2;

SELECT * FROM temp_medalists;

-- Task 2
-- Create a temporary table to store competitors who have won medals in exactly two sports
CREATE TEMPORARY TABLE temp_two_sport_medalists AS
SELECT ce.competitor_id, 
       COUNT(DISTINCT e.sport_id) AS unique_sports, 
       COUNT(ce.medal_id) AS total_medals
FROM competitor_event ce
JOIN event e ON ce.event_id = e.id
WHERE ce.medal_id IS NOT NULL
GROUP BY ce.competitor_id
HAVING COUNT(DISTINCT e.sport_id) = 2;

-- Select the 3 competitors with the most medals and display the sport names
SELECT tsm.competitor_id, tsm.total_medals, 
       GROUP_CONCAT(DISTINCT s.sport_name) AS sports_played
FROM temp_two_sport_medalists tsm
JOIN competitor_event ce ON tsm.competitor_id = ce.competitor_id
JOIN event e ON ce.event_id = e.id
JOIN sport s ON e.sport_id = s.id
GROUP BY tsm.competitor_id, tsm.total_medals
ORDER BY tsm.total_medals DESC
LIMIT 3;

-- Exercise2
--Task 1
--Step1
WITH competitor_top_event AS (
    SELECT ce.competitor_id, 
           ce.event_id, 
           COUNT(ce.medal_id) AS medal_count
    FROM competitor_event ce
    WHERE ce.medal_id IS NOT NULL
    GROUP BY ce.competitor_id, ce.event_id
    HAVING COUNT(ce.medal_id) = (
        SELECT MAX(medal_total)
        FROM (
            SELECT COUNT(ce2.medal_id) AS medal_total
            FROM competitor_event ce2
            WHERE ce2.competitor_id = ce.competitor_id AND ce2.medal_id IS NOT NULL
            GROUP BY ce2.event_id
        ) AS event_medals
    )
)

-- Step 2: Match competitors to regions and total medals by region
SELECT nr.region_name, 
       SUM(cte.medal_count) AS total_medals
FROM competitor_top_event cte
JOIN games_competitor gc ON cte.competitor_id = gc.id
JOIN person_region pr ON gc.person_id = pr.person_id
JOIN noc_region nr ON pr.region_id = nr.id
GROUP BY nr.region_name
ORDER BY total_medals DESC
LIMIT 5;

-- Task 2
-- Create a temporary table to store eligible competitors
CREATE TEMP TABLE temp_no_medal_competitors AS
SELECT gc.person_id, p.full_name, COUNT(DISTINCT gc.games_id) AS games_participated
FROM games_competitor gc
JOIN person p ON gc.person_id = p.id
LEFT JOIN competitor_event ce ON gc.id = ce.competitor_id
WHERE ce.medal_id IS NULL
GROUP BY gc.person_id, p.full_name
HAVING COUNT(DISTINCT gc.games_id) > 3;

-- Displaying the contents of the temporary table
SELECT * FROM temp_no_medal_competitors;