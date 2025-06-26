-- Create user 'user_0d_1' with the password: 'user_0d_1_pwd'
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
-- Grants all privileges
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';
