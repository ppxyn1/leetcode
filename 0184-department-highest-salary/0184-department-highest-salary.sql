/* Write your PL/SQL query statement below */
SELECT  d.name as Department, 
        e.name as Employee,
        e.salary as Salary
FROM Employee e 
Left Join Department d ON e.departmentId = d.id;
-- ORDER BY e.salary DESC
WHERE (Salary, DepartmentId) 
IN (
    SELECT MAX(salary), departmentId 
    FROM Employee 
    GROUP BY departmentId
)