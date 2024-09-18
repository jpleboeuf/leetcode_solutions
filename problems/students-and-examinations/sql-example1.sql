CREATE TABLE IF NOT EXISTS Example1 (student_id INT, student_name VARCHAR(20), subject_name VARCHAR(20), attended_exams BIGINT NOT NULL DEFAULT 0);
TRUNCATE TABLE Example1;
INSERT INTO Example1 (student_id, student_name, subject_name, attended_exams) VALUES
  ROW( 1, 'Alice', 'Math',        3),
  ROW( 1, 'Alice', 'Physics',     2),
  ROW( 1, 'Alice', 'Programming', 1),
  ROW( 2, 'Bob',   'Math',        1),
  ROW( 2, 'Bob',   'Physics',     0),
  ROW( 2, 'Bob',   'Programming', 1),
  ROW( 6, 'Alex',  'Math',        0),
  ROW( 6, 'Alex',  'Physics',     0),
  ROW( 6, 'Alex',  'Programming', 0),
  ROW(13, 'John',  'Math',        1),
  ROW(13, 'John',  'Physics',     1),
  ROW(13, 'John',  'Programming', 1);
