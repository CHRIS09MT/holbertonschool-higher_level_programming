-- 3 first students in the Batch ID=3
-- because Batch 3 is the best!
DROP TABLE IF EXISTS second_table;

CREATE TABLE IF NOT EXISTS second_table (
       id INT AUTO_INCREMENT PRIMARY KEY,
       name VARCHAR(50),
       score INT
);

INSERT INTO second_table (name, score)
       VALUES
       ('John', 10),
       ('Alex', 3),
       ('Bob', 14),
       ('George', 8);
