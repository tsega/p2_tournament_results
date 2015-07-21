-- Create the database, removes it if it already exists to create a clean database
DROP DATABASE IF EXISTS tournament;
CREATE DATABASE tournament;

-- Connect to the tournament database to start creating tables and view
\c tournament

-- Create Players table
CREATE TABLE players (
  "id"  SERIAL PRIMARY KEY,
  "name" VARCHAR(50) NOT NULL
);

-- Create Matches table
CREATE TABLE matches (
  "id" SERIAL PRIMARY KEY,
  "winner_id" INTEGER REFERENCES players ("id"),
  "loser_id" INTEGER REFERENCES players ("id")
);

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
