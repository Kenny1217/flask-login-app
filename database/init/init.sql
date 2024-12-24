---------------------------------------------------------------------
-- POSTGRES DATABASE INITIALIZE SCRIPT
-- Author: Kenny Morris
-- Creation date: 12/23/2024
---------------------------------------------------------------------

-- Create a new user with a password
CREATE USER FLASK_DB_USER WITH PASSWORD 'my_password';

-- Create a new database
CREATE DATABASE FLASK_APP_DATABASE;

-- Grant privileges to the user on the database
GRANT ALL PRIVILEGES ON DATABASE FLASK_APP_DATABASE TO FLASK_DB_USER;

-- Connect to the database
\c FLASK_APP_DATABASE

-- Create USERS table
CREATE TABLE IF NOT EXISTS USERS (
    ID INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    USERNAME TEXT UNIQUE NOT NULL,
    EMAIL TEXT UNIQUE NOT NULL,
    PASSWORD_HASH TEXT NOT NULL,
    ROLE_ID INT NOT NULL DEFAULT 1,
    CREATED_DATE TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL,
    LAST_ACTIVE TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL
);

-- Create ROLES table
CREATE TABLE IF NOT EXISTS ROLES (
    ROLE_ID INT NOT NULL PRIMARY KEY,
    ROLE_NAME TEXT NOT NULL,
    ROLE_DESCRIPTION TEXT NOT NULL
);

-- Insert BAN role to ROLES table
INSERT INTO ROLES (ROLE_ID, ROLE_NAME, ROLE_DESCRIPTION) VALUES (0, 'BAN', 'This role is for banned users');
-- Insert USER role to ROLES table
INSERT INTO ROLES (ROLE_ID, ROLE_NAME, ROLE_DESCRIPTION) VALUES (1, 'USER', 'This role is for regular users');
-- Insert ADMIN role to ROLES table
INSERT INTO ROLES (ROLE_ID, ROLE_NAME, ROLE_DESCRIPTION) VALUES (2, 'ADMIN', 'This role is for admin users');



