-- `BIGINT NOT NULL DEFAULT 0` is the correct column definition for storing the result of a `COUNT()`.
-- To check, compare the outputs of `SHOW CREATE TABLE Solution;` and `SHOW CREATE TABLE Example1;`.
CREATE TABLE IF NOT EXISTS Example1 (customer_id INT, count_no_trans BIGINT NOT NULL DEFAULT 0);
TRUNCATE TABLE Example1;
INSERT INTO Example1 (customer_id, count_no_trans) VALUES
  ROW(54, 2),
  ROW(30, 1),
  ROW(96, 1);
