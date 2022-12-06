-- Prepares a MySQL server
-- Create database
CREATE DATABASE IF NOT EXISTS hbnb_test_db;
-- Create user
CREATE USER 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';
-- Add privileges
GRANT USAGE ON * . * TO 'hbnb_test'@'localhost';
GRANT SELECT ON performance_schema . * TO 'hbnb_test'@'localhost';
GRANT ALL PRIVILEGES ON hbnb_test_db . * TO 'hbnb_test'@'localhost';
