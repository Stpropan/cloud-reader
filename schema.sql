DROP TABLE IF EXISTS Users;
DROP TABLE IF EXISTS Tokens;
DROP TABLE IF EXISTS Notes;
DROP TABLE IF EXISTS Bookmarks;
DROP TABLE IF EXISTS Books;

CREATE TABLE Users(
    id BIGSERIAL NOT NULL PRIMARY KEY,
    email TEXT NOT NULL,
    password VARCHAR(255),
    settings JSON
);

CREATE TABLE Tokens(
    id BIGSERIAL NOT NULL PRIMARY KEY,
    FOREIGN KEY (user_id)
    REFERENCES Users(id),
    token TEXT,
    refresh_token TEXT,
    client_id TEXT,
    access_type VARCHAR(8),
    drive VARCHAR(255)
    );

CREATE TABLE Books(
    id BIGSERIAL NOT NULL PRIMARY KEY,
    FOREIGN KEY (user_id)
    REFERENCES Users(id),
    book_name VARCHAR(255),
    author_name VARCHAR(255),
    author_lastname VARCHAR(255),
    link TEXT,
    tags VARCHAR(255)[],
    label VARCHAR(255)
);

CREATE TABLE Notes(
    id BIGSERIAL NOT NULL PRIMARY KEY,
    FOREIGN KEY (book)
    REFERENCES Books(id),
    FOREIGN KEY (user_id)
    REFERENCES Users(id),
    note TEXT,
    text_pointer INT
);

CREATE TABLE Bookmarks(
    id BIGSERIAL NOT NULL PRIMARY KEY,
    FOREIGN KEY (book)
    REFERENCES Books(id),
    FOREIGN KEY (user_id)
    REFERENCES Users(id),
    text_pointer INT
);

