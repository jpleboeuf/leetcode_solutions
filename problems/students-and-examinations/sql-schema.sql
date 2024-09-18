CREATE TABLE IF NOT EXISTS Students (student_id INT, student_name VARCHAR(20));
CREATE TABLE IF NOT EXISTS Subjects (subject_name VARCHAR(20));
CREATE TABLE IF NOT EXISTS Examinations (student_id INT, subject_name VARCHAR(20));
TRUNCATE TABLE Students;
INSERT INTO Students (student_id, student_name) VALUES
  ROW( 1, 'Alice'),
  ROW( 2, 'Bob'),
  ROW(13, 'John'),
  ROW( 6, 'Alex');
TRUNCATE TABLE Subjects;
INSERT INTO Subjects (subject_name) VALUES
  ROW('Math'),
  ROW('Physics'),
  ROW('Programming');
TRUNCATE TABLE Examinations;
INSERT INTO Examinations (student_id, subject_name) VALUES
  ROW( 1, 'Math'),
  ROW( 1, 'Physics'),
  ROW( 1, 'Programming'),
  ROW( 2, 'Programming'),
  ROW( 1, 'Physics'),
  ROW( 1, 'Math'),
  ROW(13, 'Math'),
  ROW(13, 'Programming'),
  ROW(13, 'Physics'),
  ROW( 2, 'Math'),
  ROW( 1, 'Math');
