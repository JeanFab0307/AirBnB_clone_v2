-- creates DB hbnb_test_db and user hbnb_test in localhost

CREATE DATABASE IF NOT EXISTS hbnb_test_db;
CREATE USER IF NOT EXISTS 'hbnb_test'@'localthost' IDENTIFIED BY 'hbnb_test_pwd';
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localthost';
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localthost';
