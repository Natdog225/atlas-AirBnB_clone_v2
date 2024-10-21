-- setup_mysql_dev.sql
-- Script to set up MySQL database and user for the project.

-- creates the database 'hbnb_dev_db' if it doesn't already exist
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;

-- Creates the user 'localhost' if it doesn't exist yet.
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';

-- Grants the localhost user all rights to the database
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_dev'@'localhost';

-- Grant select privileges on 'performance_schema' to the user localhost
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';

-- Apply the changes
FLUSH PRIVILEGES;
