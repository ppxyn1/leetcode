/* Write your PL/SQL query statement below */
SELECT C.NAME AS Customers
FROM Customers C
Left JOIN Orders o ON c.id = o.CustomerId
WHERE O.ID IS NULL