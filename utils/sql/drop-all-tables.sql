USE `LeetCode`;

DELIMITER //

CREATE PROCEDURE drop_all_tables()
BEGIN

SET @tables = NULL;
SET GROUP_CONCAT_MAX_LEN=32768;
SELECT GROUP_CONCAT('`', table_schema, '`.`', table_name, '`') INTO @tables
  FROM information_schema.tables
  WHERE table_schema = (SELECT DATABASE());

IF @tables IS NOT NULL THEN

SET FOREIGN_KEY_CHECKS = 0;
SET @tables = CONCAT('DROP TABLE IF EXISTS ', @tables);
SELECT @tables;
PREPARE stmt FROM @tables;
EXECUTE stmt;
DEALLOCATE PREPARE stmt;
SET FOREIGN_KEY_CHECKS = 1;

END IF;

END //

DELIMITER ;

CALL drop_all_tables();

DROP PROCEDURE drop_all_tables;
