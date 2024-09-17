-- Table should have been named `Activities`...
CREATE TABLE IF NOT EXISTS Activity (machine_id INT, process_id INT, activity_type ENUM('start', 'end'), timestamp FLOAT);
TRUNCATE TABLE Activity;
INSERT INTO Activity (machine_id, process_id, activity_type, timestamp) VALUES
  ROW(0, 0, 'start', 0.712),
  ROW(0, 0, 'end',   1.52 ),
  ROW(0, 1, 'start', 3.14 ),
  ROW(0, 1, 'end',   4.12 ),
  ROW(1, 0, 'start', 0.55 ),
  ROW(1, 0, 'end',   1.55 ),
  ROW(1, 1, 'start', 0.43 ),
  ROW(1, 1, 'end',   1.42 ),
  ROW(2, 0, 'start', 4.1  ),
  ROW(2, 0, 'end',   4.512),
  ROW(2, 1, 'start', 2.5  ),
  ROW(2, 1, 'end',   5    );
