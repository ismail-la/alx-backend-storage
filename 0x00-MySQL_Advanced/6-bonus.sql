-- SQL script creates a stored procedure named 'AddBonus' which takes in three parameters user_id, project_name and score.

DELIMITER $$;
CREATE PROCEDURE AddBonus(IN a_user_id INT, IN a_project_name VARCHAR(255), IN a_score INT )
BEGIN
	IF NOT EXISTS(SELECT name FROM projects WHERE name=a_project_name) THEN
		INSERT INTO projects (name) VALUES (a_project_name);
	END IF;
	INSERT INTO corrections (a_user_id, a_project_id, a_score)
	VALUES (a_user_id, (SELECT id from projects WHERE name=a_project_name), a_score);
END;$$
DELIMITER ;
