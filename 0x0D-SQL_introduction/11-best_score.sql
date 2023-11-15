-- Select all scores h-e than 10 and display them with the name .
-- record should be ordered by score >= 10 .

SELECT `score`, `name` FROM second_table WHERE `score` >= 10 ORDER BY score DESC;
