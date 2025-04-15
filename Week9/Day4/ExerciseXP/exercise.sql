--Exercise 1
--Task 1. Find the average age of competitors who have won at least one medal, grouped by the type of medal they won
SELECT m.medal_name, --
       (SELECT AVG(g.age) 
        FROM games_competitor gс
        WHERE gс.id IN (
            SELECT ce.competitor_id 
            FROM competitor_event ce 
            WHERE ce.medal_id = m.id
        )
       ) AS average_age
FROM medal m;

--Task 2.Identify the top 5 regions with the highest number of unique competitors who have participated in more than 3 different events
SELECT nr.region_name, COUNT(DISTINCT competitor_id) AS unique_competitors
FROM (
    -- Subquery to filter competitors who participated in more than 3 events
    SELECT competitor_id
    FROM competitor_event
    GROUP BY competitor_id
    HAVING COUNT(DISTINCT event_id) > 3 --Ш filter to leave only those with more than 3 unique competitions.
) AS filtered_competitors
JOIN games_competitor gc ON filtered_competitors.competitor_id = gc.person_id
JOIN noc_region nr ON gc.id = nr.id
GROUP BY nr.region_name
ORDER BY unique_competitors DESC
LIMIT 5;

--Task 3.Create a temporary table to store the total number of medals won by each competitor and filter to show only those who have won more than 2 medals.
CREATE TEMPORARY TABLE temp_medal_winners AS
SELECT competitor_id, COUNT(medal_id) AS total_medals
FROM competitor_event
WHERE medal_id IS NOT NULL  -- Participations without medals are ignored.
GROUP BY competitor_id
HAVING COUNT(medal_id) > 2;

CREATE TEMPORARY TABLE temp_competitor_analysis AS
SELECT competitor_id, COUNT(medal_id) AS total_medals
FROM competitor_event
GROUP BY competitor_id;

--Task 4.Use a subquery within a DELETE statement to remove records of competitors who have not won any medals from a temporary table created for analysis.
DELETE FROM temp_competitor_analysis
WHERE competitor_id IN (
    SELECT competitor_id FROM competitor_event
    GROUP BY competitor_id
    HAVING COUNT(medal_id) = 0
);

SELECT * FROM temp_competitor_analysis;

-- Exercise 2
--Task 1.Update the heights of competitors based on the average height of competitors from the same region. Use a correlated subquery within the UPDATE statement.
UPDATE person
SET height = (
    SELECT AVG(p2.height)
    FROM person p2
    JOIN person_region pr2 ON p2.id = pr2.person_id
    WHERE pr2.region_id = person_region.region_id
)
WHERE height IS NULL
AND person.id IN (
    SELECT person_id FROM person_region
);

--Task 2.Insert new records into a temporary table for competitors who participated in more than one event in the same games and list their total number of events participated. Use nested subqueries for filtering.
CREATE TEMPORARY TABLE temp_competitors AS
SELECT competitor_id, games_id, COUNT(DISTINCT event_id) AS total_events
FROM competitor_event
JOIN games_competitor ON competitor_event.competitor_id = games_competitor.id
GROUP BY competitor_id, games_id
HAVING COUNT(DISTINCT event_id) > 1;

-- Task 3.Identify regions where the average number of medals won per competitor is greater than the overall average. Use subqueries to calculate and compare averages.
SELECT nr.region_name, 
       AVG(competitor_medals.medals_count) AS avg_medals_per_competitor
FROM (
    -- Subquery: Number of medals per competitor and per region
    SELECT pr.region_id, ce.competitor_id, COUNT(ce.medal_id) AS medals_count
    FROM competitor_event ce
    JOIN person_region pr ON ce.competitor_id = pr.person_id
    WHERE ce.medal_id IS NOT NULL
    GROUP BY pr.region_id, ce.competitor_id
) competitor_medals
JOIN noc_region nr ON competitor_medals.region_id = nr.id
GROUP BY nr.region_name
HAVING AVG(competitor_medals.medals_count) > (
    -- Overall average medals per competitor
    SELECT AVG(medals_count) 
    FROM (
        SELECT competitor_id, COUNT(medal_id) AS medals_count
        FROM competitor_event
        WHERE medal_id IS NOT NULL
        GROUP BY competitor_id
    ) overall_avg
)
ORDER BY avg_medals_per_competitor DESC;


-- Task 4
-- Created a temporary table to store competitors and their seasons of participation
CREATE TEMPORARY TABLE temp_competitor_seasons AS
SELECT gc.person_id, 
       MIN(g.season) AS first_season, 
       MAX(g.season) AS last_season
FROM games_competitor gc
JOIN games g ON gc.games_id = g.id
GROUP BY gc.person_id
HAVING MIN(g.season) <> MAX(g.season);

