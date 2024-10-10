-- Create a new database called 'NEATestDb'
-- Connect to the 'master' database to run this snippet
USE master
GO
-- Create the new database if it does not exist already
IF NOT EXISTS (
    SELECT name
        FROM sys.databases
        WHERE name = N'NEATestDb'
)
CREATE DATABASE NEATestDb
GO

SELECT