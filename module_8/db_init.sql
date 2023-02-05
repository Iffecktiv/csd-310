/*
    Title: db_init.sql
    Author: Ifeoluwa Adeniji
    Date: 5 Feb 2023
    Description: pysports database initialization script.
*/

-- drop test user if exists 
DROP USER IF EXISTS 'pysports_user'@'localhost';


-- create pysports_user and grant them all privileges to the pysports database 
CREATE USER 'pysports_user'@'localhost' IDENTIFIED WITH mysql_native_password BY 'MySQL8IsGreat!';

-- grant all privileges to the pysports database to user pysports_user on localhost 
GRANT ALL PRIVILEGES ON pysports.* TO'pysports_user'@'localhost';


-- drop tables if they are present
DROP TABLE IF EXISTS players;
DROP TABLE IF EXISTS team;


-- create the team table 
CREATE TABLE team (
    team_id     INT             NOT NULL        AUTO_INCREMENT,
    team_name   VARCHAR(50)     NOT NULL,
    mascot      VARCHAR(50)     NOT NULL,
    PRIMARY KEY(team_id)
); 

-- create the player table and set the foreign key
CREATE TABLE players (
    player_id   INT             NOT NULL        AUTO_INCREMENT,
    first_name  VARCHAR(50)     NOT NULL,
    last_name   VARCHAR(50)     NOT NULL,
    team_id     INT             NOT NULL,
    PRIMARY KEY(player_id),
    CONSTRAINT fk_team 
    FOREIGN KEY(team_id)
        REFERENCES team(team_id)
);


-- insert team records
INSERT INTO team(team_name, mascot)
    VALUES('Borussia', 'Panther');

INSERT INTO team(team_name, mascot)
    VALUES('Dortmund', 'Lion');


-- insert player records 
INSERT INTO players(first_name, last_name, team_id) 
    VALUES('Ifeoluwa', 'Adeniji', (SELECT team_id FROM team WHERE team_name = 'Borussia'));

INSERT INTO players(first_name, last_name, team_id)
    VALUES('John', 'Wick', (SELECT team_id FROM team WHERE team_name = 'Borussia'));

INSERT INTO players(first_name, last_name, team_id)
    VALUES('Jack', 'Sparrow', (SELECT team_id FROM team WHERE team_name = 'Borussia'));

INSERT INTO players(first_name, last_name, team_id) 
    VALUES('James', 'Bond', (SELECT team_id FROM team WHERE team_name = 'Dortmund'));

INSERT INTO players(first_name, last_name, team_id)
    VALUES('John', 'Cena', (SELECT team_id FROM team WHERE team_name = 'Dortmund'));

INSERT INTO players(first_name, last_name, team_id)
    VALUES('Jason', 'Statham', (SELECT team_id FROM team WHERE team_name = 'Dortmund'));