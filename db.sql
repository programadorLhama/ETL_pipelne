CREATE DATABASE IF NOT EXISTS pipeline_db;

CREATE TABLE IF NOT EXISTS `pipeline_db`.`artists` (
    id BIGINT NOT NULL AUTO_INCREMENT,
    first_name VARCHAR(255),
    second_name VARCHAR(255),
    surname VARCHAR(255),
    artist_id BIGINT,
    link VARCHAR(255),
    extraction_date DATETIME NOT NULL,
    primary key (id)
) ENGINE=INNODB;