
CREATE TABLE if not exists øvelser (
    navn varchar(20),
    Muskelgruppe varchar(10),
);

INSERT INTO øvelser (navn, Muskelgruppe) VALUES
    ('benk press', 'chest'),
    ('incline db', 'chest'),
    ('chest flies', 'chest'),
    ('dips', 'chest'),
    ('pull ups', 'back'),
    ('lat pulldown', 'back'),
    ('cable rows', 'back'),
    ('face pulls', 'back'),
    ('leg press', 'legs'),
    ('calf raises', 'legs'),
    ('leg extensions', 'legs'),
    ('leg curls', 'legs'),
    ('deadlift', 'legs'),
    ('preacher curls', 'biceps'),
    ('incline curls', 'biceps'),
    ('tricep dips', 'tricep'),
    ('tricep extensions', 'tricep'),
    ('shoulder press', 'skuldre'),
    ('lat raises', 'skuldre'),



CREATE TABLE IF NOT EXISTS chest (
    navn VARCHAR(20),
    reps INT,
    sets INT,
    weight INT,
    pr INT
);

INSERT INTO chest (navn, reps, sets, weight, pr) VALUES 
    ('benkpress', 6, 3, 100, 120),
    ('incline dumbell', 8, 3, 30, NULL),
    ('chest flies (low)', 12, 3, 20, NULL),
    ('dips', 10, 2, 25, NULL);

CREATE TABLE IF NOT EXISTS rygg (
    navn VARCHAR(20),
    reps INT,
    sets INT,
    weight INT,
    pr INT
);

INSERT INTO rygg (navn, reps, sets, weight, pr) VALUES
    ('pull ups', 10, 2, 5, 13),
    ('lat pulldown', 10, 3, 65, NULL),
    ('cable rows', 10, 3, 74, NULL),
    ('face pulls', 15, 4, 30, NULL);

CREATE TABLE IF NOT EXISTS legs (
    navn VARCHAR(20),
    reps INT,
    sets INT,
    weight INT,
    pr INT
);

INSERT INTO legs (navn, reps, sets, weight, pr) VALUES
    ('squats', 10, 3, 70, NULL),
    ('calf raises', 10, 3, 30, NULL),
    ('leg extensions', 8, 2, 70, NULL),
    ('leg curls', 8, 2, 50, NULL),
    ('deadlift', 10, 3, 60, NULL);

CREATE TABLE IF NOT EXISTS biceps (
    navn VARCHAR(20),
    reps INT,
    sets INT,
    weight INT,
    pr INT
);

INSERT INTO biceps (navn, reps, sets, weight, pr) VALUES
    ('preacher curls', 9, 2, 22, NULL),
    ('incline curls', 24, 3, 12, NULL);

CREATE TABLE IF NOT EXISTS triceps (
    navn VARCHAR(20),
    reps INT,
    sets INT,
    weight INT,
    pr INT
);

INSERT INTO triceps (navn, reps, sets, weight, pr) VALUES
    ('dips', 10, 2, 25, NULL),
    ('tricep extensions', 10, 2, 25, NULL);

CREATE TABLE IF NOT EXISTS skuldre (
    navn VARCHAR(20),
    reps INT,
    sets INT,
    weight INT,
    pr INT
);

INSERT INTO skuldre (navn, reps, sets, weight, pr) VALUES
    ('shoulder press', 10, 3, 28, NULL),
    ('lateral raises', 15, 2, 12, NULL);
