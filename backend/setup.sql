-- CREATE notes TABLE
CREATE TABLE notes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title VARCHAR(45),
    subtitle VARCHAR(45),
    body TEXT,
    created_on DATETIME
);
-- INSERT example note
INSERT INTO notes (
    title,
    subtitle,
    body,
    created_on
) VALUES (
    "Example Note",
    "Made by Jorge",
    "This is an example note",
    DATETIME("now")
);
