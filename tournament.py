#!/usr/bin/env python
#
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2
import pdb

def connect(database_name="tournament"):
    """Connect to the Postgrequery database.  Returns a database connection."""
    try:
        db = psycopg2.connect("dbname={}".format(database_name))
        cursor = db.cursor()
        return db, cursor
    except:
        print("<your error message>")


def deleteMatches():
    """Remove all the match records from the database."""
    db, cursor = connect()
    query = 'DELETE FROM matches'
    cursor.execute(query)
    db.commit()
    db.close()


def deletePlayers():
    """Remove all the player records from the database."""
    db, cursor = connect()
    query = 'DELETE FROM players'
    cursor.execute(query)
    db.commit()
    db.close()


def countPlayers():
    """Returns the number of players currently registered."""
    db, cursor = connect()
    query = 'SELECT count(*) FROM players'
    cursor.execute(query)
    players_count = cursor.fetchone()
    db.close()
    return players_count[0]


def registerPlayer(name):
    """Adds a player to the tournament database.

    The database assigns a unique serial id number for the player.  (This
    should be handled by your query database schema, not in your Python code.)

    Args:
      name: the player's full name (need not be unique).
    """
    db, cursor = connect()
    query = 'INSERT INTO players (name) values (%s)'
    params = (name,)
    cursor.execute(query, params)
    db.commit()
    db.close()


def playerStandings():
    """Returns a list of the players and their win records, sorted by wins.

    The first entry in the list should be the player in first place, or a player
    tied for first place if there is currently a tie.

    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """
    db, cursor = connect()
    query = 'SELECT * FROM player_standings'
    cursor.execute(query)
    player_standings = cursor.fetchall()
    db.close()
    return player_standings


def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
    db, cursor = connect()
    query = 'INSERT INTO matches (winner_id, loser_id) values (%s, %s)'
    params = (winner,loser)
    cursor.execute(query, params)
    db.commit()
    db.close()


def swissPairings():
    """Returns a list of pairs of players for the next round of a match.

    Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings.  Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player adjacent
    to him or her in the standings.

    Returns:
      A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the second player's name
    """
    standings = playerStandings()
    swissPairings = list()

    # Iterate over the list two at a time, the zip method splits the single list
    # into two list, the first list containing the elements with even indices,
    # index % 2 = 0. The second list contains the elements with odd indices,
    # index % 2 = 1.
    #
    # Source: Stack Overflow - https://goo.gl/AKmuXk
    for player_1, player_2 in zip(standings[0::2], standings[1::2]):
        swissPairings.append((player_1[0], player_1[1], player_2[0], player_2[1]))

    return swissPairings
