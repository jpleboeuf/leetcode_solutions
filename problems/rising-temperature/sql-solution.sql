DROP TABLE IF EXISTS Solution;
CREATE TABLE Solution AS (

SELECT id
FROM (
  SELECT w.id,
    w.temperature, LAG(w.temperature) OVER(ORDER BY w.recordDate) AS prev_temperature,
    w.recordDate,  LAG(w.recordDate)  OVER(ORDER BY w.recordDate) AS prev_recordDate
  FROM Weather w
) AS temp
WHERE (temperature > prev_temperature) AND (recordDate - prev_recordDate) = 1

);
