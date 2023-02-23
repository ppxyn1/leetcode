/* Write your PL/SQL query statement below */
SELECT Email --, count(*)
FROM Person
GROUP BY Email
HAVING COUNT(*) >1;