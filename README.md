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
Next you need to enter the psql for our data and delete
$ heroku pg:psql -a laser-tag-spring-2022
$ delete from player;
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
Next you need to enter the psql for our data and delete
> heroku pg:psql -a laser-tag-spring-2022
> delete from player;
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

# Sprint 2 Notes:
1. Git repositories created
1. Splash Screen created
1. Player entry screen created
1. Database linked to Application
1. 2 Player addition to database through App
1. Trello tasks assigned
1. Individual github commits

# Kill Command
(CTRL+C to kill)
