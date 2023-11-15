-- list the number of records that have the same score Value

SELECT score, COUNT(*) AS 'number' FROM second_table GROUP BY score DESC;
