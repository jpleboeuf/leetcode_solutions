DROP TABLE IF EXISTS Solution;
CREATE TABLE Solution AS (

WITH
    students_subjects_prod AS (
        SELECT s.student_id, s.student_name, d.subject_name
        FROM Students s, Subjects d
    ),
    exam_count AS (
        SELECT e.student_id, e.subject_name, COUNT(*) AS attended_exams
        FROM Examinations e
        GROUP BY e.student_id, e.subject_name
    )
SELECT ssp.student_id, ssp.student_name, ssp.subject_name,
    COALESCE(ec.attended_exams, 0) AS attended_exams
FROM students_subjects_prod ssp
LEFT JOIN exam_count ec USING(student_id, subject_name)
ORDER BY ssp.student_id, ssp.subject_name

);
