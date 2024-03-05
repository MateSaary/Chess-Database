# Chess Database/Tournament Website

A project I worked on as part of University coursework.

## Description

A chess database developed using the lightweight Flask (Python) micro web framework and Jinja templating engine. Database created using SQL.

## Getting Started

The fastest way to get the Flask app running follows these steps:

  1. Flask must be installed, view "Dependencies" for more info.

  2. Locally install the files.
    
  3. Using a terminal, run `python -m flask` in the local directory containing app.py.
     
  4. The console will return a locally hosted URL, looking like this: `Running on http://127.0.0.1:5000 (Press CTRL+C to quit)`

  5. The app can be accessed via the returned link in any browser.

### Dependencies

  Flask supports Python 3.8 and newer. 

Flask also automatically installs the following distributions:
* Werkzeug
* Jinja
* MarkupSafe
* ItsDangerous
* Click
* Blinker

For more information see [this link](https://flask.palletsprojects.com/en/3.0.x/installation/).

### Installing Flask

Ensuring you are within the appropriate directory (where app.py is located), install Flask using the terminal: `pip install Flask`


## Help

#### _Q: The app is running, what now?_

A: The site has two types of users. Regular users are able to register via the registration page. Admin users will be automatically directed to the admin dashboard after login.
The base admin login details are as follows:
* Username: admin
* Password: chess123

#### _Q: How can the default admin login be changed?_

A: This can be done by accessing/modifying the already initialised database, or reinitialising a new database (Of course, this wipes all existing accounts). The app works by determining a difference between users and admins by the column "is_admin" in the database (0=user, 1=admin).

#### _Q: All the "dummy data" tournaments are in the past, how can new ones be added?_

A: The admin dashboard allows for control of all important areas of the website in an easy to use interface. However you can alternatively modify the database (app.db) file if you wish. This is also the better solution if you wish to use queries to modify the data.

## License

This project is licensed under the MIT License - see the LICENSE.md file for details
