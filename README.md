# Team 4 - Laser Tag


# Team members
1. Nick Brown
1. Jase Cornett
1. Kormah Dorko
1. Austin Flynn
1. David Hammons
1. Logan Milazzo
1. Rodrigo Mouron
1. Stephanie Stock

# To run the project (Mac), run the following commands:
```python
Before starting you must delete previous player data from Heroku
First you need to login to our Heroku account using our credentials
$ heroku login
(After this command it will bring you to the page to login)
Next you need to enter the psql for our data and delete using the two commands below
$ heroku pg:psql -a laser-tag-spring-2022
$ delete from player;
Now you can run the project
(While in project folder, when you put ls, you see "main.py")
$ export FLASK_APP=main
$ flask run
  * Runs on http://127.0.0.1:5000/
Follow the link (cmd + click)
When splash screen loads click on screen to go to player entry screen
Enter players information
Click "Enter" to send players to database and goes to playerAction.html
The timer will show up, then wait about 10 seconds for players to show up

```

# To run the project (Windows), run the following commands:
```python
Before starting you must delete previous player data from Heroku
First you need to login to our Heroku account using our credentials
> heroku login
(After this command it will bring you to the page to login)
Next you need to enter the psql for our data and delete using the two commands below
> heroku pg:psql -a laser-tag-spring-2022
> delete from player;
Now you can run the project
(While in project folder, when you put ls, you see "main.py")
> set FLASK_APP=main
> python3 -m flask run
  * Runs on http://127.0.0.1:5000/
Follow the link (ctrl + click)
When splash screen loads click on screen to go to player entry screen
Enter players information
Click "Enter" to send players to database and goes to playerAction.html
The timer will show up, then wait about 10 seconds for players to show up
 
```

# To install Flask (Terminal commands)
```python
pip3 install Flask

```

# To install PSQL on Mac using Brew (Terminal commands)
```python
$brew install postgresql

```

# To install PSQL on Windows (Instructions given in Sprint 2 Document)
```python
PostgreSQL client [https://www.enterprisedb.com/downloads/postgres-postgresql-downloads]
Download and run the setup wizard for you system architecture
During component installation only select pgAdmin, which is a graphical UI client
Technically you don’t need pgAdmin, but it installs psql which you will need
The Heroku CLI will use the PostgreSQL client, psql, to communicate with the PostgreSQL
You don’t need the PostgreSQL database server as that will be hosted on Heroku’s servers
Though if you want to run your database locally this is the way to install it
You can verify access via the Command Prompt using the following command
psql -V
If that doesn’t work then you will need to update your system’s PATH variable and then restart your Command Prompt
Add an entry similar to [C:\Program Files\PostgreSQL12\bin\]


```

# Sprint 3 Notes:
1. Update Trello cards
1. Create play action screen
1. Change to play action screen by clicking "Enter" button
1. Code the countdown timer
1. Slack reports 
1. Individual github commits

# Kill Command
(CTRL+C to kill)
