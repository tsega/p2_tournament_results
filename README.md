# P2 Tournament Results

A Result keeping system that ranks and swiss-pairs players of a tournament.  

# What's included

Excluding this `README.md` file there are three python files:

  - **tournament.sql** - Contains SQL statements to create tables in the tournament database to keep track of players and matches. Also contains a view that provides the player standings.
   the web page.
  - **tournament.py** - The python module, that contains methods to connect to the database, manage (add/delete) matches and players. Also provides methods to do the swiss-pairing and get player standings
  - **tournament_test.py** - The entry to the application, contains code to check the proper functioning of the `tournament.py` module.

# How to run the project

The requirements for running this project are:
  - A Postgresql database
  - A working Python (2.7 or 3.0) installation

These can be setup using [Vagrant](http://vagrantup.com/) and [VirtualBox](https://www.virtualbox.org/). For this particular case, one can use the vagrant based [virtual machine](https://github.com/udacity/fullstack-nanodegree-vm) setup by Udacity for the Full Stack Web Developer Nanodegree program.

Once the above setup is done and you are connect to the virtual machine, follow the instructions below to run the project:
  1. Copy the contents of this repository to the virtual machine project folder. This is located at `/vagrant/tournament/`.
  2. Connect to the Postgresql Database Management Console; simply type `psql` in your terminal.
  3. When connected, setup the tournament database by importing the `tournament.sql` file as follows; `\i tournament.sql`, this will create the database including the tables and view used in the application.
  4. Disconnect from `psql` by typing in `\q`.
  5. Run the `tournament_test.py` program; `python tournament_test.py`.


# Creator

**Tsegaselassie Tadesse**

  - http://twitter.com/tsegat
  - http://github.com/tsega
