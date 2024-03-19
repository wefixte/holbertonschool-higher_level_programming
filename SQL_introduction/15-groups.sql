-- Script that lists the number of records with same score
SELECT score, COUNT(number) FROM hbtn_0d_db.second_table
GROUP BY score ORDER BY score DESC;
```
