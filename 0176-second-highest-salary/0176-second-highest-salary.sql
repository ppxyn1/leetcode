/* Write your PL/SQL query statement below */

-- 최대가 아닌 것중 최대 고르기(서브쿼리)
SELECT MAX(salary) AS SecondHighestSalary FROM Employee
WHERE salary < (SELECT MAX(salary) FROM Employee) 


