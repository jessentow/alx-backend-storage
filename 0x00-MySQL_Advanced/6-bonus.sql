-- an SQL script which creates a stored procedure AddBonus
-- this adds a new correction for a student.
DELIMITER //
CREATE PROCEDURE AddBonus (
    IN user_id int,
    IN project_name varchar(255),
    IN score int
    )
    BEGIN
    INSERT INTO projects (name)
    SELECT project_name FROM DUAL

    WHERE NOT EXISTS (SELECT * FROM projects WHERE name = project_name);
    INSERT INTO corrections (user_id, project_id, score)
    VALUES (user_id, (SELECT id FROM projects WHERE name = project_name), score);
END;
//
DELIMITER ;
