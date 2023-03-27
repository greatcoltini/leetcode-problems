# Write your MySQL query statement below

SELECT t1.id

FROM Weather AS t1,

     Weather AS t2

WHERE

    dateDiff(t1.recordDate, t2.recordDate) = 1

    AND

    t1.temperature > t2.temperature    
