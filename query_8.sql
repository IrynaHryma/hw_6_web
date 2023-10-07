

SELECT t.fullname, ROUND(AVG(grades), 2) AS average_grade
FROM grades g
JOIN  teachers t  ON t.id = g.student_id 
GROUP BY t.fullname 
ORDER BY average_grade DESC 
