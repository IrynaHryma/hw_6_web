

SELECT  subjects.name 
FROM  students s 
JOIN grades   ON s.id = grades.student_id 
JOIN subjects  ON grades.subject_id = subject_id
WHERE s.id = 1
GROUP BY subjects.name
ORDER BY subjects.name ASC ; 
