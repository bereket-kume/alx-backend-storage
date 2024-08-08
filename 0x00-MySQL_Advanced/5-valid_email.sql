-- script that creates a trigger that resets valid_email if the email changes
DELIMITER //

CREATE TRIGGER validate
BEFORE UPDATE
ON users
FOR EACH ROW
BEGIN
    IF NEW.email != OLD.email THEN
        UPDATE users
        SET valid_email = 0
        WHERE id = NEW.id;
    END IF;
END //

DELIMITER ;
