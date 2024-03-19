-- Script that creates a table and add multiples rows
CREATE TABLE IF NOT EXISTS hbtn_0d_db.second_table (
	id INT,
	name VARCHAR(256),
	score INT
);
INSERT INTO hbtn_0d_db.second_table (id, name, score) VALUES 
(1, 'John', 100);
(2, 'Alex', 3);
(3, 'Bob', 14);
(4, 'George', 8);
```
