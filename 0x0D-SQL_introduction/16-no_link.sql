-- SELECT score and name
-- name should be not NULL and Records should be listed by descending score order

SELECT score, name FROM second_table WHERE NAME IS NOT NULL ORDER BY score DESC; 
