-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.


-- Create Players table
CREATE TABLE players (
  "id"  SERIAL PRIMARY KEY,
  "name" VARCHAR(50) NOT NULL
);

-- -- Create Tournaments table
-- CREATE TABLE tournaments (
--   "id" SERIAL PRIMARY KEY,
--   "name" VARCHAR(50) NOT NULL
-- );

-- Create Matches table
CREATE TABLE matches (
  "id" SERIAL PRIMARY KEY,
  "winner_id" INTEGER REFERENCES players ("id"),
  "loser_id" INTEGER REFERENCES players ("id")
);

-- -- Create View to count number of matches each player has played
-- -- The first parameter is the tournamentId while the second is the playerId
-- CREATE VIEW matches_played($1) AS
--     SELECT count(*) FROM matches
--     WHERE winner_id = ||$1|| or loser_id = ||$1||;
--
-- -- Create View to count number of wins for each player
-- -- The first parameter is the tournamentId while the second is the playerId
-- CREATE VIEW matches_won($1) AS
--     SELECT count(*) FROM matches
--     WHERE winner_id = ||$1||;

-- Create View to return player standings
-- The View joins the players tables with the matches table twice to first count
-- the number of wins and then to count the total number of matches played.
CREATE VIEW player_standings AS
  SELECT players.id, players.name, count(matches_won.id) as wins, count(matches_played.id) as played
  FROM players 
    LEFT JOIN matches as matches_won
         ON players.id = matches_won.winner_id
    LEFT JOIN matches as matches_played
         ON players.id = matches_played.winner_id OR players.id = matches_played.loser_id
  GROUP BY players.id, players.name
  ORDER BY wins DESC
