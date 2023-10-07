
SELECT  t.fullname ,subjects.name 
FROM  teachers t
JOIN subjects  ON t.id = subjects.teacher_id 
WHERE teacher_id =2
GROUP BY t.fullname
ORDER BY t.fullname ASC ; 