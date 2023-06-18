-- DROP DATABASE inventory;
-- CREATE DATABASE inventory;

-- USE inventory;

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50),
    password VARCHAR(50)
);

INSERT INTO users (username, password) VALUES ('admin', 'admin');

CREATE TABLE barang (
    id INT AUTO_INCREMENT PRIMARY KEY,
    kode_barang VARCHAR(50) UNIQUE,
    nama_barang VARCHAR(255),
    jumlah_barang INT,
    harga_barang DECIMAL(10,2),
    keuntungan DECIMAL(10,2)
);
