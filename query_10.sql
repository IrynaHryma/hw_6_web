

SELECT  subjects.name
FROM   teachers t 
JOIN subjects  ON t.id = subjects.teacher_id 
JOIN students  ON students.group_id  = subjects.teacher_id 
WHERE t.id = 1
AND students.id = 2;

