-- Script that lists all records, score and name, by descending score
SELECT score, name FROM hbtn_0d_db.second_table
WHERE name IS NOT NULL ORDER BY score DESC;
```
