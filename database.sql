CREATE DATABASE stego_db;

USE stego_db;

CREATE TABLE images (
    id INT AUTO_INCREMENT PRIMARY KEY,
    filename VARCHAR(255) NOT NULL,
    description TEXT,
    upload_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);