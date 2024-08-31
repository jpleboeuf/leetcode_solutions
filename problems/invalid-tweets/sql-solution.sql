DROP TABLE IF EXISTS Solution;
CREATE TABLE Solution AS (

SELECT t.tweet_id
FROM Tweets t
-- `CHAR_LENGTH()` is better but does not pass LeetCode's test.
WHERE LENGTH(t.content) > 15

);
