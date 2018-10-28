CREATE DATABASE be_test;
use be_test;

CREATE TABLE tax_objects (
	id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
	name VARCHAR(100) NOT NULL,
	tax_code ENUM('1', '2', '3') NOT NULL,
	price BIGINT
);

INSERT INTO tax_objects(name, tax_code, price)
VALUES
('Lucky Stretch', 2, 1000),
('Big Mac', 1, 1000),
('Movie', 3, 150);