
SELECT subjects.name, s.fullname ,ROUND(AVG(g.grades),2) AS average_grade
FROM grades g 
JOIN students s ON s.id = g.student_id 
JOIN subjects  ON subject_id = g.subject_id 
WHERE subject_id =3
GROUP BY s.fullname 
ORDER BY average_grade DESC 
LIMIT 1;
