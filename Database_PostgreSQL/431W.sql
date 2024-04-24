CREATE TABLE Player (
    date_of_birth DATE,
    name VARCHAR(100),
    batting_hand VARCHAR(20),
    bowling_skill VARCHAR(20),
    country VARCHAR(50),
    PRIMARY KEY (date_of_birth, name)
);

CREATE TABLE Team (
    name VARCHAR(100) PRIMARY KEY,
    home_wins INTEGER,
    away_wins INTEGER,
    home_matches INTEGER,
    away_matches INTEGER
);

CREATE TABLE Match (
    id INTEGER PRIMARY KEY,
    season INTEGER,
    toss_winner VARCHAR(100),
    toss_decision VARCHAR(20),
    city VARCHAR(100),
    team1 VARCHAR(100),
    team2 VARCHAR(100),
    result VARCHAR(20),
    match_date DATE
);


CREATE TABLE Delivery (
    batting_team VARCHAR(100),
    match_id INTEGER,
    inning_num INTEGER,
    non_striker VARCHAR(100),
    batsman VARCHAR(100),
    ball_num INTEGER,
    over_num INTEGER,
    PRIMARY KEY (batting_team, match_id, inning_num)
);



