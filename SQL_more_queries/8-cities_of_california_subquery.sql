-- 3 first students in the Batch ID=3
-- because Batch 3 is the best!
SELECT id, name
    FROM cities
    WHERE state_id IN (
        SELECT name = "California"
        FROM states
    );
