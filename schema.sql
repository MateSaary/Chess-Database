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
    ('First Blog', '2023-02-08', 'You are reading the first ever blog entry on CTC''s brand new site! Welcome! This site provides information on upcoming tournaments, allows you to purchase tickets for them, and provides the most up-to-date information on past tournaments.'),
    ('First Tournament', '2023-02-10', 'This is to announce our first ever tournament, happening this Sunday! For more details please visit the store page.'),
    ('Tomorrow''s a big day!', '2023-02-11', 'Final preparations have been made, everything is set and ready for the inaugural chess tournament organised by CTC. Ticket holders: don''t forget to make note of the venue and start time and to be there at least 60 minutes early to ensure entry.'),
    ('Massive Success!', '2023-02-13', 'A massive thank you to everyone who participated in yesterday''s tournament, and congratulations to Cagnus Marlsen, the first ever winner of a CTC organised chess tournament.'),
    ('First ever Rapid Tournament', '2023-02-20', 'As our continued effort to expand our reach for all players, CTC are introducing a new tournament series based on the rapid time control. The first iteration of this series will be played on the 28th of this month.'),
    ('New Bullet Series!', '2023-03-05', 'We are happy to announce our newest tournament series featuring the tense bullet time control! For this first iteration, the time control will be set to 2 minutes per player per game. Best of luck to participants!'); 

DROP TABLE IF EXISTS users;

CREATE TABLE users
(
    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    password TEXT NOT NULL,
    is_admin INTEGER NOT NULL
);

DROP TABLE IF EXISTS tournaments;

CREATE TABLE tournaments
(
    tournament_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    date TEXT NOT NULL,
    start_time TEXT NOT NULL,
    entry_fee REAL NOT NULL,
    prize_money REAL NOT NULL,
    description TEXT NOT NULL,
    winner TEXT
);

INSERT INTO tournaments (name, date, start_time, entry_fee, prize_money, description)
VALUES
    ('Inaugural CTC Tournament', '2023-02-12', '18:00', 10, 100, 'This is the first ever tournament organised by CTC.'),
    ('CTC Inaugural Tournament #2', '2023-02-14', '19:00', 10, 150, 'A second iteration of the inaugural tournament, with a higher prize pool.'),
    ('CTC Tournament Series #1', '2023-02-17', '17:00', 19.99, 150, 'Welcome to CTC''s first official series-based tournament. Along with the prize money associated, the winner will receive free entry into the next tournament of this series.'),
    ('CTC Checkmate Circuit #1', '2023-02-19', '19:00', 24.99, 200, 'Welcome to CTC''s first ever tournament series with a time control of 5 minutes per player per game. This tournament will be played over 5 rounds.'),
    ('CTC Tournament Series #2', '2023-02-25', '17:00', 19.99, 150, 'Welcome to CTC''s second series-based tournament. We look forward to seeing you there!'),
    ('CTC Rapid Series #1', '2023-02-28', '19:00', 24.99, 200, 'Welcome to CTC''s first rapid tournament. This tournament will be played over 3 rounds, with a 10 minute time control per player per game.'),
    ('CTC Checkmate Circuit #2', '2023-03-01', '19:00', 24.99, 200, 'Welcome to CTC''s second ever tournament series with a time control of 5 minutes per player per game. This tournament will be played over 5 rounds.'),
    ('CTC Tournament Series #3', '2023-03-04', '16:00', 14.99, 150, 'This iteration of CTC''s series tournament comes with a 25% discount to usual entry fees!'),
    ('CTC Checkmate Circuit #3', '2023-03-06', '15:00', 19.99, 200, 'The third iteration of the checkmate circuit, now with a discounted entry fee.'),
    ('CTC Bullet Challengers #1', '2023-03-26', '19:00', 24.99, 200, 'Welcome to CTC''s first ever bullet tournament! The tournament will be played over 5 rounds, with a 2 minute time control per player per game.'),
    ('CTC Tournament Series #4', '2023-03-30', '18:00', 14.99, 125, 'Welcome back to CTC''s tournament series. This tournament will be played over 3 rounds with a 30 minute time control per player per game.'),
    ('CTC Rapid Series #2', '2023-04-08', '15:00', 19.99, 150, 'CTC''s second ever rapid tournament! 3 rounds, with a 10 minute time control as before will be used.'),
    ('CTC Checkmate Circuit #4', '2023-04-14', '13:00', 17.50, 175, 'The fourth iteration of the checkmate circuit, with a revised entry fee and prize pool.');

DROP TABLE IF EXISTS participants;

CREATE TABLE participants
(
    participant_id INTEGER PRIMARY KEY AUTOINCREMENT,
    tournament_id INTEGER NOT NULL,
    name TEXT,
    FOREIGN KEY (tournament_id) REFERENCES tournaments(tournament_id)
);

INSERT INTO participants (tournament_id, name)
VALUES
    (1, 'Cagnus Marlsen'),
    (1, 'Georgia Miles'),
    (1, 'Maximus Chen'),
    (1, 'Julian West'),
    (1, 'Calvin Wong'),
    (2, 'Nikaru Hakamura'),
    (2, 'Ethan Alvarez'),
    (2, 'Oliver Guerra'),
    (3, 'Sophia Carlson'),
    (3, 'Isabel Jordan'),
    (3, 'Daniel Silva'),
    (3, 'Caleb Ortiz');
