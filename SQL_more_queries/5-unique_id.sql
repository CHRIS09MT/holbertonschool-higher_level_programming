-- 3 first students in the Batch ID=3
-- because Batch 3 is the best!
CREATE TABLE IF NOT EXISTS unique_id (
       id INT UNIQUE DEFAULT 1,
       name VARCHAR(256)
);
