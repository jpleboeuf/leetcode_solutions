DROP TABLE IF EXISTS Solution;
CREATE TABLE Solution AS (

SELECT DISTINCT v.author_id AS id
FROM Views v
WHERE v.author_id = v.viewer_id
ORDER BY id ASC

);
