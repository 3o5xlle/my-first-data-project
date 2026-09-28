DROP TABLE IF EXISTS students ;
CREATE TABLE students (
id INT PRIMARY KEY ,
student_name VARCHAR (100),
birth_date DATE ,
track VARCHAR (50)
);
INSERT INTO students (id, student_name, birth_date, track)
VALUES (1, 'Reem', '2007-03-22', 'DATA'),
       (2, 'Sara', '2008-05-14', 'DATA'),
       (3, 'Jawaher', '1995-10-31', 'Security');
SELECT id, student_name, strftime('%d-%m-%Y', birth_date) AS birth_date, track FROM students;
