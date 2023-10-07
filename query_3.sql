
SELECT subjects.name, gr.name ,ROUND(AVG(g.grades),2) AS average_grade
FROM grades g 
JOIN students s ON s.id = g.student_id 
JOIN subjects  ON subject_id = g.subject_id 
JOIN [groups] gr ON gr.id =s.group_id 
WHERE subject_id =2
GROUP BY gr.name
ORDER BY average_grade DESC; 
