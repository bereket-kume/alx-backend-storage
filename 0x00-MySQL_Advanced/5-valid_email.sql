-- script that creates a trigger that resets valid_email if the email changes
DELIMITER //

CREATE TRIGGER validate
BEFORE UPDATE
ON users
FOR EACH ROW
BEGIN
    IF NEW.email != OLD.email THEN
        SET valid_email = 0
    END IF;
END //

DELIMITER ;
