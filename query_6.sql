
SELECT  s.fullname
FROM  students s 
JOIN groups gr  ON s.group_id = gr.id 
WHERE gr.id = 3
ORDER BY s.fullname ASC ; 