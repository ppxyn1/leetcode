/* Write your PL/SQL query statement below */

SELECT a.name as Employee
FROM Employee a, Employee b
WHERE a.ManagerId = b.Id AND a.Salary > b.Salary;