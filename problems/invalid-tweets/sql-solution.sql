DROP TABLE IF EXISTS Solution;
CREATE TABLE Solution AS (

SELECT t.tweet_id
FROM Tweets t
WHERE LENGTH(t.content) > 15

);
