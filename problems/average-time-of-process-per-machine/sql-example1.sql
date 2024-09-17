CREATE TABLE IF NOT EXISTS Example1 (machine_id INT, processing_time DOUBLE);
TRUNCATE TABLE Example1;
INSERT INTO Example1 (machine_id, processing_time) VALUES
  ROW(0, 0.894),
  ROW(1, 0.995),
  ROW(2, 1.456);
