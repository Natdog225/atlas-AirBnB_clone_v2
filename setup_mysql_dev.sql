-- setup_mysql_dev.sql
-- Script to set up MySQL database and user for the project.

-- command to run this whole script ; mysql -u root -p < setup_mysql_dev.sql 
-- create the test server.
-- mysql -u root -p < setup_mysql_test.sql

-- creates the database 'hbnb_dev_db' if it doesn't already exist
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;

-- Creates the user 'localhost' if it doesn't exist yet.
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';

-- Grants the localhost user all rights to the database
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';

-- Grant select privileges on 'performance_schema' to the user localhost
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';

-- Apply the changes
FLUSH PRIVILEGES;
