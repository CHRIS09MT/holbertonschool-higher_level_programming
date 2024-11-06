-- 3 first students in the Batch ID=3
-- because Batch 3 is the best!
CREATE TABLE IF NOT EXISTS second_table (
       id INT PRIMARY KEY,
       name VARCHAR(50),
       score INT
);

INSERT INTO second_table (id, name, score)
       VALUES
       (1, 'John', 10),
       (2, 'Alex', 3),
       (3, 'Bob', 14),
       (4, 'George', 8);
