create database test;

use test;

CREATE TABLE admindata (
    id INT PRIMARY KEY,
    username VARCHAR(50),
    password VARCHAR(50)
);

CREATE TABLE buynow (
    base VARCHAR(20),
    toppings VARCHAR(20),
    qty INT,
    totalamt INT
);

CREATE TABLE cart (
    base VARCHAR(20),
    toppings VARCHAR(20),
    qty INT
);

-- drop table if exists savedata;
CREATE TABLE if not exists savedata (
    id INT AUTO_INCREMENT PRIMARY KEY,
    firstname VARCHAR(255),
    lastname VARCHAR(255),
    contact INT,
    gender VARCHAR(10)
);

CREATE TABLE userdata (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(255),
    password1 VARCHAR(255),
    password VARCHAR(255)
);

insert into userdata values (1, "megh@gmail.com", "123megh", "");