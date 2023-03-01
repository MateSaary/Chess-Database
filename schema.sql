DROP TABLE IF EXISTS news;

CREATE TABLE news
(
    blog_id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    date TEXT NOT NULL,
    content TEXT NOT NULL
);

INSERT INTO news (title, date, content)
VALUES
    ('First Blog', '2023-01-14', 'You are reading the first ever blog entry on CTC''s brand new site! Welcome! This site provides information on upcoming tournaments, allows you to purchase tickets for them, and provides the most up-to-date information on past tournaments.'),
    ('First Tournament', '2023-01-16', 'This is to announce our first ever tournament, happening this Friday 20th! For more details please visit the store page.'),
    ('Tomorrow''s a big day!', '2023-01-19', 'Final preparations have been made, everything is set and ready for the inaugural chess tournament organised by CTC. Ticket holders: don''t forget to make note of the venue and start time and to be there at least 60 minutes early to ensure entry.'),
    ('Massive Success!', '2023-01-21', 'A massive thank you to everyone who participated in yesterday''s tournament, and congratulations to Cagnus Marlsen, the first ever winner of a CTC organised chess tournament.'); 

DROP TABLE IF EXISTS users;

CREATE TABLE users
(
    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    password TEXT NOT NULL,
    is_admin INTEGER NOT NULL
);

INSERT INTO users (username, password, is_admin)
VALUES
    ('admin1', 'chess123', '1');