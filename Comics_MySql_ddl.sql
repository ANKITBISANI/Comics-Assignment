create database  comics ; 

USE comics;

CREATE TABLE `comics_details` (
`names` varchar(500) DEFAULT NULL,
`alt_text` varchar(500) DEFAULT NULL,
`number` int DEFAULT NULL,
`link` varchar(500) DEFAULT NULL,
`image` varchar(500) DEFAULT NULL,
`image_link` varchar(500) DEFAULT NULL
) ;
                             