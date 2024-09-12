DROP TABLE IF EXISTS Solution;
CREATE TABLE Solution AS (

SELECT v.customer_id, COUNT(v.visit_id) AS count_no_trans
FROM Visits v
WHERE v.visit_id NOT IN (
    SELECT DISTINCT t.visit_id
    FROM Transactions t
)
GROUP BY v.customer_id

);
