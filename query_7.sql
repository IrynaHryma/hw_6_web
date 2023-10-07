

SELECT  s.fullname, grades, subjects.name
FROM grades g 
JOIN students s ON s.id = g.student_id 
JOIN subjects  ON subject_id = g.subject_id 
JOIN [groups] gr ON gr.id =s.group_id 
WHERE subject_id = 2
GROUP BY s.id
ORDER BY  grades DESC ; 