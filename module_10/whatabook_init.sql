/*
    Title: whatabook.init.sql
    Author: Ifeoluwa Adeniji
    Date: 19 Feb 2023
*/

-- drop test user if exists 
DROP USER IF EXISTS 'whatabook_user'@'localhost';

-- create whatabook_user and grant them all privileges to the whatabook database 
CREATE USER 'whatabook_user'@'localhost' IDENTIFIED WITH mysql_native_password BY 'MySQL8IsGreat!';

-- grant all privileges to the whatabook database to user whatabook_user on localhost 
GRANT ALL PRIVILEGES ON whatabook.* TO'whatabook_user'@'localhost';

-- drop contstraints if they exist
ALTER TABLE wishlist DROP FOREIGN KEY fk_book;
ALTER TABLE wishlist DROP FOREIGN KEY fk_user;

-- drop tables if they exist
DROP TABLE IF EXISTS store;
DROP TABLE IF EXISTS book;
DROP TABLE IF EXISTS wishlist;
DROP TABLE IF EXISTS user;

/*
    Create table(s)
*/
CREATE TABLE store (
    store_id    INT             NOT NULL    AUTO_INCREMENT,
    locale      VARCHAR(500)    NOT NULL,
    PRIMARY KEY(store_id)
);

CREATE TABLE book (
    book_id     INT             NOT NULL    AUTO_INCREMENT,
    book_name   VARCHAR(200)    NOT NULL,
    author      VARCHAR(200)    NOT NULL,
    details     VARCHAR(500),
    PRIMARY KEY(book_id)
);

CREATE TABLE user (
    user_id         INT         NOT NULL    AUTO_INCREMENT,
    first_name      VARCHAR(75) NOT NULL,
    last_name       VARCHAR(75) NOT NULL,
    PRIMARY KEY(user_id) 
);

CREATE TABLE wishlist (
    wishlist_id     INT         NOT NULL    AUTO_INCREMENT,
    user_id         INT         NOT NULL,
    book_id         INT         NOT NULL,
    PRIMARY KEY (wishlist_id),
    CONSTRAINT fk_book
    FOREIGN KEY (book_id)
        REFERENCES book(book_id),
    CONSTRAINT fk_user
    FOREIGN KEY (user_id)
        REFERENCES user(user_Id)
);

/*
    insert store record 
*/
INSERT INTO store(locale)
    VALUES('7819 Talladega Springs Ln, Richmond, TX 77407');

/*
    insert book records 
*/
INSERT INTO book(book_name, author, details)
    VALUES('The Guest List', 'Lucy Foley', 'The wedding night');

INSERT INTO book(book_name, author, details)
    VALUES('In Five Years', 'Rebecca Serle', 'A charming love story');

INSERT INTO book(book_name, author, details)
    VALUES('Purple Hibiscus', 'Chimamanda Adiche', 'Politcal unrest and freedom');

INSERT INTO book(book_name, author)
    VALUES('Harry Potter and the Sorcerers Stone', 'J.K. Rowling');

INSERT INTO book(book_name, author)
    VALUES('Harry Potter and the Chambers of Secrets', 'J.K. Rowling');

INSERT INTO book(book_name, author)
    VALUES('Harry Potter and the Prisoner of Azkaban', 'J.K. Rowling');

INSERT INTO book(book_name, author)
    VALUES('Harry Potter and the Goblet of Fire', 'J.K. Rowling');

INSERT INTO book(book_name, author)
    VALUES('Harry Potter and the Half-Blood Prince', 'J.K. Rowling');

INSERT INTO book(book_name, author)
    VALUES('Harry Potter and the Deathly Hallows', 'J.K. Rowling');

/*
    insert user
*/ 
INSERT INTO user(first_name, last_name) 
    VALUES('Thomas', 'Shelby');

INSERT INTO user(first_name, last_name)
    VALUES('Michael', 'Scofield');

INSERT INTO user(first_name, last_name)
    VALUES('Raymond', 'Reddington');

/*
    insert wishlist records 
*/
INSERT INTO wishlist(user_id, book_id) 
    VALUES (
        (SELECT user_id FROM user WHERE first_name = 'Thomas'), 
        (SELECT book_id FROM book WHERE book_name = 'Harry Potter and the Sorcerers Stone')
    );

INSERT INTO wishlist(user_id, book_id)
    VALUES (
        (SELECT user_id FROM user WHERE first_name = 'Michael'),
        (SELECT book_id FROM book WHERE book_name = 'In Five Years')
    );

INSERT INTO wishlist(user_id, book_id)
    VALUES (
        (SELECT user_id FROM user WHERE first_name = 'Raymond'),
        (SELECT book_id FROM book WHERE book_name = 'The Guest List')
    );
